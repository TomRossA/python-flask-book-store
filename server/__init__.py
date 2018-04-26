from flask import Flask
from flask_cors import CORS
from flask_marshmallow import Marshmallow

app = Flask(__name__)
ma = Marshmallow(app)
CORS(app)

from server.models.book import Book, BookSchema
from server.models.bookstore import BookStore, BookStoreSchema
from storage.storage import Storage

db = Storage()
db.loadInitialData()

import server.endpoints.book
import server.endpoints.bookstore