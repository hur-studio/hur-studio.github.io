#!/usr/bin/env python3
"""
HUURS STUDIO - Free 11-Surah Taster Sanctuary Server
====================================================
Lightweight server for running and installing the Free Taster Package
to mobile devices (Android / iOS) via PWA.
"""

import os
import sys
import socket
import argparse
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler

PACKAGE_DIR = os.path.dirname(os.path.abspath(__file__))

class TasterHTTPRequestHandler(SimpleHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=PACKAGE_DIR, **kwargs)

    extensions_map = SimpleHTTPRequestHandler.extensions_map.copy()
    extensions_map.update({
        '.json': 'application/json',
        '.webmanifest': 'application/manifest+json',
        '.js': 'application/javascript',
        '.mjs': 'application/javascript',
        '.wasm': 'application/wasm',
        '.svg': 'image/svg+xml',
        '.png': 'image/png',
        '.webp': 'image/webp',
    })

    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, HEAD, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Range, Content-Type, Accept, Origin')
        
        if self.path.endswith('sw.js'):
            self.send_header('Service-Worker-Allowed', '/')
            self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
            self.send_header('Content-Type', 'application/javascript; charset=utf-8')
        elif self.path.endswith('manifest.json'):
            self.send_header('Content-Type', 'application/manifest+json; charset=utf-8')
        elif self.path.endswith('.html'):
            self.send_header('Cache-Control', 'no-cache')
            
        super().end_headers()

def get_lan_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(0.5)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"

def run(port=8183):
    lan_ip = get_lan_ip()
    server_address = ('0.0.0.0', port)
    
    os.chdir(PACKAGE_DIR)
    httpd = ThreadingHTTPServer(server_address, TasterHTTPRequestHandler)
    
    print("=" * 72)
    print("    HUURS STUDIO — FREE 11-SURAH TASTER SANCTUARY SERVER")
    print("=" * 72)
    print(f"Directory : {PACKAGE_DIR}")
    print(f"Status    : ACTIVE & LISTENING on port {port}")
    print("-" * 72)
    print(f"Localhost Access        : http://localhost:{port}/")
    print(f"Android / Mobile (Wi-Fi): http://{lan_ip}:{port}/")
    print("-" * 72)
    print("📱 HOW TO INSTALL ON ANDROID:")
    print(f"  1. Connect your Android device to the same Wi-Fi network.")
    print(f"  2. Open Google Chrome and visit: http://{lan_ip}:{port}/")
    print(f"  3. Tap Chrome's menu (⋮) -> select 'Add to Home screen' / 'Install App'.")
    print(f"  4. The 11-Surah Free Taster Sanctuary will launch full-screen and offline!")
    print("=" * 72)
    sys.stdout.flush()
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server.")
        httpd.server_close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Free 11-Surah Taster Sanctuary Server")
    parser.add_argument("--port", type=int, default=8183, help="Port to bind (default: 8183)")
    args = parser.parse_args()
    run(port=args.port)
