from flask import Flask, json, jsonify, make_response, request

from lib.author import Author
from lib.book import Book
from lib.bought import Bought
from lib.cabang import Cabang
from lib.customer import Customer
from lib.publisher import Publisher
from lib.revenue import Revenue
from lib.wrote import Wrote

app = Flask(__name__)

@app.route('/books', methods=['GET'])
def books():
    if request.method == 'GET':
        data = Book.get_books()
        res = jsonify(data)
        
        return res

@app.route('/books/<int:id>', methods=['GET', 'POST'])
# request API curl -X GET http://localhost:5000/books/7 -i
def book(id):
    if request.method == 'GET':
        return Book.get_book(id)
    
    # curl -X POST -H "Content-Type:application/json" -d '{"store":1,"book_number":32,"book_name":"tutorial ternak ikan","publication_year":2022,"pages":45,"pname":"Penerbit Erlangga","quantity":1,"price":30000}' http://127.0.0.1:5000/books/7 -i
    if request.method == 'POST':
        try:
            data = request.get_json()
            
            
            req = {
                "store": data.get('store'),
                "book_number": data.get('book_number'),
                "book_name": data.get('book_name'),
                "publication_year": data.get('publication_year'),
                "pages": data.get('pages'),
                "pname": data.get('pname'),
                "quantity": data.get('quantity'),
                "price": data.get('price'),
            }
            
            print(req)
            return 'success'
        except Exception as err:
            print(err)
            


@app.route('/authors', methods=['GET'])
def authors():
    if request.method == 'GET':
        return Author.get_authors()

@app.route('/bought', methods=['GET'])
def bought():
    if request.method == 'GET':
        return Bought.get_bought()
    
@app.route('/cabang', methods=['GET'])
def cabang():
    if request.method == 'GET':
        return Cabang.get_cabang()
    
@app.route('/customer', methods=['GET'])
def customer():
    if request.method == 'GET':
        return Customer.get_customer()
    
@app.route('/publisher', methods=['GET'])
def publisher():
    if request.method == 'GET':
        return Publisher.get_publisher()
    
@app.route('/revenue', methods=['GET'])
def revenue():
    if request.method == 'GET':
        return Revenue.get_revenue()
    
@app.route('/wrote', methods=['GET'])
def wrote():
    if request.method == 'GET':
        return Wrote.get_wrote()

if __name__ == '__main__':
    app.run()