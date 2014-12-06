__author__ = 'vlim'




txt = """
    {"employees":[
        {"firstName":"John", "lastName":"Doe"},
        {"firstName":"Anna", "lastName":"Smith"},
        {"firstName":"Peter", "lastName":"Jones"}
    ]}
    """

print "txt: %s" % txt


import base64
encoded = base64.b64encode(txt)

print "encoded: %s" % encoded

data = base64.b64decode(encoded)

print "data: %s" % data

# a, b = 2, 4
#
# print "a: %s" % a
# print "b: %s" % b