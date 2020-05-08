# This is mainly used to change the uris quickly
ip = '127.0.0.1'
port = ':8080'
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
