# implementing default values in data classes

from dataclasses import dataclass, field
import random

def price_func():
    return float(random.randrange(20,40))

@dataclass
class Book:
    # you can define default values when attributes are declared
    title: str = "No title"
    author: str = "No Author"
    pages: int = 0
    price: float = field(default_factory=price_func)


b1 = Book()
b2 = Book("War and Peace", "Leo Tolstoy", 1225)
b3 = Book("The Catcher in the Rye", "JD Salinger", 234)

print(b1)
print(b2)
print(b3)

""" 
Book(title='No title', author='No Author', pages=0, price=10.0)
Book(title='War and Peace', author='Leo Tolstoy', pages=1225, price=10.0)        
Book(title='The Catcher in the Rye', author='JD Salinger', pages=234, price=10.0)
"""