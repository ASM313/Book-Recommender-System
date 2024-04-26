from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np

df = pd.read_pickle('models/popular_books_info.pkl')
pt = pd.read_pickle('models/pt.pkl')
similiarity = pd.read_pickle('models/similiarity.pkl')


book_name = list(df['Book-Title'])
author = list(df['Book-Author'])
votes = list(df['No. of Votes'])
rating = list(df['Avg votes'])
image = list(df['Image-URL-M'])

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', 
                            book_name=book_name, author=author, votes=votes, rating=rating,image=image
                            )

@app.route('/recommend', methods=['GET', 'POST'])
def recommend():
    user_input = request.form.get('user_input')

    rec_books = []
    idx=np.where(pt.index==user_input)[0][0]
    similiar_books = sorted(list(enumerate(similiarity[idx])), key= lambda x:x[1], reverse=True)[1:6]
    
    for book in similiar_books:
        # item = []
        # temp_df = df[df['Book-Title'] == pt.index[book[0]]]
        # item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        # item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        # item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))
        
        rec_books.append(pt.index[book[0]])
        print(pt.index[book[0]])

    return render_template('index.html', rec_books=rec_books)

if __name__ == '__main__':
    app.run(debug=True)
