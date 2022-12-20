#!/bin/bash
#takes url and displays all http methods server will accept
curl -s -i -X OPTIONS "$1" | grep "allow"
