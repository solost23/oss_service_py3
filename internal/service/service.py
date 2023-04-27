from protopb.gen.py3.protos.oss import oss_pb2_grpc as oss_grpc
from protopb.gen.py3.protos.oss import oss_pb2 as oss

from internal.service.upload import action

class OSSService(oss_grpc.OssServicer):
    minio_client = None

    def __init__(self, minio_client):
        self.minio_client = minio_client

    def Upload(self, request, context):
        return upload(self, request, context)


# upload
def upload(self, request, context):
    a = action.Action()
    setattr(a, 'minio_client', self.minio_client)
    return a.deal(request, context)