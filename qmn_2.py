# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 15:39:44 2015

@author: sush
"""



class Qnumber:
    'Number to deal with fix point comma numbers'
    def __init__(self, m, n, verbose = False):
        self.m = m
        self.n = n
        self.bitLen = m+n
        self.rawValue      = "not initialized"
        self.rawInteger    = "not initialized"
        self.rawFractional = "not initialized"
        self.value         = "not initialized"
        self.minimumFraction = pow(2,-self.n)
        self.verbose = verbose
        if self.verbose == True:
            print "Empty Q{}.{} initialized. Min Fraction=2^-{} = {}".format(self.m, self.n, self.n,self.minimumFraction)
        
    def destroy(self):
        self.m = 0
        self.n = 0
        self.bitLen = 0
        self.rawValue      = 0
        self.rawInteger    = 0
        self.rawFractional = 0
        self.value         = 0
        self.minimumFraction = 0
        self.verbose = 0
    
    def fromRawInteger(self, valueInteger):
        #Sanity Checks        
        temp = "{0:b}".format(valueInteger)  
        assert len(temp) <= (self.m+self.n)  , "Number exceeds Qmn size"
        
        self.rawValue = valueInteger    
        self.rawInteger = self.rawValue >> self.n
        self.rawFractional = self.rawValue & (~(self.rawInteger << self.n))        
        self.value = self.rawInteger + (self.rawFractional * self.minimumFraction)  
        
        
        if self.verbose == True:
            print  "Raw Value  0d{}".format(self.rawValue)        
            print  "           0x{:X}".format(self.rawValue)
            temp = "           0b{:0" + str(self.bitLen) + "b}"
            print temp.format(self.rawValue)
            print  "Value      0d{}".format(self.value)
            #print "Integer.Fractional"
            #print  "           0d {}.{}".format(self.valueInteger, self.valueFractional)
        
            temp = "           0b{:0" + str(self.m) + "b}.{:0" + str(self.n) + "b}"
            print temp.format(self.rawInteger, self.rawFractional)
        
            #temp = "Fractional 0b{:0" + str(self.n) + "b}"
            #print temp.format(self.rawFractional)
        
        
        
    
    def fromString(self, valueString):
        'valueString: number with the corresponding prefix (0x 0d 0b)'
        #Sanity Checks
        assert "0" == valueString[0]  , "Prefix 0 missing"
        assert len(valueString) >= 3  , "Number with prefix too short"
        
        
        self.rawValue = "empty"
        self.rawValue = 0
        if "x" == valueString[1]:
            self.rawValue = int(valueString,16)
        elif "d" == valueString[1]:
            self.rawValue = int(valueString[2:])
        elif "b" == valueString[1]:
            self.rawValue = int(valueString,2)
        else:
            assert 0, "Wrong Prefix"
        self.fromRawInteger( self.rawValue)
   
    def value(self):
        return self.value