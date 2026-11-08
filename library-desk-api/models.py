from dataclasses import dataclass
@dataclass
class Book:
 id:int; title:str; author:str; total_copies:int; available_copies:int
@dataclass
class Loan:
 id:int; book_id:int; member_name:str; returned:bool
