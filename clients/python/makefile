#!make

include .env
export $(shell sed 's/=.*//' .env)

# check that env option DONT_DOWNLOAD_STUB is not true
grpc.stubs:
	{ \
	if [ "$$DONT_DOWNLOAD_STUB" != "TRUE" ]; then \
		curl -sSL https://raw.githubusercontent.com/Sharpz7/introducing/main/proto/service.proto > ./intro_client/service.proto ;\
	fi ;\
	poetry run python -m grpc_tools.protoc -I. --python_out=./intro_client/proto --grpc_python_out=./intro_client/proto --proto_path=./intro_client/ service.proto ;\
	sed -i 's/import service_pb2/import intro_client.proto.service_pb2/g' intro_client/proto/service_pb2_grpc.py ;\
	echo "# pylint: disable=all" >> intro_client/proto/service_pb2.py ;\
	echo "# flake8: noqa" >> intro_client/proto/service_pb2.py ;\
	echo "# pylint: disable=all" >> intro_client/proto/service_pb2_grpc.py ;\
	echo "# flake8: noqa" >> intro_client/proto/service_pb2_grpc.py ;\
	}

run: grpc.stubs
	poetry run python -m intro_client