# client2.py
# 1、创建客户端套接字 socket(socket.af_inet,socket.sock_steram)
# 2、选取服务器主机名与端口
# 3、构建服务器套接字地址 (host,port)
# 4、连接服务器地址 connect
# 5、发送与接收消息 send recv
import socket
import sys
print("start clinet")
# 构建客户端套接字
c_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 选取服务器主机名与端口
# 因为服务端与客户端 处于同一机器 且拥有共同ip地址 所以用本机地址代替服务器地址
s_host = socket.gethostname()
s_port = 9999
# 构建服务器套接字地址
s_addr = (s_host,s_port)
# 用客户端套接字连接服务器套接字
c_socket.connect(s_addr)
# 处理服务器与客户端通信
# 1024 为接收小于 1024 字节的数据
msg = c_socket.recv(1024)
c_socket.close()
print(msg.decode("utf8"))