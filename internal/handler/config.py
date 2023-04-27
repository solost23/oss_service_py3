class config():
    server = None
    minio_client = None

    def __init__(self, server, minio_client):
        self.server = server
        self.minio_client = minio_client