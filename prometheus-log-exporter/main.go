package main

import (
	"encoding/json"
	"flag"
	"fmt"
	"time"

	"net/http"
	"os"

	"github.com/prometheus/client_golang/prometheus"
	"github.com/prometheus/client_golang/prometheus/promhttp"
	"github.com/prometheus/common/log"
)

var (
	listenAddress = flag.String("web.listen-address", ":9141",
		"Address to listen on for telemetry")
	metricsPath = flag.String("web.telemetry-path", "/metrics",
		"Path under which to expose metrics")
	logParserEndpoint = flag.String("log_parser_api_url",
		"http://flask-api:5000/api/rsync/logs_count",
		"Path under which to expose metrics")
)

func main() {
	flag.Parse()

	if *logParserEndpoint == "" {
		fmt.Fprintln(os.Stderr, "Please provide a address for Log Parser API")
		os.Exit(1)
	}

	log.Infoln("Starting Log Parser API exporter")

	exporter, err := NewExporter(*logParserEndpoint)
	if err != nil {
		fmt.Println("Error initializing Service API exporter.")
		os.Exit(1)
	}

	prometheus.MustRegister(exporter)

	http.Handle(*metricsPath, promhttp.Handler())

	log.Infof("Listening on %s", *listenAddress)

	if err := http.ListenAndServe(*listenAddress, nil); err != nil {
		log.Fatal(err)
	}
}

const (
	namespace = "service_api"
)

var (
	up = prometheus.NewDesc(
		prometheus.BuildFQName(namespace, "", "up"),
		"Was the last query of Log Parser API successful.",
		nil, nil,
	)
	rsyncLogsReceived = prometheus.NewDesc(
		prometheus.BuildFQName(namespace, "", "rsync_logs_received_total"),
		"How many rsync logs have been received.",
		nil, nil,
		// []string{"channel"}, nil,
	)
)

type Info struct {
	NumLogs int `json:"NumLogs"`
}

type Exporter struct {
	client            *http.Client
	logParserEndpoint string
}

func NewExporter(logParserEndpoint string) (*Exporter, error) {
	h := &http.Client{Timeout: 10 * time.Second}

	return &Exporter{client: h, logParserEndpoint: logParserEndpoint}, nil
}

func (e *Exporter) Describe(ch chan<- *prometheus.Desc) {
	ch <- up
	ch <- rsyncLogsReceived
}

func (e *Exporter) Collect(ch chan<- prometheus.Metric) {
	numLogs, err := e.fetchNumberOfLogs()
	if err != nil {
		ch <- prometheus.MustNewConstMetric(
			up, prometheus.CounterValue, 0,
		)
		log.Error("Can't query Log Parser API: %v", err)
		return
	}

	ch <- prometheus.MustNewConstMetric(
		rsyncLogsReceived, prometheus.CounterValue, float64(numLogs),
	)
}

func (e *Exporter) fetchNumberOfLogs() (int, error) {
	r, err := e.client.Get(e.logParserEndpoint)
	if err != nil {
		return 0, err
	}
	defer r.Body.Close()

	var info Info

	err = json.NewDecoder(r.Body).Decode(&info)
	if err != nil {
		return 0, err
	}

	return info.NumLogs, nil
}
