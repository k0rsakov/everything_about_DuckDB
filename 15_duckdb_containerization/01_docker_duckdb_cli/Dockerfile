FROM debian:bookworm-slim

RUN apt-get update && \
    apt-get install -y curl unzip && \
    rm -rf /var/lib/apt/lists/*

RUN curl --fail --location --progress-bar \
    --output duckdb_cli-linux-arm64.zip \
    https://github.com/duckdb/duckdb/releases/download/v1.5.1/duckdb_cli-linux-arm64.zip && \
    unzip duckdb_cli-linux-arm64.zip && \
    mv duckdb /usr/local/bin/duckdb && \
    chmod +x /usr/local/bin/duckdb && \
    rm duckdb_cli-linux-arm64.zip

WORKDIR /usr/src/app

ENTRYPOINT ["duckdb"]