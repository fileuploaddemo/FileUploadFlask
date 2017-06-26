from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title='Duokan')

@app.route('/files')
def load():
    files = [
        {
          "id": "1",
          "size": 100,
          "name": "python",
          "path": "/books/python"
        },
        {
          "id": "2",
          "size": 200,
          "name": "golang",
          "path": "/books/golang"
        }
    ]
    return jsonify(files)

@app.route('/files/<name>')
def download(name):
    return "todo"

@app.route('/files', methods=['POST'])
def upload():
    return "todo"

@app.route('/files/<name>', methods=['DELETE'])
def delete(name):
    return "todo"




if __name__ == '__main__':
    app.run(debug=True)