#!make

include .env
export $(shell sed 's/=.*//' .env)

# check that env option DONT_DOWNLOAD_STUB is not true
grpc.stubs:
	{ \
	if [ "$$DONT_DOWNLOAD_STUB" != "TRUE" ]; then \
		curl -sSL https://raw.githubusercontent.com/Sharpz7/introducing/main/proto/service.proto > ./IntroClient/Protos/service.proto ;\
	fi ;\
	}

run: grpc.stubs
	cd IntroClient ;\
	dotnet run