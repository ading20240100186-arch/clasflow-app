import os
import socket
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler

PORT = 8000
HOST = "0.0.0.0"
ROOT = os.path.dirname(os.path.abspath(__file__))


def get_local_ip():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            sock.connect(("8.8.8.8", 80))
            return sock.getsockname()[0]
    except Exception:
        return "127.0.0.1"


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT, **kwargs)


if __name__ == "__main__":
    ip = get_local_ip()
    print("=====================================")
    print("Server catatan pengeluaran sedang berjalan")
    print(f"URL lokal: http://localhost:{PORT}")
    print(f"URL dari HP: http://{ip}:{PORT}")
    print("Akses dari HP menggunakan Wi-Fi yang sama")
    print("Tekan Ctrl+C untuk berhenti")
    print("=====================================")

    try:
        server = ThreadingHTTPServer((HOST, PORT), Handler)
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer dihentikan.")
    finally:
        if 'server' in locals():
            server.server_close()
