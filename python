import http.server
import socketserver
import os
import cgi

PORT = 8080
UPLOAD_FOLDER = 'uploads'

class FileUploadHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST'}
        )

        uploaded_file = form['file']
        if uploaded_file:
            filename = os.path.join(UPLOAD_FOLDER, uploaded_file.filename)
            with open(filename, 'wb') as f:
                f.write(uploaded_file.file.read())
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'File uploaded successfully')
        else:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b'Bad request - no file uploaded')

if __name__ == '__main__':
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    
    with socketserver.TCPServer(("", PORT), FileUploadHandler) as httpd:
        print(f"Serving at port {PORT}")
        httpd.serve_forever()
