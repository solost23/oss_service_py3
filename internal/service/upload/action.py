import io

from datetime import timedelta

from protopb.gen.py3.oss import oss_pb2 as oss
from internal.service.base import action


class Action(action.Action):
    def __init__(self, context):
        self.context = context

    def deal(self, request, context):
        """logic"""
        return deal(self, request, context)


def deal(self, request, context):
    # 判断参数是否正常

    mc = self.get_minio()
    # 1.检查桶是否存在，不存在则创建
    # 2.创建文件，返回文件url
    try:
        if not mc.bucket_exists(bucket_name=request.folder):
            mc.make_bucket(request.folder)
    except Exception as e:
        context.set_details(e)

    try:
        obj = io.BytesIO(request.data)
        mc.put_object(request.folder, request.key, obj, len(request.data), content_type=f'application/{request.uploadType}')
    except Exception as e:
        context.set_details(e)

    return oss.UploadResponse(url=mc.presigned_get_object(request.folder, request.key, expires=timedelta(days=7)), key=request.key)
