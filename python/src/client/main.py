import grpc

from proto.message_server_pb2 import MessageRequest
from proto.message_server_pb2_grpc import MessageServerStub

channel = grpc.insecure_channel("localhost:50051")
stub = MessageServerStub(channel)


def main():
    print("Hello from client!")
    resp = stub.GetMessage(MessageRequest(name="hello"))

    print(resp)


if __name__ == "__main__":
    main()
