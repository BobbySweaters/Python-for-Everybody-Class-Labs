

#! JavaScript Object Notation - JSON
#! The JSON format was inspired by the object and array format used in the JavaScript language.
#! But since Python was invented before JavaScript, Python’s syntax for dictionaries and lists influenced the syntax of JSON. 
#! So the format of JSON is nearly identical to a combination of Python lists and dictionaries.

#! Here is a JSON encoding that is roughly equivalent to the simple XML from above:

import json #JSON represents data as nested "lists" and "dictionaries"

data = '''{
  "name" : "Chuck",
  "phone" : {
    "type" : "intl",
    "number" : "+1 734 303 4456"
   },
   "email" : {
     "hide" : "yes"
   }
}'''

info = json.loads(data) #Info is a dictionary, but you can call it anything. 
# Loads JSON and parses it into a structured object in the form of a python dictionary with key value pairs
print('Name', info['name'])
print('Hide', info['email']['hide'])
print()

import json

data = '''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Brent"
  }
]'''

info = json.loads(data)
print('User count:', len(info))

for item in info:
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])