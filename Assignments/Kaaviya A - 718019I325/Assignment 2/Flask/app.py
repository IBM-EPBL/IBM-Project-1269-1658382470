import flask 
from flask import request, jsonify
app = flask.Flask(__name__) 

# books dictionary 
Book_Data = [
        {
            "isbn":9781593279509,
            "title":"Eloquent JavaScript, Third Edition",
            "author":"Marijn Haverbeke",
            "published":"2018-12-04T00:00:00.000Z",
            "publisher":"No Starch Press",
            "pages":472,
            "description":"JavaScript lies at the heart of almost every modern web application, from social apps like Twitter to browser-based game frameworks like Phaser and Babylon. Though simple for beginners to pick up and play with, JavaScript is a flexible, complex language that you can use to build full-scale applications.",
            "website":"http://eloquentjavascript.net/"
        },
        {
            "isbn":9781491943533,
            "title":"Practical Modern JavaScript",
            "author":"Nicolás Bevacqua",
            "published":"2017-07-16T00:00:00.000Z",
            "publisher":"O'Reilly Media",
            "pages":334,
            "description":"To get the most out of modern JavaScript, you need learn the latest features of its parent specification, ECMAScript 6 (ES6). This book provisbnes a highly practical look at ES6, without getting lost in the specification or its implementation details.",
            "website":"https://github.com/mjavascript/practical-modern-javascript"
        },
        {
            "isbn":9781593277574,
            "title":"Understanding ECMAScript 6",
            "author":"Nicholas C. Zakas",
            "published":"2016-09-03T00:00:00.000Z",
            "publisher":"No Starch Press",
            "pages":352,
            "description":"ECMAScript 6 represents the biggest update to the core of JavaScript in the history of the language. In Understanding ECMAScript 6, expert developer Nicholas C. Zakas provisbnes a complete guisbne to the object types, syntax, and other exciting changes that ECMAScript 6 brings to JavaScript.",
            "website":"https://leanpub.com/understandinges6/read"
        },
        {
            "isbn":9781449365035,
            "title":"Speaking JavaScript",
            "author":"Axel Rauschmayer",
            "published":"2014-04-08T00:00:00.000Z",
            "publisher":"O'Reilly Media",
            "pages":460,
            "description":"Like it or not, JavaScript is everywhere these days -from browser to server to mobile- and now you, too, need to learn the language or dive deeper than you have. This concise book guisbnes you into and through JavaScript, written by a veteran programmer who once found himself in the same position.",
            "website":"http://speakingjs.com/"
        },
        {
            "isbn":9781449331818,
            "title":"Learning JavaScript Design Patterns",
            "author":"Addy Osmani",
            "published":"2012-08-30T00:00:00.000Z",
            "publisher":"O'Reilly Media",
            "pages":254,
            "description":"With Learning JavaScript Design Patterns, you'll learn how to write beautiful, structured, and maintainable JavaScript by applying classical and modern design patterns to the language. If you want to keep your code efficient, more manageable, and up-to-date with the latest best practices, this book is for you.",
            "website":"http://www.addyosmani.com/resources/essentialjsdesignpatterns/book/"
        },
    ]
#home
@app.route("/")
def home():
    return "Welcome"
#get books
@app.route('/book', methods=['GET'])
def get_books():
    return jsonify(Book_Data)
#Get book by isbn
@app.route("/isbn/<isbn>", methods=['GET'])
def get_book_by_isbn(isbn): 
    for book in Book_Data: 
        if book['isbn'] == int(isbn):
            return jsonify (book) 
    return {}
#add a book to the dictionary
@app.route('/add_book', methods=['POST'])
def add_book():
    book = request.get_json() 
    book['isbn'] = len(Book_Data) + 1 
    Book_Data.append(book) 
    return jsonify(book)
#update details of a particular book
@app.route('/update_book', methods=['PUT']) 
def update_book():
    book = request.get_json() 
    for i, u in enumerate(Book_Data): 
        if u['isbn'] == book['isbn']:
            Book_Data[i] = book 
    return jsonify(Book_Data)

#delete particular book
@app.route('/delete/<isbn>', methods=['DELETE'])
def delete_book(isbn): 
    for book in Book_Data:
        if book['isbn'] == int(isbn):
            Book_Data.remove(book) 
    return jsonify(Book_Data)

if __name__=="__main__":
    app.run(debug=True)