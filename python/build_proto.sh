#!/usr/bin/env bash
set -euox pipefail

echo "Building protos..."
python3 -m grpc_tools.protoc \
    -I../proto \
    --python_out=./src \
    --grpc_python_out=./src \
    ../proto/message_server.proto
