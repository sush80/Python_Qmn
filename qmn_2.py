# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 15:39:44 2015

@author: sush
"""

'''
Example 
m.n 
2.2

2^1  2^0  2^-1  2^-2
  2    1   0,5  0,25

Max = 2+1+0,5+0,25 = 3,75
    = 2^(m)-2^(-n) = 2^2-2^-2 = 4 - 0,25 = 3,75
Min = 2^(-n) = 0,25

'''


class Qunsigned:
    'Number to deal with fix point comma numbers'
    def __init__(self, m, n, verbose = False):
        self._m = m
        self._n = n
        self._bitLen = m+n
        self._resolution = pow(2,-self._n)
        self._max = pow(2,self._m) - self._resolution
        self._verbose = verbose
        self.FromRawInteger(0)
        if self._verbose == True:
            print "Empty Q{}.{} initialized. Min Fraction=2^-{} = {}".format(self._m, self._n, self._n,self._resolution)
   
    @property
    def value(self):
        return self._value   
        
    @property
    def resolution(self):
        return self._resolution
        
    @property
    def max(self):
        return self._max  
        
    @property
    def min(self):
        return 0         
   
        
    def PrettyPrintt(self):
        print "Qunsigned {}.{}".format(self._m, self._n)
        print " Resolution = 2^-{}".format(self._n)
        print "              = {}".format(self._resolution)
        print " Max          = {}".format(self._max)
        print  " Raw Value  0d{}".format(self._rawValue)        
        print  "            0x{:X}".format(self._rawValue)
        temp = "            0b{:0" + str(self._bitLen) + "b}"
        print temp.format(self._rawValue)
        print  " Value      0d{}".format(self._value)
        temp = "            0b{:0" + str(self._m) + "b}.{:0" + str(self._n) + "b}"
        print temp.format(self._rawInteger, self._rawFractional)
        
        
    
    def FromRawInteger(self, rawInteger):
        #Sanity Checks        
        temp = "{0:b}".format(rawInteger)  
        assert len(temp) <= (self._m+self._n)  , "Number exceeds Qmn size"
        
        self._rawValue = rawInteger    
        self._rawInteger = self._rawValue >> self._n
        self._rawFractional = self._rawValue & (~(self._rawInteger << self._n))        
        self._value = self._rawInteger + (self._rawFractional * self._resolution)  
        
        
        if self._verbose == True:
            print  "Raw Value  0d{}".format(self._rawValue)        
            print  "           0x{:X}".format(self._rawValue)
            temp = "           0b{:0" + str(self._bitLen) + "b}"
            print temp.format(self._rawValue)
            print  "Value      0d{}".format(self._value)
            #print "Integer.Fractional"
            #print  "           0d {}.{}".format(self._valueInteger, self._valueFractional)
        
            temp = "           0b{:0" + str(self._m) + "b}.{:0" + str(self._n) + "b}"
            print temp.format(self._rawInteger, self._rawFractional)
        
            #temp = "Fractional 0b{:0" + str(self._n) + "b}"
            #print temp.format(self._rawFractional)
        
        
        
    
    def FromString(self, valueString):
        'valueString: number with the corresponding prefix (0x 0d 0b)'
        #Sanity Checks
        assert "0" == valueString[0]  , "Prefix 0 missing"
        assert len(valueString) >= 3  , "Number with prefix too short"
        
        
        self._rawValue = "empty"
        self._rawValue = 0
        if "x" == valueString[1]:
            self._rawValue = int(valueString,16)
        elif "d" == valueString[1]:
            self._rawValue = int(valueString[2:])
        elif "b" == valueString[1]:
            self._rawValue = int(valueString,2)
        else:
            assert 0, "Wrong Prefix"
        self.FromRawInteger( self._rawValue)
   