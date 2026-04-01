import http.server
import socketserver
import webbrowser
import threading
import time

PORT = 8000

def start_server():
    handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", PORT), handler) as httpd:
        print(f"Serving at http://localhost:{PORT}")
        httpd.serve_forever()

if __name__ == "__main__":
    # Start the server in a separate thread so it doesn't block the script
    threading.Thread(target=start_server, daemon=True).start()
    
    # Give the server a second to start, then open the browser
    time.sleep(1)
    webbrowser.open(f"http://localhost:{PORT}")
    
    print("Press Ctrl+C to stop the server.")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nShutting down server...")
