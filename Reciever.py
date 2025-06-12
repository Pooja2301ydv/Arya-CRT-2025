import socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip_add="172.20.10.2"
port_num=1234
complete = (ip_add, port_num)
s.bind(complete)
while(True):
    msg=s.recvfrom(1024)
    decode_msg=msg[0].decode('ascii')
    print(decode_msg)