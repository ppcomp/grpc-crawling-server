from __future__ import print_function
import logging

import grpc

from grpc_files import crawling_pb2
from grpc_files import crawling_pb2_grpc

def start_scrap(stub, board=None, pages=1):
    scrap_request = crawling_pb2.ScrapRequest(board=board, pages=pages)
    feature = stub.Scrap(scrap_request)
    if feature.resultCode == 0:
        print("Server crawling completed with result code 0.")
    else:
        print(f"Server crawling is not completed with result code {feature.resultCode}.")
        print(f"Cause by {feature.message}")

def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50053') as channel:
        stub = crawling_pb2_grpc.CrawlingStub(channel)
        print("-------------- Scrap --------------")
        start_scrap(stub, "cse", 3)


if __name__ == '__main__':
    logging.basicConfig()
    run()