
#! XML parsing

import xml.etree.ElementTree as ET #import the element tree built in function

data = '''
<person>
  <name>Chuck</name>
  <phone type="intl">
    +1 734 303 4456
  </phone>
  <email hide="yes" />
</person>'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text) #this will pull the text from the name tag
print('Attr:', tree.find('email').get('hide') #this will pull the hide value from email tag. The get finds the attribute hide within the email tag

#! Looping through nodes. Often the XML has multiple nodes and we need to write a loop to process all of the nodes. 
#! In the following program, we loop through all of the user nodes:

import xml.etree.ElementTree as ET

input = '''
<stuff>
  <users>
    <user x="2">
      <id>001</id>
      <name>Chuck</name>
    </user>
    <user x="7">
      <id>009</id>
      <name>Brent</name>
    </user>
  </users>
</stuff>'''

stuff = ET.fromstring(input) #take all of the text and pass it through fromstring
lst = stuff.findall('users/user') #search for all of the usertags using findall in list form
print('User count:', len(lst)) #this is letting us know how many users are in the text

for item in lst: #now we loop through each instance of users identified above
    print('Name', item.find('name').text) #within the item, we are looking for name tag and text within
    print('Id', item.find('id').text) #within the item, we are looking for the id
    print('Attribute', item.get('x')) #within the item, we are looking for the x attribute
