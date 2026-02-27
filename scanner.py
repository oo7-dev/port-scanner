import socket
from concurrent.futures import ThreadPoolExecutor


def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        result = sock.connect_ex((target, port))
        sock.close()

        if result == 0:
            return port
    except:
        pass

    return None


def scan_ports(target, start_port, end_port):
    open_ports = []
    ports = range(start_port, end_port + 1)

    with ThreadPoolExecutor(max_workers=100) as executor:
        results = executor.map(lambda port: scan_port(target, port), ports)

    for result in results:
        if result:
            open_ports.append(result)

    return open_ports