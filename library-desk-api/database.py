import sqlite3
class Database:
 def __init__(self,path): self.path=path; self.initialize()
 def connect(self):
  c=sqlite3.connect(self.path); c.row_factory=sqlite3.Row; return c
 def initialize(self):
  with self.connect() as c:
   c.execute('CREATE TABLE IF NOT EXISTS books(id INTEGER PRIMARY KEY, title TEXT NOT NULL, author TEXT NOT NULL, total_copies INTEGER NOT NULL CHECK(total_copies>=0), available_copies INTEGER NOT NULL CHECK(available_copies>=0))')
   c.execute('CREATE TABLE IF NOT EXISTS loans(id INTEGER PRIMARY KEY, book_id INTEGER NOT NULL REFERENCES books(id), member_name TEXT NOT NULL, returned INTEGER NOT NULL DEFAULT 0)')
