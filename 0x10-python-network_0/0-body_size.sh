#!/bin/bash
#takes in URL, sends request to that URL and display size of response
curl -s "$1" | wc -c
