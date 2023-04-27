import os, sys
sys.path.append(os.getcwd())
sys.path.append(os.getcwd() + '/protopb/gen/py3')

from internal.server.server import run

if __name__ == '__main__':
    run()