class LibraryService:
 def __init__(self,db): self.db=db
 def list_books(self):
  with self.db.connect() as c: return [dict(r) for r in c.execute("SELECT * FROM books ORDER BY title")]
 def get_book(self,i):
  with self.db.connect() as c:
   r=c.execute("SELECT * FROM books WHERE id=?",(i,)).fetchone(); return dict(r) if r else None
 def add_book(self,d):
  title=str(d.get("title","")).strip(); author=str(d.get("author","")).strip(); n=d.get("copies",1)
  if not title or not author: raise ValueError("title and author are required")
  if type(n) is not int or n<1: raise ValueError("copies must be a positive integer")
  with self.db.connect() as c: cur=c.execute("INSERT INTO books(title,author,total_copies,available_copies) VALUES(?,?,?,?)",(title,author,n,n)); i=cur.lastrowid
  return self.get_book(i)
 def borrow_book(self,d):
  i=d.get("book_id"); member=str(d.get("member_name","")).strip()
  if type(i) is not int or not member: raise ValueError("book_id and member_name are required")
  with self.db.connect() as c:
   b=c.execute("SELECT * FROM books WHERE id=?",(i,)).fetchone()
   if not b: raise LookupError("Book not found")
   if b["available_copies"]<1: raise ValueError("No copies available")
   c.execute("UPDATE books SET available_copies=available_copies-1 WHERE id=?",(i,))
   cur=c.execute("INSERT INTO loans(book_id,member_name) VALUES(?,?)",(i,member)); r=c.execute("SELECT * FROM loans WHERE id=?",(cur.lastrowid,)).fetchone(); return dict(r)
 def list_loans(self):
  with self.db.connect() as c: return [dict(r) for r in c.execute("SELECT * FROM loans ORDER BY id DESC")]
