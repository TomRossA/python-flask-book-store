from flask import request, jsonify
from server import app, db, BookSchema, Book

STORAGE_NAME = 'books'
book_schema = BookSchema()
book_schema = BookSchema(many=True)

@app.route('/books', methods=["GET"])
def list_all_books():
    all_books = db.getAll(STORAGE_NAME)
    result = book_schema.dump(all_books)
    return jsonify(result.data)

@app.route('/books', methods=["POST"])
def create_a_book():
    data = request.get_json()
    obj = Book(data['title'], data['author'], data['isbn'], data['about'])
    result = db.add(STORAGE_NAME, obj)
    return book_schema.jsonify(result)

@app.route("/books/<bookId>", methods=["GET"])
def read_a_book(bookId):
    book = db.get(STORAGE_NAME, bookId)
    return book_schema.jsonify(book)

@app.route("/books/<bookId>", methods=["PUT"])
def update_a_book(bookId):
    data = request.get_json()
    book = db.get(STORAGE_NAME, bookId)[0]
    book.title = data['title']
    book.author = data['author']
    book.isbn = data['isbn']
    book.about = data['about']
    result = db.update(STORAGE_NAME, bookId, book)
    return book_schema.jsonify(result)

@app.route("/books/<bookId>", methods=["DELETE"])
def delete_a_book(bookId):
    result = db.delete(STORAGE_NAME, bookId)
    if result:
        return jsonify({ 'id': bookId, 'message': 'Book successfully deleted' })
    else:
        return jsonify({'message': 'Book not found' })