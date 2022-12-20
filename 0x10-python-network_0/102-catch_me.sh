#!/bin/bash
#makes request to specific url and responds with message
curl -s -L -X PUT 0.0.0.0:5000/catch_me -H "Origin: HolbertonSchool" -d "user_id=98"
