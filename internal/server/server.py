import grpc
import consul
from minio import Minio
import time

from concurrent import futures

from internal.handler import handle
from internal.handler import config
from pkg.helper import internal

class Server:
    config = None

    def __init__(self, config):
        self.config = config

    def run(self):
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10),
                             options=[('grpc.max_receive_message_length', 100 * 1024 * 1024)])
        # oss.add_OssServicer_to_server(OssService(), server)
        # TODO: 后续考虑链接minio
        mc = Minio(self.config.get('minio').get('end_point'),
                   access_key=self.config.get('minio').get('access_key_id'),
                   secret_key=self.config.get('minio').get('secret_access_key'),
                   secure=self.config.get('minio').get('user_ssl'))
        handle.init(config.config(server, mc))

        ip = internal.get_internal_ip()
        port = internal.get_free_port()

        server.add_insecure_port(f'{ip}:{port}')

        c = consul.Consul(host=self.config.get('consul').get('host'), port=self.config.get('consul').get('port'))
        self.register(c, self.config.get('name'), ip, port)

        server.start()
        server.wait_for_termination()
        try:
            while True:
                time.sleep(186400)
        except:
            self.unregister(c, self.config.get('name'), ip, port)
            server.stop(0)

    def register(self, c, name, ip, port):
        check = consul.Check.tcp(ip, port, "10s")
        c.agent.service.register(name, f'{name}-{ip}-{port}', address=ip, port=port, check=check)
        print("oss register success...")

    def unregister(self, c, name, ip, port):
        c.agent.service.deregister(f'{name}-{ip}-{port}')
        print("oss exited...")



