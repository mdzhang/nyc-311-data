load:
	http POST "http://localhost:9200/311_data/311_data/_bulk" --json < items.json

all:
	http GET "http://localhost:9200/311_data/_search?pretty=true&q=*:*"

search:
	http GET "http://localhost:9200/311_data/_search?pretty=true" --json < query.json

rm:
	http DELETE "http://localhost:9200/311_data"

build-items:
	python script.py | jq -c . > items.json

