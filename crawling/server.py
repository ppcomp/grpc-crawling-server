from concurrent import futures
import logging
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import grpc

from grpc_files import crawling_pb2
from grpc_files import crawling_pb2_grpc
from src.tasks import CustomCrawler


class Crawling(crawling_pb2_grpc.CrawlingServicer):

    def Scrap(self, request, context):
        custom_crawler = CustomCrawler()
        res = custom_crawler.crawl(request.board, request.pages)
        return crawling_pb2.ScrapReply(
            resultCode=res["result_code"], 
            message=res["message"],
            output=res["output"]
        )


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    crawling_pb2_grpc.add_CrawlingServicer_to_server(Crawling(), server)
    server.add_insecure_port('[::]:50053')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()