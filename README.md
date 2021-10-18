# cogito-kgg
Knowledge graph generator for the COGITO project


curl --location --request POST 'localhost:5000/idf2rdf' \
--header 'Content-Type: multipart/form-data' \
--form 'file=@"/home/sgonzalez/Escritorio/Example.ifc"' \
--output 'data.ttl'

# Create Docker File and Run
docker build -t cogito-kgg .
docker run cogito-kgg