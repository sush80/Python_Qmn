# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 16:43:36 2015

@author: sush
"""

import unittest
import qmn_2 as Qmn

class Test_q2_2_Basics(unittest.TestCase):
    def setUp(self):
        self.q = Qmn.Qnumber(2,2)

    def tearDown(self):
        self.q = -1
        
    def test_q2_2__b0000(self):
        self.q.fromString("0b0")
        self.assertEqual(0 , self.q.value )
    def test_q2_2__b0101(self):
        self.q.fromString("0b0101")
        self.assertEqual(1.25 , self.q.value )
    def test_q2_2__b1010(self):
        self.q.fromString("0b1010")
        self.assertEqual(2.5 , self.q.value )
    def test_q2_2__b1111(self):
        self.q.fromString("0b1111")
        self.assertEqual(3.75 , self.q.value )
    def test_q2_2__xF(self):
        self.q.fromString("0xF")
        self.assertEqual(3.75 , self.q.value )
    def test_q2_2__x0(self):
        self.q.fromString("0x0")
        self.assertEqual(0 , self.q.value )
    def test_q2_2__xA(self):
        self.q.fromString("0xA")
        self.assertEqual(2.5 , self.q.value )
    def test_q2_2__x5(self):
        self.q.fromString("0x5")
        self.assertEqual(1.25 , self.q.value )

class Test_q8_0_Basics(unittest.TestCase):
    def setUp(self):
        self.q = Qmn.Qnumber(8,0)

    def tearDown(self):
        self.q = -1
        
    def test_q8_0_x00(self):
        self.q.fromString("0x00")
        self.assertEqual(0 , self.q.value )
    def test_q8_0_x01(self):
        self.q.fromString("0x01")
        self.assertEqual(1 , self.q.value )
    def test_q8_0_x80(self):
        self.q.fromString("0x80")
        self.assertEqual(128 , self.q.value )
    def test_q8_0_x100(self):
        with self.assertRaises(AssertionError):
            self.q.fromString("0x100")

class Test_q32_0_Basics(unittest.TestCase):
    def setUp(self):
        self.q = Qmn.Qnumber(32,0)

    def tearDown(self):
        self.q = -1
        
    def test_q32_0_x00(self):
        self.q.fromString("0x00")
        self.assertEqual(0 , self.q.value )
    def test_q32_0_x01(self):
        self.q.fromString("0x01")
        self.assertEqual(1 , self.q.value )
    def test_q32_0_x80(self):
        self.q.fromString("0x80")
        self.assertEqual(128 , self.q.value )
    def test_q32_0_x100(self):
        with self.assertRaises(AssertionError):
            self.q.fromString("0x100000000")

        
        
        
 
if __name__ == '__main__':
 
    unittest.main()