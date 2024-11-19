from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Dummy data to simulate a database
data = [
    {"id": 1, "name": "Apple"},
    {"id": 2, "name": "Banana"},
    {"id": 3, "name": "Cherry"},
    {"id": 4, "name": "Date"},
    {"id": 5, "name": "Elderberry"},
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '').lower()
    if not query:
        return jsonify([])  # Return an empty list if no query is provided
    results = [item for item in data if query in item['name'].lower()]
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
