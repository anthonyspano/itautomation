#!/usr/bin/env python3
import requests

url = "http://localhost/upload"
myfile = 'filelocation'
with open(myfile, 'rb') as opened:
	r = requests.post(url, files={file: opened})