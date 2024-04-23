from flask import Flask, render_template, request, jsonify
from dill import loads, dumps
import json

popular_books_info = loads(dumps('popular_books_info.pkl'))
book_name= list(jsonify(popular_books_info[0]))
author= list(json(popular_books_info[4]))
votes = list(json(popular_books_info[1]))
ratings = list(json(popular_books_info[2]))
image = list(json(popular_books_info[8]))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', 
                            book_name= book_name, author= author, votes = votes, ratings = ratings, image= image
                            )

if __name__ == '__main__':
    app.run(debug=True)
