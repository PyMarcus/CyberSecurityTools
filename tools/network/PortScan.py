import socket
import sys
from datetime import datetime
import threading
from typing import Callable, Any


print("[*]Please, wait...")


def timeToScan(function) -> Callable[[tuple[Any, ...]], None]:
    def wrapper(*args) -> None:
        t1: datetime = datetime.now()
        function(args[0], args[1], args[2])
        print(f"[*] Time {datetime.now() - t1}")
    return wrapper


def threadToScan(function) -> Callable[[tuple[Any, ...]], None]:
    def inner(*args) -> None:
        th = threading.Thread(target=function, args=(args[0], args[1], args[2]))
        th.start()
    return inner


@threadToScan
@timeToScan
def scanPort(target: str, init: int, end: int) -> None:
    """
    target: host domain or ip addres
    :param init:
    :param end:
    :param target:
    :return:
    """
    for port in range(init, end):
        try:
            sockt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            response = sockt.connect_ex((target, port))
            if response == 0:
                print(f"[*]Port {port}: OPEN")
        except KeyboardInterrupt:
            print("[*]bye")
            sys.exit(0)
        except socket.gaierror:
            print("[*]hostname unresolved")
        except socket.error:
            print("[*]couldn´t connect to server")

if __name__ == '__main__':
    scanPort("www.vivaolinux.com.br", 0, 400)
    scanPort("www.vivaolinux.com.br", 400, 800)
    scanPort("www.vivaolinux.com.br", 800, 1200)

