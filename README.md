# fastAPI-docker-boilerplate
Boilerplate api written in fastAPI with tests written in pytest. 

# Build the docker image
```
docker build -t <tag name> .
```

# Run tests
```
docker run -t <tag name> pytest
```

# Start the app with the default port 5000
```
docker run -p 127.0.0.1:5000:5000/tcp -t <tag name>
```
