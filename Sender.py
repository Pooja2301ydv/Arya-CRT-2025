import socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip_add="172.20.10.2"
port_num=1234
complete = (ip_add, port_num)
msg=input("What message you want to deliver")
encode_msg=msg.encode('ascii')
s.sendto(encode_msg, complete)