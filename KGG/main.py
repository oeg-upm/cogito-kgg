from typing_extensions import final
from flask import Flask, send_file, request
import tempfile
from requestREST import materialise

app = Flask(__name__)


@app.route('/idf2rdf', methods=['POST'])
def post_file():
    if request.method == 'POST':
        uploaded_file = request.files['file'].read()
        temp = tempfile.NamedTemporaryFile() # mode='w+t'
        try:
            temp.write(uploaded_file)
            temp.seek(0)
            response = materialise(temp.name)
            temp.flush()
            temp.write(bytes(response, 'utf-8'))
            temp.seek(0)
            return send_file(temp.name, as_attachment=True)
        finally:
            temp.close()


if __name__ == '__main__':
    app.run(debug=True)
