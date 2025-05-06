from concurrent import futures
from typing import override

import grpc

from proto import message_server_pb2, message_server_pb2_grpc


class MessageServer(message_server_pb2_grpc.MessageServerServicer):
    @override
    def GetMessage(self, request, context):
        print(f"received request: {request}")
        return message_server_pb2.Message(name=request.name, message="Received!")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    message_server_pb2_grpc.add_MessageServerServicer_to_server(MessageServer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
