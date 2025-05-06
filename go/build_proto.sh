#!/usr/bin/env bash
set -euox pipefail

echo "Building protos..."
protoc \
  --go_out=./proto \
  --go-grpc_out=./proto \
  --go_opt=paths=source_relative \
  --go-grpc_opt=paths=source_relative \
  --proto_path=../proto \
  message_server.proto
