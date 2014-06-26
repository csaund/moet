"""Carolyn Saund
June 2014
Prosecco jam clusters 
test data generation"""

import random
import json
import sys

people = [{'cluster': None, 'jam_count':None}] * 80
i = 0

text = "{'people' : ["

for i in range(len(people)):
  p = people[i]
  people[i]['cluster'] = random.randint(0,10) #random for now, 0-9
  people[i]['jam_count'] = random.randint(5, 50) #random for now, 5-50
  text += str(people[i]) + ','

text = text[:-1]
text += "], 'user' : 'carolyn'}"

print text

with open('jams.json','w') as outfile:
  json.dump(text, outfile)
