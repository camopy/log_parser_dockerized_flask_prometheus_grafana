# log_parser_dockerized_flask_prometheus_grafana

This is a basic log parser!

Did this while learning the stack:

    - Python
    - Flask
    - MySQL
    - SQL Alchemy
    - Prometheus exporter
    - Golang
    - Prometheus
    - Grafana
    - Docker
    - Docker Compose


For now, it only parses files from a local (from project files) rsync log file.

The parser was made using Python, with Flask framework, and saved to a MySQL database using SQL Alchemy.

I created a Prometheus exporter in Golang to communicate with the flask api and get metrics for Prometheus that will be later displayed in a Grafana dashboard.

Everything is in docker containers, all connected with a docker compose file. So you can get everything running with a single docker-compose up in the terminal. 
