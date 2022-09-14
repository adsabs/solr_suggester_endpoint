## Service for interacting with the SOLR /suggest endpoint

This service makes calls to the the SOLR /suggest endpoint based on the suggesters that have been defined for:

- Author names: `AuthorSuggesterView`
- Normalized author names: `AuthorNormSuggesterView`
- Universal Astronomy Thesaurus Terms: `UATSuggesterView`

Each suggester uses a slightly different implementation of the SOLR suggester and takes slightly different inputs.
The endpoints defined in this service break out each suggester into its own endpoint and provide reasonable defaults for autocomplete functionality.