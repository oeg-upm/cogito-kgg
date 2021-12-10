# cogito-kgg
Knowledge Graph Generator for the COGITO Project

Queries to the triple store:

1. Give me all the spaces located in the building

PREFIX bot: <https://w3id.org/bot#>

SELECT ?x

FROM <http://localhost:8890/building>

WHERE {

?x a bot:Space .

}


2. Obtain the volume of the Space "Space_598"

PREFIX bot: <https://w3id.org/bot#>
PREFIX props: <https://w3id.org/props#>
PREFIX cogito: <http://openmetrics.eu/openmetrics#>

SELECT ?volume
FROM <http://localhost:8890/building>

WHERE {
cogito:Space_598 props:hasVolume ?volume .
}



3. Get all the stories.

PREFIX bot: <https://w3id.org/bot#>

SELECT ?x

FROM <http://localhost:8890/building>

WHERE {

?x a bot:Storey .

}

4. Get all the spaces fo storey cogito:BuildingStorey_133

PREFIX bot: <https://w3id.org/bot#>
PREFIX cogito: <http://openmetrics.eu/openmetrics#>

SELECT ?space

FROM <http://localhost:8890/building>

WHERE {

cogito:BuildingStorey_133 bot:hasSpace ?space .

}

5. Get all the building elements contained in the storey BuildingStorey_133

PREFIX bot: <https://w3id.org/bot#>
PREFIX cogito: <http://openmetrics.eu/openmetrics#>

SELECT ?element

FROM <http://localhost:8890/building>

WHERE {

cogito:BuildingStorey_133 bot:containsElement ?element .

}
