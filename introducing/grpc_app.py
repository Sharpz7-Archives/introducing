import logging
from concurrent import futures

import grpc

import introducing.proto.service_pb2 as pb2
import introducing.proto.service_pb2_grpc as pb2_grpc
from introducing import faces, location, text, urls

cache = {}

class Card(pb2_grpc.CardServicer):
    """
    Get Card
    """

    def __init__(self):
        self.personCards = pb2.personCards
        self.personCard = pb2.personCard

    def get_card(self, request, _):
        """
        Gets a card from the server
        """

        cards = self.personCards()

        for _ in range(request.no_of_cards):
            data = get_data()
            card = self.personCard(**data)
            cards.card.append(card)

        return cards


def get_data():
    """#
    Gets all data for a card
    """

    data = {}

    logging.info("UPDATING CACHE")
    urls.update_cache(cache)
    logging.info("FINISHED")

    loc, background = location.get(cache)
    profile_picture = faces.get(cache)
    name = text.get_name()
    title = text.get_title()
    age = text.get_age(profile_picture)
    backstory = text.get_backstory(cache)

    data["profile_picture"] = profile_picture
    data["location"] = loc
    data["background_image"] = background
    data["name"] = name
    data["age"] = age
    data["backstory"] = backstory
    data["title"] = title

    return data


def serve():
    """
    Serve the server
    """

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_CardServicer_to_server(Card(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    print("Running the gRPC server")
    serve()
