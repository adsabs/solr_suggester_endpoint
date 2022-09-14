#!/bin/bash

cd /montysolr/build/contrib/examples/adsabs/
cp /solrconfig.xml ./server/solr/collection1/conf/
chmod +x ./bin/solr
./bin/solr -p 8983