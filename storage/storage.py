import os
import json
from server import Book, BookStore

BOOKS_SCHEME = 'books'
BOOKSTORES_SCHEME = 'bookstores'

class Storage:
    
    storage = {}

    def loadInitialData(self):
        basedir = os.path.abspath(os.path.dirname(__file__))
        file = os.path.join(basedir, 'initialdata.json')

        openfile = open(file)
        content = openfile.read()
        json_data = json.loads(content)
        self.__parseJsonScheme(json_data)
        return

    def getAll(self, schema):
        return self.storage[schema]
    
    def get(self, schema, id):
        for item in self.storage[schema]:
            if str(item.id) == id:
                return [item]

    def add(self, schema, obj):
        self.storage[schema].append(obj)
        return [obj]
    
    def update(self, schema, id, update):
        for item in self.storage[schema]:
            if str(item.id) == id:
                item = update
                return [item]

    def delete(self, schema, id):
        index = -1
        result = False
        for item in self.storage[schema]:
            if str(item.id) == id:
                index = self.storage[schema].index(item)
                break
        if index != -1:
            del self.storage[schema][index]
            result = True
        return result

    def __addStorage(self, schema, data):
        self.storage[schema] = data
        return

    def __parseJsonScheme(self, json_data):
        for schema, data in json_data.items():
            parsed_data = self.__parseSchemeData(data, schema)
            self.__addStorage(schema, parsed_data)

    def __parseSchemeData(self, items, schema):
        parsed_data = []
        for data in items:
            if schema == BOOKS_SCHEME:
                obj = Book(data['title'], data['author'], data['isbn'], data['about'])
                # parsed_data[obj.id] = obj
                parsed_data.append(obj)
            else:
                obj = BookStore(data['name'], data['lat'], data['long'], data['about'])
                # parsed_data[obj.id] = obj
                parsed_data.append(obj)
        return parsed_data
