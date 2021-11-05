from flask import Flask, json, send_file, request, make_response, jsonify
import tempfile
from KGG.requestREST import materialise
from KGG.insert_data import insert_data

app = Flask(__name__)


@app.route('/idf2rdf', methods=["GET", 'POST'])
def post_file():
    if request.method == 'POST':
        uploaded_file = request.files['file'].read()
        temp = tempfile.NamedTemporaryFile() # mode='w+t'
        try:
            temp.write(uploaded_file)
            temp.seek(0)
            response = materialise(temp.name)
            results = insert_data("http://localhost:8890/cogito", data=response)

            temp.truncate()
            temp.write(bytes(response, 'utf-8'))
            temp.seek(0)
            #return send_file(temp.name, as_attachment=True)
            return make_response(jsonify({"response": "Graph created"}), 201)
        finally:
            temp.close()

    return "KGG Service"

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
