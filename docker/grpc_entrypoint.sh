#/bin/bash

if [ "$$DONT_DOWNLOAD_STUB" != "TRUE" ]; then \
    curl -sSL https://raw.githubusercontent.com/Sharpz7/introducing/main/proto/service.proto > ./introducing/service.proto
fi; \

poetry run python -m grpc_tools.protoc -I. --python_out=./introducing/proto --grpc_python_out=./introducing/proto --proto_path=./introducing/ service.proto
sed -i 's/import service_pb2/import introducing.proto.service_pb2/g' introducing/proto/service_pb2_grpc.py
echo "# pylint: disable=all" >> introducing/proto/service_pb2.py
echo "# flake8: noqa" >> introducing/proto/service_pb2.py
echo "# pylint: disable=all" >> introducing/proto/service_pb2_grpc.py
echo "# flake8: noqa" >> introducing/proto/service_pb2_grpc.py

poetry run python -m introducing.grpc_app