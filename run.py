import http.server
import socketserver
import webbrowser
import threading
import os
import time

PORT = 8000
# Ensure the server serves files from the directory where run.py is located
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)
    
    # Hide the standard HTTP logs so the console stays clean
    def log_message(self, format, *args):
        pass

def start_server():
    # Allow port to be reused quickly
    socketserver.TCPServer.allow_reuse_address = True
    try:
        with socketserver.TCPServer(("", PORT), QuietHandler) as httpd:
            print(f"✅ MEDICURE Server running successfully at http://localhost:{PORT}")
            print("Press Ctrl+C to stop the server.")
            httpd.serve_forever()
    except OSError:
        pass # Port might be in use, we'll try to just open the browser anyway

if __name__ == "__main__":
    print("Starting MEDICURE local server...")
    
    # Start the server in a background thread
    server_thread = threading.Thread(target=start_server)
    server_thread.daemon = True
    server_thread.start()

    # Wait a tiny bit for the server to start
    time.sleep(1)

    print("🌐 Opening Medicure in your default web browser...")
    webbrowser.open(f'http://localhost:{PORT}/index.html')

    try:
        # Keep running until the user presses Ctrl+C
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n🛑 Shutting down server. Goodbye!")
