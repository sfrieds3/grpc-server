#!/usr/bin/env bash
set -euox pipefail

echo "Building protos..."
protoc --go_out=./proto --go-grpc_out=./proto --proto_path ../proto message_server.proto
