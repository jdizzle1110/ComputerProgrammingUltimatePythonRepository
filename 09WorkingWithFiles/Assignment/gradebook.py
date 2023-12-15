import csv
import json
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

f = open("../data/gradebook_data.csv", "r")
