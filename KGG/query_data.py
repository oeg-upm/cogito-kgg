from SPARQLWrapper import SPARQLWrapper, JSON, N3, POST, DIGEST

def query_data(graph_uri):

    query = "SELECT ?s ?p ?o FROM <{}> ".format(graph_uri) + "WHERE {?s ?p ?o}"
    print(query)

    sparql = SPARQLWrapper("http://my_virtdb:8890/sparql")
    sparql.setQuery(query)

    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    final_results = ""

    for result in results["results"]["bindings"]:

        final_results += result["s"]["value"] + " " + result["p"]["value"] + " " + result["o"]["value"] + "\n"

    return final_results