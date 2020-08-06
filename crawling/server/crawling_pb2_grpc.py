# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import crawling_pb2 as crawling__pb2


class CrawlingStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Scrap = channel.unary_unary(
                '/crawling.Crawling/Scrap',
                request_serializer=crawling__pb2.ScrapRequest.SerializeToString,
                response_deserializer=crawling__pb2.ScrapReply.FromString,
                )


class CrawlingServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Scrap(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CrawlingServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Scrap': grpc.unary_unary_rpc_method_handler(
                    servicer.Scrap,
                    request_deserializer=crawling__pb2.ScrapRequest.FromString,
                    response_serializer=crawling__pb2.ScrapReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'crawling.Crawling', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Crawling(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Scrap(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/crawling.Crawling/Scrap',
            crawling__pb2.ScrapRequest.SerializeToString,
            crawling__pb2.ScrapReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
