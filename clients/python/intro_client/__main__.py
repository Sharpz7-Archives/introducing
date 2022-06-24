import grpc

import intro_client.proto.service_pb2 as pb2
import intro_client.proto.service_pb2_grpc as pb2_grpc


class fetchCard(object):
    """
    Class for fetching data
    """

    def __init__(self):
        self.channel = grpc.insecure_channel("introducing_grpc_dev:50051")
        self.stub = pb2_grpc.CardStub(self.channel)

    def get_card(self, no_of_cards):
        """
        Gets Card
        """

        request = pb2.request(no_of_cards=no_of_cards)
        response = self.stub.get_card(request)
        return response


if __name__ == "__main__":
    print("Running the gRPC client")
    client = fetchCard()
    print(client.get_card(1))
