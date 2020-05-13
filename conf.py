# This is mainly used to change the uris quickly
ip = '10.86.167.191'
port = ':80'
method = 'http://'

def ip_conf():
    global ip
    return ip

def complete_server_conf():
    global ip
    global port
    global  method
    ret = method+ip+port
    return ret
