#!/bin/bash

# Build image
docker build --tag=calculator-api .

# List docker images
docker image ls

# Run flask app
docker run -p 8000:5001 calculator-api