# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 16:43:36 2015

@author: sush
"""

import unittest
import qmn_2 as Qmn

class Test_q2_2_Basics(unittest.TestCase):
    def setUp(self):
        self.q = Qmn.Qunsigned(2,2)

    def tearDown(self):
        self.q = None
        
    def test_basic(self):
        self.q.FromString("0b0")
        self.assertEqual(0.25 , self.q.resolution )
        self.assertEqual(0 , self.q.min )
        self.assertEqual(3.75 , self.q.max )
        
    def test_b0000(self):
        self.q.FromString("0b0")
        self.assertEqual(0 , self.q.value )
    def test_b0101(self):
        self.q.FromString("0b0101")
        self.assertEqual(1.25 , self.q.value )
    def test_b1010(self):
        self.q.FromString("0b1010")
        self.assertEqual(2.5 , self.q.value )
    def test_b1111(self):
        self.q.FromString("0b1111")
        self.assertEqual(3.75 , self.q.value )
    def test_xF(self):
        self.q.FromString("0xF")
        self.assertEqual(3.75 , self.q.value )
    def test_x0(self):
        self.q.FromString("0x0")
        self.assertEqual(0 , self.q.value )
    def test_xA(self):
        self.q.FromString("0xA")
        self.assertEqual(2.5 , self.q.value )
    def test_x5(self):
        self.q.FromString("0x5")
        self.assertEqual(1.25 , self.q.value )

class Test_q1_0_Basics(unittest.TestCase):
    def setUp(self):
        self.q = Qmn.Qunsigned(1,0)

    def tearDown(self):
        self.q = None
        
    def test_basic(self):
        self.q.FromString("0b0")
        self.assertEqual(   1 , self.q.resolution )
        self.assertEqual(   0 , self.q.min )
        self.assertEqual(   1 , self.q.max )
        
    def test_x0(self):
        self.q.FromString("0x0")
        self.assertEqual(0 , self.q.value )
    def test_x1(self):
        self.q.FromString("0x1")
        self.assertEqual(1 , self.q.value )
    def test_d1(self):
        self.q.FromString("0d1")
        self.assertEqual(1 , self.q.value )
    def test_d2(self):
        with self.assertRaises(AssertionError):
            self.q.FromString("0d2")
    def test_x2(self):
        with self.assertRaises(AssertionError):
            self.q.FromString("0x2")
    def test_b10(self):
        with self.assertRaises(AssertionError):
            self.q.FromString("010")

class Test_q0_1_Basics(unittest.TestCase):
    def setUp(self):
        self.q = Qmn.Qunsigned(0,1)

    def tearDown(self):
        self.q = None
        
    def test_basic(self):
        self.q.FromString("0b0")
        self.assertEqual( 0.5 , self.q.resolution )
        self.assertEqual(   0 , self.q.min )
        self.assertEqual( 0.5 , self.q.max )
        
    def test_x0(self):
        self.q.FromString("0x0")
        self.assertEqual(0 , self.q.value )
    def test_x1(self):
        self.q.FromString("0x1")
        self.assertEqual(0.5 , self.q.value )
    def test_d1(self):
        self.q.FromString("0d1")
        self.assertEqual(0.5 , self.q.value )
    def test_d2(self):
        with self.assertRaises(AssertionError):
            self.q.FromString("0d2")
    def test_x2(self):
        with self.assertRaises(AssertionError):
            self.q.FromString("0x2")
    def test_b10(self):
        with self.assertRaises(AssertionError):
            self.q.FromString("010")

class Test_q8_0_Basics(unittest.TestCase):
    def setUp(self):
        self.q = Qmn.Qunsigned(8,0)

    def tearDown(self):
        self.q = None
        
    def test_basic(self):
        self.q.FromString("0b0")
        self.assertEqual(   1 , self.q.resolution )
        self.assertEqual(   0 , self.q.min )
        self.assertEqual( 255 , self.q.max )
        
    def test_x00(self):
        self.q.FromString("0x00")
        self.assertEqual(0 , self.q.value )
    def test_x01(self):
        self.q.FromString("0x01")
        self.assertEqual(1 , self.q.value )
    def test_x80(self):
        self.q.FromString("0x80")
        self.assertEqual(128 , self.q.value )
    def test_x100(self):
        with self.assertRaises(AssertionError):
            self.q.FromString("0x100")

class Test_q32_0_Basics(unittest.TestCase):
    def setUp(self):
        self.q = Qmn.Qunsigned(32,0)

    def tearDown(self):
        self.q = None
        
    def test_x00(self):
        self.q.FromString("0x00")
        self.assertEqual(0 , self.q.value )
    def test_x01(self):
        self.q.FromString("0x01")
        self.assertEqual(1 , self.q.value )
    def test_x80(self):
        self.q.FromString("0x80")
        self.assertEqual(128 , self.q.value )
    def test_x100(self):
        with self.assertRaises(AssertionError):
            self.q.FromString("0x100000000")

        
        
        
 
if __name__ == '__main__':
 
    unittest.main()