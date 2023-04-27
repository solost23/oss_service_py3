import grpc
import consul
import time

from concurrent import futures

from internal.handler import handle
from internal.handler import config
from pkg.helper import internal

SERVERNAME = 'oss_service'

def run():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10), options=[('grpc.max_receive_message_length', 100 * 1024 * 1024)])
    # oss.add_OssServicer_to_server(OssService(), server)
    # TODO: 后续考虑链接minio
    handle.init(config.config(server, None))

    ip = internal.get_internal_ip()
    port = internal.get_free_port()

    server.add_insecure_port(f'{ip}:{port}')
    register(SERVERNAME, ip, port)
    server.start()
    server.wait_for_termination()
    try:
        while True:
            time.sleep(186400)
    except:
        unregister(SERVERNAME, ip, port)
        server.stop(0)


def register(name, ip, port):
    c = consul.Consul()
    check = consul.Check.tcp(ip, port, "10s")
    c.agent.service.register(name, f'{name}-{ip}-{port}', address=ip, port=port, check=check)
    print("oss register success...")


def unregister(name, ip, port):
    c = consul.Consul()
    c.agent.service.deregister(f'{name}-{ip}-{port}')
    print("oss exited...")