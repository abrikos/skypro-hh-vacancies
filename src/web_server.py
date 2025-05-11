import pathlib
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):


    def do_GET(self):
        url = urlparse(self.path)

        self.send_response(200)
        if url.path in ('/', '/index.html'):
            query_components = parse_qs(url.query)
            page_address = query_components.get('page') or ['home']
            self.send_header("Content-type", "text/html")
            self.end_headers()
            with open("static/index.html", "r") as f:
                template = f.read()
                page_content =""
                with open(f"static/{page_address[0]}.html", "r") as f:
                    page_content = f.read()
                    self.wfile.write(bytes(template.replace("{%page%}", page_content), "utf-8"))

        if url.path.find('static')>=0:
            suffix = pathlib.Path(self.path).suffix
            self.send_header("Content-type", f"text/{suffix[1:]}")
            self.end_headers()

            with open(f".{self.path}", "r") as f:
                self.wfile.write(bytes(f.read(), "utf-8"))

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")