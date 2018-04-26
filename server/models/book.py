import uuid
from server import ma

class Book():
    id = str
    title = str
    author = str
    isbn = str
    about = str
    
    def __init__(self, title, author, isbn, about):
        self.id = uuid.uuid4()
        self.title = title
        self.author = author
        self.isbn = isbn
        self.about = about

class BookSchema(ma.Schema):
    class Meta:
        fields = ('id' ,'title', 'author', 'isbn', 'about')