# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 16:43:36 2015

@author: Anyuser
"""

import unittest
import Qsigned as Qmn


class Test_Basics(unittest.TestCase):
        
    def test_0(self):
        with self.assertRaises(AssertionError):
            q = Qmn.Qsigned(0,0)
            q.FromRawString("0b0") # Dummy Line to prevent warnings
        
    def test_1(self):
        with self.assertRaises(AssertionError):
            q = Qmn.Qsigned(-1,0)
            q.FromRawString("0b0") # Dummy Line to prevent warnings
        
    def test_2(self):
        with self.assertRaises(AssertionError):
            q = Qmn.Qsigned(0,1)
            q.FromRawString("0b0") # Dummy Line to prevent warnings
        
    def test_3(self):
        with self.assertRaises(AssertionError):
            q = Qmn.Qsigned(0,-1)
            q.FromRawString("0b0") # Dummy Line to prevent warnings
   
   
class Test_q2_0_Basics(unittest.TestCase):
    def setUp(self):
        self.q = Qmn.Qsigned(2,0)

    def tearDown(self):
        self.q = None
        
    def test_basic(self):
        self.q.FromRawString("0b0")
        self.assertEqual(   1 , self.q.resolution )
        self.assertEqual(  -2 , self.q.min )
        self.assertEqual(   1 , self.q.max )
        
    def test_x0(self):
        self.q.FromRawString("0x0")
        self.assertEqual(0 , self.q.value )
        
    def test_x1(self):
        self.q.FromRawString("0x1")
        self.assertEqual(1 , self.q.value )
        self.q.PrettyPrint()
        
    def test_x2(self):
        self.q.FromRawString("0x2")
        self.assertEqual(-2 , self.q.value )
        
    def test_x3(self):
        self.q.FromRawString("0x3")
        self.assertEqual(-1 , self.q.value )
        
    def test_x4(self):
        with self.assertRaises(AssertionError):
            self.q.FromRawString("0x4")
        
    def test_float_1(self):
        testFloat = 1.0
        errReturn = self.q.FromFloating(testFloat)
        self.assertEqual(testFloat , self.q.value )
        self.assertEqual(0 , errReturn )
        #self.assertAlmostEqual(0.01 , errReturn , 3)
        #self.assertLess(errReturn , self.q.resolution)
        
    def test_float_n1(self):
        testFloat = -1.0
        errReturn = self.q.FromFloating(testFloat)
        self.assertEqual(testFloat , self.q.value )
        self.assertEqual(0 , errReturn )
        
    def test_float_n2(self):
        testFloat = -2.0
        errReturn = self.q.FromFloating(testFloat)
        self.assertEqual(testFloat , self.q.value )
        self.assertEqual(0 , errReturn )



class Test_q3_0_Basics(unittest.TestCase):
    def setUp(self):
        self.q = Qmn.Qsigned(3,0)

    def tearDown(self):
        self.q = None
        
    def test_basic(self):
        self.q.FromRawString("0b0")
        self.assertEqual(   1 , self.q.resolution )
        self.assertEqual(  -4 , self.q.min )
        self.assertEqual(   3 , self.q.max )
        
    def test_x0(self):
        self.q.FromRawString("0x0")
        self.assertEqual(0 , self.q.value )
        
    def test_x1(self):
        self.q.FromRawString("0x1")
        self.assertEqual(1 , self.q.value )
        
    def test_x2(self):
        self.q.FromRawString("0x2")
        self.assertEqual(2 , self.q.value )
        
    def test_x3(self):
        self.q.FromRawString("0x3")
        self.assertEqual(3 , self.q.value )
        
    def test_x7(self):
        self.q.FromRawString("0x7")
        self.assertEqual(-1 , self.q.value )
        
    def test_x6(self):
        self.q.FromRawString("0x6")
        self.assertEqual(-2 , self.q.value )
        
    def test_x5(self):
        self.q.FromRawString("0x5")
        self.assertEqual(-3 , self.q.value )
        
    def test_x4(self):
        self.q.FromRawString("0x4")
        self.assertEqual(-4 , self.q.value )
        self.q.PrettyPrint()
        
    def test_x8(self):
        with self.assertRaises(AssertionError):
            self.q.FromRawString("0x8")



class Test_q2_1_Basics(unittest.TestCase):
    def setUp(self):
        self.q = Qmn.Qsigned(2,1)

    def tearDown(self):
        self.q = None
        
    def test_basic(self):
        self.q.FromRawString("0b0")
        self.assertEqual(   0.5 , self.q.resolution )
        self.assertEqual(   1.5 , self.q.max )
        self.assertEqual(  -2   , self.q.min )
        
    def test_x0(self):
        self.q.FromRawString("0x0")
        self.assertEqual(0 , self.q.value )
        
    def test_x1(self):
        self.q.FromRawString("0x1")
        self.assertEqual(0.5, self.q.value )
        
    def test_x2(self):
        self.q.FromRawString("0x2")
        self.assertEqual( 1 , self.q.value )
        
    def test_x3(self):
        self.q.FromRawString("0x3")
        self.assertEqual(1.5 , self.q.value )
        
    def test_x7(self):
        self.q.FromRawString("0x7")
        self.assertEqual(-0.5 , self.q.value )
        
    def test_x6(self):
        self.q.FromRawString("0x6")
        self.assertEqual(-1 , self.q.value )
        
    def test_x5(self):
        self.q.FromRawString("0x5")
        self.assertEqual(-1.5 , self.q.value )
        
    def test_x4(self):
        self.q.FromRawString("0x4")
        self.assertEqual(-2 , self.q.value )
        
    def test_x8(self):
        with self.assertRaises(AssertionError):
            self.q.FromRawString("0x8")
        
    def test_float_0_3(self):
        testFloat = 0.3
        errReturn = self.q.FromFloating(testFloat)
        self.assertEqual(0.5 , self.q.value )
        self.assertEqual(-0.2 , errReturn )
        
    def test_float_0_5(self):
        testFloat = 0.5
        errReturn = self.q.FromFloating(testFloat)
        self.assertEqual(testFloat , self.q.value )
        self.assertEqual(0 , errReturn )
        
    def test_float_1(self):
        testFloat = 1.0
        errReturn = self.q.FromFloating(testFloat)
        self.assertEqual(testFloat , self.q.value )
        self.assertEqual(0 , errReturn )
        
    def test_float_n2(self):
        testFloat = -2.0
        errReturn = self.q.FromFloating(testFloat)
        self.assertEqual(testFloat , self.q.value )
        self.assertEqual(0 , errReturn )
        self.q.PrettyPrint()
        
    def test_float_n1_5(self):
        testFloat = -1.5
        errReturn = self.q.FromFloating(testFloat)
        self.assertEqual(testFloat , self.q.value )
        self.assertEqual(0 , errReturn )
        
    def test_float_n0_5(self):
        testFloat = -0.5
        errReturn = self.q.FromFloating(testFloat)
        self.assertEqual(testFloat , self.q.value )
        self.assertEqual(0 , errReturn )


class Test_q1_2_Basics(unittest.TestCase):
    def setUp(self):
        self.q = Qmn.Qsigned(1,2)

    def tearDown(self):
        self.q = None
        
    def test_basic(self):
        self.q.FromRawString("0b0")
        self.assertEqual(   0.25 , self.q.resolution )
        self.assertEqual(   0.75 , self.q.max )
        self.assertEqual(  -1   , self.q.min )
        
    def test_x0(self):
        self.q.FromRawString("0x0")
        self.assertEqual(0 , self.q.value )
        
    def test_x1(self):
        self.q.FromRawString("0x1")
        self.assertEqual(0.25, self.q.value )
        
    def test_x2(self):
        self.q.FromRawString("0x2")
        self.assertEqual( 0.5 , self.q.value )
        
    def test_x3(self):
        self.q.FromRawString("0x3")
        self.assertEqual(0.75 , self.q.value )
        
    def test_x7(self):
        self.q.FromRawString("0x7")
        self.assertEqual(-0.25 , self.q.value )
        
    def test_x6(self):
        self.q.FromRawString("0x6")
        self.assertEqual(-0.5 , self.q.value )
        
    def test_x5(self):
        self.q.FromRawString("0x5")
        self.assertEqual(-0.75 , self.q.value )
        
    def test_x4(self):
        self.q.FromRawString("0x4")
        self.assertEqual(-1 , self.q.value )
        
    def test_x8(self):
        with self.assertRaises(AssertionError):
            self.q.FromRawString("0x8")
        
    def test_float_0_75(self):
        testFloat = 0.75
        errReturn = self.q.FromFloating(testFloat)
        self.assertEqual(testFloat , self.q.value )
        self.assertEqual(0 , errReturn )
        
    def test_float_0(self):
        testFloat = 0.0
        errReturn = self.q.FromFloating(testFloat)
        self.assertEqual(testFloat , self.q.value )
        self.assertEqual(0 , errReturn )
        
    def test_float_n0_75(self):
        testFloat = -0.75
        errReturn = self.q.FromFloating(testFloat)
        self.assertEqual(testFloat , self.q.value )
        self.assertEqual(0 , errReturn )
        
    def test_float_n1(self):
        testFloat = -1
        errReturn = self.q.FromFloating(testFloat)
        self.assertEqual(testFloat , self.q.value )
        self.assertEqual(0 , errReturn )
        
    def test_float_n0_8(self):
        testFloat = -0.9
        self.q.FromFloating(testFloat)
        self.assertEqual(-1.0 , self.q.value )
        self.q.PrettyPrint()
        
    def test_n2(self):
        with self.assertRaises(AssertionError):
            self.q.FromFloating(-2.0)
        
    def test_float_min(self):
        with self.assertRaises(AssertionError):
            self.q.FromFloating(-1.0001)
        
    def test_float_max(self):
        with self.assertRaises(AssertionError):
            self.q.FromFloating(+0.75001)
    
 
 
class Test_q32_0_Basics(unittest.TestCase):
    def setUp(self):
        self.q = Qmn.Qsigned(32,0)

    def tearDown(self):
        self.q = None
        
    def test_basic(self):
        self.q.FromRawString("0b0")
        self.assertEqual(   1 , self.q.resolution )
        self.assertEqual(   pow(2,31) -1 , self.q.max )
        self.assertEqual(  -pow(2,31)    , self.q.min )
        self.q.PrettyPrint()
        
    def test_x0(self):
        self.q.FromRawString("0x0")
        self.assertEqual(0 , self.q.value )
        
    def test_x1(self):
        self.q.FromRawString("0x1")
        self.assertEqual(1, self.q.value )
    
 
 
class Test_q64_0_Basics(unittest.TestCase):
    def setUp(self):
        self.q = Qmn.Qsigned(64,0)

    def tearDown(self):
        self.q = None
        
    def test_basic(self):
        self.q.FromRawString("0b0")
        self.assertEqual(   1 , self.q.resolution )
        self.assertEqual(   pow(2,63) -1 , self.q.max )
        self.assertEqual(  -pow(2,63)    , self.q.min )
        self.q.PrettyPrint()
        
    def test_x0(self):
        self.q.FromRawString("0x0")
        self.assertEqual(0 , self.q.value )
        
    def test_x1(self):
        self.q.FromRawString("0x1")
        self.assertEqual(1, self.q.value )
        
 


if __name__ == '__main__':
    
    unittest.main(  )