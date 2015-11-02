# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 15:39:44 2015

@author: sush
"""

'''
### EXAMPLE 
m.n 
2.1 -> 2 data bits + 1 sign bit = 3bits Datatype


2^1       2^0  2^-1 
SignBit    1   1/2
           1   0,5

Max = 1+0,5 = 1,5
    = 2^(m-1)-2^(-n) = 2^(2-1) - 2^-1 = 2 - 0,5 = 1,5
Min = -(2^(-1)m)
Resolution = 2^(-n) = 0,25




			Qs3.0	 Qs2.1	  Qs1.2	
0	0	0	 0	 0	  0	
0	0	1	 1	 0,5	  0,25    Resolution
0	1	0	 2	 1	  0,5	
0	1	1	 3	 1,5	  0,75	    MAX
1	0	0	-4	-2	 -1	    MIN
1	0	1	-3	-1,5	 -0,75	
1	1	0	-2	-1	 -0,5	
1	1	1	-1	-0,5	 -0,25	

'''

class Qsigned:
    'Number to deal with fix point comma numbers'
    def __init__(self, m, n):
        assert (m) > 0   ,   "m must be > 0"
        assert (n) >= 0  , "n must be >= 0"
        self._m = m
        self._n = n
        self._bitLen = m+n
        self._resolution = pow(2,-self._n)
        self._max = pow(2,self._m - 1) - self._resolution
        #self._min = -self._max - self._resolution 
        self._min = -pow(2,self._m -1)  
        self.FromRaw(0)
   
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
        return self._min    
   
        
    def PrettyPrint(self):
        print  "Qsigned  {}.{}".format(self._m, self._n)
        print  "+ Resolution = 2^-{}".format(self._n)
        print  "+            = {}".format(self._resolution)
        print  "+ Max....... = {}".format(self._max)
        print  "+ Min....... = {}".format(self._min)
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
        >>> FromRaw(12345)
        >>> FromRaw(-23)
        
    
        """
        #Sanity Checks        
        temp = "{0:b}".format(raw)  
        assert len(temp) <= (self._m+self._n)  , "Number exceeds Qmn size"
        self._rawValue = raw 
        
        self._rawSignbit = 0
        if 0 != raw & pow(2,self._bitLen -1):
            self._rawSignbit = 1
        
        
        if 0 != self._rawSignbit:
            #highest bit set -> negative number
            #print "negative number detected"
            temp = raw & (~pow(2,self._bitLen -1))
            self._rawInteger = temp >> self._n
            self._rawFractional = temp & (~(self._rawInteger << self._n)) 
            self._value = self.min + (self._rawInteger + (self._rawFractional * self._resolution) )
        else:
            self._rawInteger = self._rawValue >> self._n
            self._rawFractional = self._rawValue & (~(self._rawInteger << self._n)) 
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
        >>> FromRawString("0b1111")
        >>> FromRawString("0d1234")
        >>> FromRawString("0xFF23")
        
    
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
        The returned error might look odd because on floating point calculation issues not solved here
        e.g. 2.26 - 2.25 = 0.00999999999999978
    
        Example
        -------
        >>> FromFloating(0.12)
        >>> FromFloating(1.222)
        >>> FromFloating(123.456)
        >>> FromFloating(-123.456)
        >>> FromFloating(+123.456)
    
        """        
        
        self._rawValue = None
        self._value = None
        
        temp = floatIn / self._resolution
        self.FromRaw(int(round(temp)))
        return (floatIn - self._value)
   