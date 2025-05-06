package main

import (
	"context"
	"fmt"
	pb "grpc-server/go/proto"
	"log"
	"net"

	"google.golang.org/grpc"
	"google.golang.org/protobuf/proto"
)

type messageServer struct {
	pb.UnimplementedMessageServerServer
}

func (s *messageServer) GetMessage(_ context.Context, message *pb.MessageRequest) (*pb.Message, error) {
	log.Printf("Received message: %s", message)
	return &pb.Message{Name: message.Name, Message: proto.String("Received")}, nil
}

func newServer() *messageServer {
	s := &messageServer{}
	return s
}

func main() {
	port := 50051
	lis, err := net.Listen("tcp", fmt.Sprintf("localhost:%d", port))
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}
	var opts []grpc.ServerOption
	grpcServer := grpc.NewServer(opts...)
	pb.RegisterMessageServerServer(grpcServer, newServer())
	grpcServer.Serve(lis)
}
