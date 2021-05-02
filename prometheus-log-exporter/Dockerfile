FROM golang:1.16
RUN mkdir /usr/src/prometheus-log-exporter/
COPY . /usr/src/prometheus-log-exporter/
WORKDIR /usr/src/prometheus-log-exporter/
RUN go mod download
RUN go build -o main .
EXPOSE 9141
ENTRYPOINT [ "./main" ]
# CMD [ "go", "run", "main.go" ]
# CMD [ "./main.go" ]
