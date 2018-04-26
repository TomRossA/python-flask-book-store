from flask import request, jsonify
from server import app, db, BookStoreSchema, BookStore

STORAGE_NAME = 'bookstores'
bookstore_schema = BookStoreSchema()
bookstore_schema = BookStoreSchema(many=True)

@app.route('/bookstores', methods=["GET"])
def list_all_stores():
    all_bookstores = db.getAll(STORAGE_NAME)
    result = bookstore_schema.dump(all_bookstores)
    return jsonify(result.data)

@app.route('/bookstores', methods=["POST"])
def create_a_store():
    data = request.get_json()
    obj = BookStore(data['name'], data['lat'], data['long'], data['about'])
    result = db.add(STORAGE_NAME, obj)
    return bookstore_schema.jsonify(result)

@app.route("/bookstores/<storeId>", methods=["GET"])
def read_a_store(storeId):
    bookstore = db.get(STORAGE_NAME, storeId)
    return bookstore_schema.jsonify(bookstore)

@app.route("/bookstores/<storeId>", methods=["PUT"])
def update_a_store(storeId):
    data = request.get_json()
    bookstore = db.get(STORAGE_NAME, storeId)[0]
    bookstore.name = data['name']
    bookstore.lat = data['lat']
    bookstore.long = data['long']
    bookstore.about = data['about']
    result = db.update(STORAGE_NAME, storeId, bookstore)
    return bookstore_schema.jsonify(result)

@app.route("/bookstores/<storeId>", methods=["DELETE"])
def delete_a_store(storeId):
    result = db.delete(STORAGE_NAME, storeId)
    if result:
        return jsonify({ 'id': storeId, 'message': 'Bookstore successfully deleted' })
    else:
        return jsonify({'message': 'Bookstore not found' })