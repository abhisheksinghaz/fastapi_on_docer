# to create docker image
docker build -t fastapi_app .

# to run the container
docker run -d --name mycontainer -p 80:80 myimage


# try the following requests for hitting all three APIs

1.
request
curl -X 'GET' \
  'http://127.0.0.1/' \
  -H 'accept: application/json'

response body:
{"Hello":"World"}

2. 
request:
curl -X 'GET' \
  'http://127.0.0.1/items/23?q=Abhishek' \
  -H 'accept: application/json'

response body:
{"item_id":23,"q":"Abhishek"}

3.
request:
curl -X 'PUT' \
  'http://127.0.0.1/items/27' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "sample name",
  "price": 100,
  "is_offer": true
}'

response body:
{"item_name":"sample name","item_id":27
