#!/bin/bash
#takes url and displays all http methods server will accept
curl -s -i -X "$1"
