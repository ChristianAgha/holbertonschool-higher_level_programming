#!/bin/bash
#Displays the body of a GET request
curl -sL "$1" -X GET -H "X-HolbertonSchool-User-Id: 98"
