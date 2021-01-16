import configparser
import socket
import os

class NetParam(object):
    __HOST = ''
    __POST_ALGORIGHTM = '123457'

    def get_host_ip(self):
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        __HOST = host_ip
    def get_algorithm_post(self,cls):
        return cls.__POST_ALGORIGHTM
    def set_algorithm_post(self, cls, post):
        cls.__POST_ALGORIGHTM = post

class read_config:
    """读取配置文件类"""

    def __init__(self, file_path=None):
        if file_path:
            config_path = file_path

if __name__ == '__main__':
    net_param = NetParam()

    print(net_param.get_host_ip())
    print(net_param.get_algorithm_post())