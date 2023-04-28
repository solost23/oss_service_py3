class Action:
    context = None
    mysql = None
    minio_client = None

    def set_context(self, context):
        self.context = context

    def get_context(self):
        return self.context

    def set_mysql(self, mysql):
        self.mysql = mysql

    def get_mysql(self):
        return self.mysql

    def set_minio(self, minio):
        self.minio_client = minio

    def get_minio(self):
        return self.minio_client