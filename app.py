from flask import Flask, jsonify, request
from yake import KeywordExtractor
import pandas as pd


kw_extractor = KeywordExtractor(lan="en", n=1, top=5)
app = Flask(__name__)


df = pd.concat(
    map(pd.read_csv, ['reviews-13495-13500.csv', 'reviews-13500-13537.csv']), ignore_index=True)
# CORS(app)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/trending_keywords/<int:appid>')
def trending_keywords(appid):

    df3 = df[(df['appid'] == appid)]
    x = df3.shape[0]
    arr = []
    for i in range(1, 100):
        a = kw_extractor.extract_keywords(text=df3['review'].values[i])
        arr = arr + a
    x = arr.sort(key=lambda x: x[1])
    print(x)
    return jsonify({'Trending keywords': arr})


if __name__ == "__main__":
    app.run()
