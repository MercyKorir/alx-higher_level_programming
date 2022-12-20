#!/bin/bash
#sends request to url and displays only status code of response
curl -s -o /dev/null -w "%{http_code}" "$1"
