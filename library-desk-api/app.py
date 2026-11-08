from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from urllib.parse import urlparse
from database import Database
from library_service import LibraryService
service = LibraryService(Database("library.db"))
class Handler(BaseHTTPRequestHandler):
 def send_json(self, code, data):
  body=json.dumps(data).encode(); self.send_response(code); self.send_header("Content-Type","application/json"); self.send_header("Content-Length",str(len(body))); self.end_headers(); self.wfile.write(body)
 def do_GET(self):
  path=urlparse(self.path).path
  if path=="/books": return self.send_json(200,service.list_books())
  if path=="/loans": return self.send_json(200,service.list_loans())
  if path.startswith("/books/"):
   try: item=service.get_book(int(path.rsplit("/",1)[1])); return self.send_json(200 if item else 404,item or {"error":"Book not found"})
   except ValueError: return self.send_json(400,{"error":"Invalid book id"})
  return self.send_json(404,{"error":"Route not found"})
 def do_POST(self):
  try: data=json.loads(self.rfile.read(int(self.headers.get("Content-Length","0"))) or b"{}")
  except (ValueError,json.JSONDecodeError): return self.send_json(400,{"error":"Invalid JSON"})
  try:
   if urlparse(self.path).path=="/books": return self.send_json(201,service.add_book(data))
   if urlparse(self.path).path=="/loans": return self.send_json(201,service.borrow_book(data))
   return self.send_json(404,{"error":"Route not found"})
  except LookupError as e: return self.send_json(404,{"error":str(e)})
  except ValueError as e: return self.send_json(400,{"error":str(e)})
if __name__=="__main__": HTTPServer(("127.0.0.1",8000),Handler).serve_forever()
