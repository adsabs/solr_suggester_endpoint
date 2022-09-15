## Service for interacting with the SOLR /suggest endpoint

This service makes calls to the the SOLR /suggest endpoint based on the suggesters that have been defined for:

- Author names: `AuthorSuggesterView`
- Normalized author names: `AuthorNormSuggesterView`
- Universal Astronomy Thesaurus Terms: `UATSuggesterView`

Each suggester uses a slightly different implementation of the SOLR suggester and takes slightly different inputs.
The endpoints defined in this service break out each suggester into its own endpoint and provide reasonable defaults for autocomplete functionality.

`docker-compose` can be used to launch a dev environment that includes an nginx reverse proxy, the microservice containing the `/autocomplete` endpoints, and a build of `montysolr` that includes a modified `solrconfig.xml` that adds the suggestions `SearchComponent` and `/suggest` SOLR endpoint.

```bash
#This builds the images for each container. 
#It's recommended to run without cache because unexpected behavior can occur if monytsolr fails to finish building.
docker-compose build --no-cache

#This launches the services and handles modifying SOLR as well as reading in any records in the json_records folder.
docker-compose up
```