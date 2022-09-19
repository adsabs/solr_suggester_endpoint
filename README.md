## Service for interacting with the SOLR /suggest endpoint

This service makes calls to the the SOLR /suggest endpoint based on the suggesters that have been defined for:

- Author names: `AuthorSuggesterView`
- Normalized author names: `AuthorNormSuggesterView`
- ADS keywords: `KeywordSuggesterView`

Each suggester uses a slightly different implementation of the SOLR suggester and takes slightly different inputs.
The endpoints defined in this service break out each suggester into its own endpoint and provide reasonable defaults for autocomplete functionality.

### Installation and 
`docker-compose` can be used to launch a dev environment that includes an NGINX reverse proxy, the microservice containing the `/autocomplete` endpoints, and a build of `montysolr` that includes a modified `solrconfig.xml` that adds the suggestions `SearchComponent` and `/suggest` SOLR endpoint.

```bash
#This builds the images for each container. 
#It's recommended to run without cache because unexpected behavior can occur if monytsolr fails to finish building.
docker-compose build --no-cache

#This launches the services and handles modifying SOLR as well as reading in any records in the json_records folder.
docker-compose up
```
prior to running `docker-compose` The user can specify an `$EXTERNAL_IP` for the NGINX to listen on. This should be the network IP of the device if you would like other services on the network to be able to see the endpoint. If `$EXTERNAL_IP` is not set, the service will listen on `127.0.0.1`.

### Usage
Queries can be made against the suggester using 

```bash
curl http://$EXTERNAL_IP:8000/autocomplete/$SUGGESTER_NAME/?q=$QUERY_TEXT&cf=$COLLECTION
```

Currently the three suggesters are:
- `author`: Suggests based on the full author name
- `author_norm`: Suggests based on the normalized author name
- `keyword`: Suggests based on all ADS keywords currently in SOLR

Both `author` and `author_norm` can have an additional field added, `cf`, that allows the user to filter on the ADS collection they would wish to search (ie. astronomy, physics).

### Query Example
``` bash
 curl http://127.0.0.1:8000/autocomplete/author_norm/\?q\=re\&cf\=physics

{"suggestions": ["Rezzolla, L", "Reynolds, C", "Revillet, C", "Reville, V", "Reville, B", "Resconi, E", "Renzi, G", "Renschler, M", "Relethford, B", "Reiss, M", "Reinwardt, S", "Reinhart, M", "Reinhardt, C", "Reimann, R", "Reid, H", "Reichherzer, P", "Reetsong, T", "Reep, J", "Rebolo, R", "Rea, I"]}

```