#!/bin/bash
#takes url, sends get request and displays response body
curl -s -L "$1" -H "X-School-User-Id: 98"
