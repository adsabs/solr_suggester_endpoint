#!/bin/bash

cd /app/montysolr/build/contrib/examples/adsabs/
cp /app/local/scripts/solrconfig.xml ./server/solr/collection1/conf/
chmod +x ./bin/solr
chmod +x ./bin/post
./bin/solr -p 8983 -force
./bin/post -c collection1 /app/local/scripts/json_records/* -p 8983

echo "For interactive access, run in a diferent terminal:"
echo "  docker exec -it solr_search bash"
echo "Press CTRL+c to stop"
tail -f /dev/null