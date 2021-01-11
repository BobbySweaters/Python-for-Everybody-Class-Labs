
#! Using Web Services
#* Once it became easy to retrieve documents and parse documents over HTTP using programs, it did not take 
#* long to develop an approach where we started producing documents that were specifically designed to be consumed by other 
#* programs (i.e., not HTML to be displayed in a browser).

#! There are two common formats that we use when exchanging data across the web. eXtensible Markup Language (XML)
#! has been in use for a very long time and is best suited for exchanging document-style data. 
#! When programs just want to exchange dictionaries, lists, or other internal information with each other, they use 
#! JavaScript Object Notation (JSON) (see www.json.org). We will look at both formats.


#! eXtensible Markup Language - XML

#* XML looks very similar to HTML, but XML is more structured than HTML. Here is a sample of an XML document:
#<person> 
#  <name>Chuck</name>
#  <phone type="intl">
#    +1 734 303 4456
#  </phone>
#  <email hide="yes" />
#</person>

#! XML is used to separate data prom presentation (HTML)

import xml.etree.ElementTree as ET #* Element tree is built in library that that can read and manipulate XMLs

data = ''' #! this allows for the creation of strings that span multiple lines
<person>
  <name>Chuck</name>
  <phone type="intl">
    +1 734 303 4456
  </phone>
  <email hide="yes" />
</person>'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))

#! XSD Structure - XML Schema Definition

<root>
  <parent>
     <child_one>Y</child_one>
     <child_two>12</child_two>
  </parent>
</root>

#* now here is the design
<xs:schema attributeFormDefault="unqualified" elementFormDefault="qualified" 
xmlns:xs="http://www.w3.org/2001/XMLSchema">
  <xs:element name="root">
    <xs:complexType>
      <xs:sequence>
        <xs:element name="parent">
          <xs:complexType>
            <xs:sequence>
              <xs:element name="child_one" type="xs:string" />
              <xs:element name="child_two" type="xs:int" />
            </xs:sequence>
          </xs:complexType>
        </xs:element>
      </xs:sequence>
    </xs:complexType>
  </xs:element>
</xs:schema>

#! Here:
#! xs:element : Defines an element.
#! xs:sequence : Denotes child elements only appear in the order mentioned.
#! xs:complexType : Denotes it contains other elements.
#! xs:simpleType : Denotes they do not contain other elements.
#! type: string, decimal, integer, boolean, date, time,
#! In simple words, xsd is another way to represent and validate XML data with the specific type.
#! With the help of extra attributes, we can perform multiple operations.
#! Performing any task on xsd is simpler than xml
