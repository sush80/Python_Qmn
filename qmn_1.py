# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 16:29:04 2015

@author: sush
"""

    
# m = raw_input("m?")
# n = raw_input("n?")
#valueString = raw_input("Enter the number with the corresponding prefix (0x 0d 0b)")

m = 10
n = 2
valueString = "0d3"
#valueString = "0x3"
#valueString = "0b1111101"


#Sanity Checks
bitLen = m+n
assert "0" == valueString[0]  , "Prefix 0 missing"
assert len(valueString) >= 3  , "Number with prefix too short"

    
#Parse according to prefix
value = 0
if "x" == valueString[1]:
    value = int(valueString,16)
elif "d" == valueString[1]:
    value = int(valueString[2:])
elif "b" == valueString[1]:
    value = int(valueString,2)
else:
    assert 0, "Wrong Prefix"
    

print "Raw Value  0d{}".format(value)
#print "Raw Value  0b{:08b}".format(value)
temp = "Raw Value  0b{:0" + str(bitLen) + "b}"
print temp.format(value)


valueInteger = value >> n
valueFractional = value & (~(valueInteger << n))
print "Integer    0d{}".format(valueInteger)
print "Fractional 0d{}".format(valueFractional)

temp = "Integer    0b{:0" + str(m) + "b}"
print temp.format(valueInteger)

temp = "Fractional 0b{:0" + str(n) + "b}"
print temp.format(valueFractional)
#print "Integer    0b{:08b}".format(valueInteger)
#print "Fractional 0b{:08b}".format(valueFractional)



    
print "la la "

