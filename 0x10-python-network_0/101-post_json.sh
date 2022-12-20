#!/bin/bash
#sends JSON POST request to url and displays response body
curl -s "$1" -H "Content-Type: application/json" -H "Accept: application/json" -d "[json data]"
