# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 16:43:36 2015

@author: sush
"""

import unittest
import Qsigned as Qmn


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
        
    def test_x2(self):
        self.q.FromRawString("0x2")
        self.assertEqual(-2 , self.q.value )
        
    def test_x3(self):
        self.q.FromRawString("0x3")
        self.assertEqual(-1 , self.q.value )
        
    def test_x4(self):
        with self.assertRaises(AssertionError):
            self.q.FromRawString("0x4")



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
    
 
if __name__ == '__main__':
    
    unittest.main(  )