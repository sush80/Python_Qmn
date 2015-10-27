# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 15:39:44 2015

@author: sush
"""

'''
### EXAMPLE 
m.n 
2.2

2^1  2^0  2^-1  2^-2
  2    1   1/2  1/4
  2    1   0,5  0,25

Max = 2+1+0,5+0,25 = 3,75
    = 2^(m)-2^(-n) = 2^2-2^-2 = 4 - 0,25 = 3,75
Min = 2^(-n) = 0,25


### EXAMPLE
m.n
0.4
2^-1  2^-2  2^-3  2^-4
1/2   1/4   1/8   1/16   
0,5   0,25  0,125 ...

Max = 1/2 + 1/4 + 1/8 + 1/16   = (1+2+4+8)/16 = 15/16
    = 2^(m)-2^(-n) = 2^0-2^-4 = 1 - (1/16) = 15/16
Min = 2^(-n) = 1/16

### EXAMPLE
 on negative m or n: 
 m.n
-1.5
Total of 4 bits!
2^-2  2^-3  2^-4  2^-5 
1/4   1/8   1/16  1/32

Max = 1/4 + 1/8 + 1/16 + 1/32  = (1+2+4+8)/32 = 15/32 = 0.4687
    = 2^(m)-2^(-n) = 2^2-2^-4 = 1 - (1/16) =  0.4687
Min = 2^(-n) = 1/32

'''

class Qunsigned:
    'Number to deal with fix point comma numbers'
    def __init__(self, m, n):
        assert (m+n) > 0  , "Bitlen (m+n) must be > 0"
        self._m = m
        self._n = n
        self._bitLen = m+n
        self._resolution = pow(2,-self._n)
        self._max = pow(2,self._m) - self._resolution
        self.FromRawInteger(0)
   
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
   
        
    def PrettyPrint(self):
        print  "Qunsigned  {}.{}".format(self._m, self._n)
        print  "+ Resolution = 2^-{}".format(self._n)
        print  "+            = {}".format(self._resolution)
        print  "+ Max....... = {}".format(self._max)
        print  "+ Raw Value  0d{}".format(self._rawValue)        
        print  "+            0x{:X}".format(self._rawValue)
        temp = "+            0b{:0" + str(self._bitLen) + "b}"
        print temp.format(self._rawValue)
        print  "+ Value......0d{}".format(self._value)
        if (self._m > 0) and (self._n > 0):
            temp = "+            0b{:0" + str(self._m) + "b}.{:0" + str(self._n) + "b}"
            print temp.format(self._rawInteger, self._rawFractional)
        elif self._m == 0 :
            assert self._rawInteger == 0 , "sanity test"
            temp = "+            0b.{:0" + str(self._n) + "b}"
            print temp.format(self._rawFractional)
        elif self._n == 0 :
            assert self._rawFractional == 0 , "sanity test"
            temp = "+            0b{:0" + str(self._m) + "b}"
            print temp.format(self._rawInteger)
        elif self._m  < 0:
            print "+             FIXME binary representation"
        elif self._n  < 0:
            print "+             FIXME binary representation"
        else:
            assert False , "Should never happen"
        
        
    
    def FromRaw(self, raw):
        """
        Read Q Value from Raw Integer value
    
        Parameters
        ----------
        raw : Integer
          Raw Representation of Number
    
        Returns
        -------
        nothing
    
        Example
        -------
        >>> q.FromRaw(12345)
        
    
        """
        #Sanity Checks        
        temp = "{0:b}".format(raw)  
        assert len(temp) <= (self._m+self._n)  , "Number exceeds Qmn size"
        
        self._rawValue = raw 
        if self._n >= 0:
            self._rawInteger = self._rawValue >> self._n
            self._rawFractional = self._rawValue & (~(self._rawInteger << self._n)) 
        else:
            self._rawInteger = self._rawValue << (-self._n)
            self._rawFractional = self._rawValue & (~(self._rawInteger >> (-self._n))) 
        self._value = self._rawInteger + (self._rawFractional * self._resolution)  
        

        
        
    
    def FromRawString(self, valueString):
        """
        Read Q Value from String representing a Raw Q Value
    
        Parameters
        ----------
        valueString : String
          number with the corresponding prefix (0x 0d 0b)
    
        Returns
        -------
        nothing
    
        Example
        -------
        >>> q.FromRawString("0b1111")
        >>> q.FromRawString("0d1234")
        >>> q.FromRawString("0xFF23")
        
    
        """
        #Sanity Checks
        assert "0" == valueString[0]  , "Prefix 0 missing"
        assert len(valueString) >= 3  , "Number with prefix too short"
        
        
        self._rawValue = None
        self._value = None
        
        if "x" == valueString[1]:
            self._rawValue = int(valueString,16)
        elif "d" == valueString[1]:
            self._rawValue = int(valueString[2:])
        elif "b" == valueString[1]:
            self._rawValue = int(valueString,2)
        else:
            assert 0, "Wrong Prefix"
        self.FromRaw( self._rawValue)
    
    def FromFloating(self, floatIn):
        """
        Read Q Value from Floating Point Number
    
        Parameters
        ----------
        
        floatIn : float or double
          number representing the real value
    
        Returns
        -------
        The Error Difference due to internal representation (floatIn - Qmn.value)
    
        Example
        -------
        >>> q.FromFloating(0.12)
        >>> q.FromFloating(1.222)
        >>> q.FromFloating(123.456)
    
        """        
        
        self._rawValue = None
        self._value = None
        
        temp = floatIn / self._resolution
        self.FromRawInteger(int(round(temp)))
        return 3
        #return (floatIn - self._value)
   