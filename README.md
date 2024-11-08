## CI for a Flask app 


Send a GET request to '/'
```
curl --resolve "myapp-dev.local:80:127.0.0.1" -i http://myapp-dev.local/
```

Send a GET request to '/metrics'
```
curl --resolve "myapp-dev.local:80:127.0.0.1" -i http://myapp-dev.local/metrics
```

Send a POST request to '/items'
```
curl --resolve "myapp-dev.local:80:127.0.0.1" -i -X POST -H "Content-Type: application/json" -d '{"name": "apple"}' http://myapp-dev.local/items
curl --resolve "myapp-dev.local:80:127.0.0.1" -i -X POST -H "Content-Type: application/json" -d '{"name": "peach"}' http://myapp-dev.local/items
curl --resolve "myapp-dev.local:80:127.0.0.1" -i -X POST -H "Content-Type: application/json" -d '{"name": "pear"}' http://myapp-dev.local/items
curl --resolve "myapp-dev.local:80:127.0.0.1" -i -X POST -H "Content-Type: application/json" -d '{"name": "banana"}' http://myapp-dev.local/items
```

Send a GET request to '/items/[itemID]'
```
curl --resolve "myapp-dev.local:80:127.0.0.1" -i http://myapp-dev.local/items/1
curl --resolve "myapp-dev.local:80:127.0.0.1" -i http://myapp-dev.local/items/2
curl --resolve "myapp-dev.local:80:127.0.0.1" -i http://myapp-dev.local/items/3
```

Send a PUT request to '/items/[itemID]'
```
curl --resolve "myapp-dev.local:80:127.0.0.1" -i -X PUT -H "Content-Type: application/json" -d '{"name": "pear"}' http://myapp-dev.local/items/1
```

Send a DELETE request to 'items/[itemID]'
```
curl --resolve "myapp-dev.local:80:127.0.0.1" -i -X DELETE http://myapp-dev.local/items/1
```
