#!/bin/bash
#takes url, sends post request and displays response body
curl -s -X POST "$1" -d "email: test@gmail.com" -d "subject: I will always be here for PLD"
