import json
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

f = open("1000-largest-us-cities.json", "r")
words = f.read().split("\n")
f.close()





