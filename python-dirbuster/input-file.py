import os

site = input("Enter Site to Scan: \n")
if site[:7] == 'http://':
    name = site[7:]
elif site[:8] == 'https://':
    name = site[8:]
fs = open(name, "x")
fs = open(name, "w")
