import socket

def grab_banner(target, port):
    try:
        sock = socket.socket()
        sock.settimeout(2)
        sock.connect((target, port))
        
        # Send basic request (works for HTTP services)
        sock.send(b"HEAD / HTTP/1.0\r\n\r\n")
        banner = sock.recv(1024)
        sock.close()
        
        return banner.decode(errors="ignore").strip()
    except:
        return "No banner available"