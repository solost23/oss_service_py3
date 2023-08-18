from protopb.gen.py3.oss import oss_pb2_grpc as oss_grpc
from internal.service import service


def init(config):
    """
    注册服务
    :return:
    """
    oss_grpc.add_OSSServiceServicer_to_server(service.OSSService(config.minio_client), config.server)