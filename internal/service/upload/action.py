from protopb.gen.py3.protos.oss import oss_pb2 as oss
from internal.service.base import action

class Action(action.Action):
    def __init__(self):
        pass

    def deal(self, request, context):
        """logic"""
        return deal(self, request, context)


def deal(self, request, context):
    return oss.UploadResponse(url=request.folder)
