import uuid
from server import ma

class BookStore():
    id = str
    name = str
    lat = str
    long = str
    about = str
    books = list
    
    def __init__(self, name, lat, long, about):
        self.id = uuid.uuid4()
        self.name = name
        self.lat = lat
        self.long = long
        self.about = about
        self.books = []

class BookStoreSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'lat', 'long', 'about', 'books')