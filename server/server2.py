# server2.py
# 1、创建一个套接字 socket(socket.af_inet,socket.sock_stream)
# 2、绑定套接字地址 bind
# 3、开启监听 listen
# 4、等待客户端连接并接收客户端连接 accept
# 5、发送或者接收消息 send -- recv
import socket
import sys

print("start server")
# 创建服务套接字
s_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 获取本地主机名
host = socket.gethostname()
# 选取端口号
port = 9999
# 构建套接字地址
s_addr = (host,port)
# 设置与绑定套接字地址
# 绑定的意思就是设置套接字地址
s_socket.bind(s_addr)
# 开启监听
s_socket.listen(5)
# 处理服务器与客户端通信
while True:
    c_socket,c_addr = s_socket.accept()
    print(c_addr)
    print(c_socket)
    msg = "欢迎来到这里" + "\r\n"
    c_socket.send(msg.encode("utf8"))
    c_socket.close()
