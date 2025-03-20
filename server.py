from flask import Flask, render_template, jsonify

app = Flask(__name__)

news = [
    {"id": 1, "title": "Новость 1", "content": "Содержимое новости 1"},
    {"id": 2, "title": "Новость 2", "content": "Содержимое новости 2"},
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/news', methods=['GET'])
def get_news():
    return jsonify(news)

if __name__ == '__main__':
    app.run(debug=True)
