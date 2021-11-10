from flask import Flask, json, send_file, request, make_response, jsonify
import tempfile
from KGG.requestREST import materialise
from KGG.insert_data import insert_data
from KGG.query_data import query_data

app = Flask(__name__)


@app.route('/idf2rdf', methods=["GET", 'POST'])
def post_file():
    if request.method == 'POST':
        uploaded_file = request.files['file'].read()
        subgraph_uri = request.args.get("graph_uri", "")
        temp = tempfile.NamedTemporaryFile() # mode='w+t'
        try:
            temp.write(uploaded_file)
            temp.seek(0)
            response = materialise(temp.name)
            results = insert_data("http://localhost:8890/building/" + subgraph_uri, data=response)

            temp.truncate()
            temp.write(bytes(response, 'utf-8'))
            temp.seek(0)
            #return send_file(temp.name, as_attachment=True)
            return make_response(jsonify({"response": "Graph created"}), 201)
        finally:
            temp.close()

    return "KGG Service"


@app.route("/graphs/<graph_uri>", methods=["GET"])
def get_graph(graph_uri):

    results = query_data("http://localhost:8890/building/" + graph_uri)

    if results == "":
        return make_response(jsonify({"response": "Resource not found"}), 404)

    return results

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
