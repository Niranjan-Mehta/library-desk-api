import tempfile,unittest
from pathlib import Path
from database import Database
from library_service import LibraryService
class Tests(unittest.TestCase):
 def setUp(self):
  self.tmp=tempfile.TemporaryDirectory(); self.s=LibraryService(Database(str(Path(self.tmp.name)/"t.db")))
 def tearDown(self): self.tmp.cleanup()
 def test_add(self): self.assertEqual(self.s.add_book({"title":"T","author":"A","copies":2})["available_copies"],2)
 def test_borrow(self):
  b=self.s.add_book({"title":"T","author":"A","copies":1}); self.s.borrow_book({"book_id":b["id"],"member_name":"A"}); self.assertEqual(self.s.get_book(b["id"])["available_copies"],0)
 def test_no_stock(self):
  b=self.s.add_book({"title":"T","author":"A","copies":1}); self.s.borrow_book({"book_id":b["id"],"member_name":"A"})
  with self.assertRaises(ValueError): self.s.borrow_book({"book_id":b["id"],"member_name":"B"})
if __name__=="__main__": unittest.main()
