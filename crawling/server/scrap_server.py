from concurrent import futures
import logging
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import grpc

from server import crawling_pb2
from server import crawling_pb2_grpc


class Crawling(crawling_pb2_grpc.CrawlingServicer):

    def Scrap(self, request, context):
        return crawling_pb2.ScrapReply(resultCode=1, message='Hello, %s!' % request.board)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    crawling_pb2_grpc.add_CrawlingServicer_to_server(Crawling(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()