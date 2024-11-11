"""
如何唯一标识一个进程?
网络层的“ip地址”可以唯一标识网络中的主机，而传输层的“协议+端口”可以唯一标识主机中的应用程序（进程）, 三元组（ip地址，协议，端口）就可以标识网络的进程了
协议族决定了socket的地址类型，在通信中必须采用对应的地址，如AF_INET决定了要用ipv4地址（32位的）与端口号（16位的）的组合
赋值一个地址，就必须调用bind()函数，否则就当调用connect()、listen()时系统会自动随机分配一个端口。
domain: 协议域(AF_INET: ipv4地址， AF_INET6：ipv6)
type: socket类型
通常服务器在启动的时候都会绑定一个众所周知的地址（如ip地址+端口号），用于提供服务;
客户就可以通过它来接连服务器；而客户端就不用指定，有系统自动分配一个端口号和自身的ip地址组合。
这就是为什么通常服务器端在listen之前会调用bind()，而客户端就不会调用，而是在connect()时由系统随机生成一个。
TCP服务器端依次调用socket()、bind()、listen()之后，就会监听指定的socket地址了。TCP客户端依次调用socket()、connect()之后就想TCP服务器发送了一个连接请求。TCP服务器监听到这个请求之后，就会调用accept()函数取接收请求，这样连接就建立好了。之后就可以开始网络I/O操作了，即类同于普通文件的读写I/O操作。
"""


"""
tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    


tcp_server.close()   



TCP客户端
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.connect(("127.0.0.1", 6001))    # ip, post        ip = client.getsockname()[0]
client.send().encode()
client.recv(1024).decode('utf-8')
client.close()

# 客户端
import socket

host_post = ("127.0.0.1", 7000)     # (socket.gethostname(), 7000)
# 创建 TCP客户端 套接字
tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    # 连接服务器
    tcp_client.connect(host_post)
    print("正在连接tcp服务器...")
except:
    print("not found 404")

while True:
    # 发送数据
    data = input("client: ")
    if data == "bye":
        break
    print(data)
    tcp_client.send(data.encode())  # 编码成二进制发送

    # 接收数据
    res = tcp_client.recv(1024)
    print(f"server: {res.decode('utf-8')}")     # 转码成utf-8编码
tcp_client.close()







# 服务端
import socket

ip = "127.0.0.1"
post = 5001
buffer_size = 1024                     # 文件读写缓存区

tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Tcp
tcp_server.bind((ip, post))            # ip地址和post端口号
tcp_server.listen(6)                   # 最大监听数

conn, addr = tcp_server.accept()       # 接受客户端连接

while True:
    # 接收数据
    ret = conn.recv(buffer_size）
    if ret = b'bye':
        conn.send(b'bye')
        break
    print(f"client: {res.decode('utf-8')}")
    
    # 发送数据
    data = "The server has received"
    conn.send(data.encode())
conn.close()
tcp_server.close()


# 文件读写缓存区
BUFFER_SIZE = 4096
# 传输数据分隔符
SEPARATOR = "<SEPARATOR>"

received = client_socket.recv(BUFFER_SIZE).decode()

# 获取文件名称
filename, file_size = received.split(SEPARATOR)
filename = os.path.basename(filename)
file_size = int(file_size)


progress = tqdm.tqdm(range(file_size), f"接收{filename}", unit="B", unit_divisor=1024, unit_scale=True)
with open(filename, "wb") as f:
    for _ in progress:
        # 从客户端读取数据
        bytes_read = client_socket.recv(BUFFER_SIZE)
        # 如果没有数据传输内容
        if not bytes_read:
            break
        # 读取写入
        f.write(bytes_read)
        # 更新进度条
        progress.update(len(bytes_read))

传递信号
sigUpdateSpeed = pyqtSignal(dict)  # 更新进度速度
self.sigUpdateSpeed.connect(self.sigUpdateSpeedDo)
def sigUpdateSpeedDo(self, datas):
    self.speedShow.setText(datas["speed"])
    self.progressShow.setText(datas["progress"])
    self.progressLabel2.resize(datas["progressNum"], 11)
    self.progressShow.move(datas["progressNum"] + 5, 167)
    self.nowFilesShow.setText(datas["path"])

self.sigUpdateSpeed.emit({
    "speed": self.convert(speed * 2) + "/s",
    "progress": str(pronum) + "%",
    "progressNum": int(450 * pronum / 100),
    "path": i["localpath"]
})


文件字节大小转换
# 总字节转换为大小
def convert(self, bit):
    try:
        # B
        if bit < 1024:
            return str(bit) + "B"
        # KB
        elif 1024 <= bit < 2 ** 20:
            return str('%.2f' % (bit / (2 ** 10))) + "KB"
        # MB
        elif 2 ** 20 <= bit < 2 ** 30:
            return str('%.2f' % (bit / (2 ** 20))) + "MB"
        # GB
        elif 2 ** 30 <= bit < 2 ** 40:
            return str('%.2f' % (bit / (2 ** 30))) + "GB"
        # TB
        elif 2 ** 40 <= bit < 2 ** 50:
            return str('%.2f' % (bit / (2 ** 40))) + "TB"
        else:
            return "未知"
    except:
        return "未知"


gc.collect()  # 主动释放内存

"""