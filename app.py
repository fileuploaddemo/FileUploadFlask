from flask import Flask, render_template, jsonify, send_from_directory, request
from werkzeug.utils import secure_filename
import os
import uuid
app = Flask(__name__)

UPLOAD_FOLDER='upload'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
basedir = os.path.abspath(os.path.dirname(__file__))
ALLOWED_EXTENSIONS = set(['txt','png','jpg','gif','pdf','epub'])  
IGNORED_FILES = set(['.gitignore'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1] in ALLOWED_EXTENSIONS

def init_dir():
    file_dir=os.path.join(basedir,app.config['UPLOAD_FOLDER'])
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)
    return file_dir

@app.route('/')
def index():
    return render_template('index.html', title='Duokan')

@app.route('/files')
def load():
    file_dir = init_dir()
    files_saved = [f for f in os.listdir(file_dir) if os.path.isfile(os.path.join(file_dir, f)) and f not in IGNORED_FILES ]
    files = []
    number = 0
    for f in files_saved:
        size = os.path.getsize(os.path.join(app.config['UPLOAD_FOLDER'], f))
        number += 1
        files.append({
          "id": number,
          "size": size,
          "name": f,
          "path": ""
        })

    return jsonify(files)    

@app.route('/files/<string:filename>')
def download(filename):
    return send_from_directory(os.path.join(app.config['UPLOAD_FOLDER']), filename=filename, as_attachment=True)

@app.route('/files', methods=['POST'])
def upload():
    file_dir = init_dir()
    file = request.files['newfile']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(file_dir, filename))
        return jsonify({"result":"OK"})
    else:
        return jsonify({"result":"error"})

@app.route("/files/<string:filename>", methods=['DELETE'])
def delete(filename):
    file_dir = init_dir()
    file_path = os.path.join(file_dir, filename)

    if os.path.exists(file_path):
        try:
            os.remove(file_path)            
            return jsonify({"result":"OK"})
        except:
            return jsonify({"result":"error"})




if __name__ == '__main__':
    app.run(debug=True)