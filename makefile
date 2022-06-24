all: SHELL:=/bin/bash

grpc.stubs:
	{ \
	curl -sSL https://github.com/Sharpz7/introducing/blob/main/proto/service.proto > ./introducing/service.proto ;\
	poetry run python -m grpc_tools.protoc -I. --python_out=./introducing/proto --grpc_python_out=./introducing/proto --proto_path=./introducing/ service.proto ;\
	sed -i 's/import service_pb2/import introducing.proto.service_pb2/g' introducing/proto/service_pb2_grpc.py ;\
	echo "# pylint: disable=all" >> introducing/proto/service_pb2.py ;\
	echo "# flake8: noqa" >> introducing/proto/service_pb2.py ;\
	echo "# pylint: disable=all" >> introducing/proto/service_pb2_grpc.py ;\
	echo "# flake8: noqa" >> introducing/proto/service_pb2_grpc.py ;\
	}


grpc: grpc.stubs
	poetry run python -m introducing.grpc_app