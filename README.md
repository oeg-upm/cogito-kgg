# cogito-kgg
Knowledge Graph Generator for the COGITO Project

````
curl --location --request POST 'localhost:5000/idf2rdf' \
--header 'Content-Type: multipart/form-data' \
--form 'file=@"/home/sgonzalez/Escritorio/Example.ifc"' \
--output 'data.ttl'
````

# Create Docker File and Run
````
docker build -t cogito-kgg .
````
````
docker run cogito-kgg  # if we want to use an specific port use --> -p 5000:5000
````