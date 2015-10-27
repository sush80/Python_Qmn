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
        self.q.FromRawString("0b0")
        self.assertEqual(0.25 , self.q.resolution )
        self.assertEqual(0 , self.q.min )
        self.assertEqual(3.75 , self.q.max )
        
    def test_b0000(self):
        self.q.FromRawString("0b0")
        self.assertEqual(0 , self.q.value )
    def test_b0101(self):
        self.q.FromRawString("0b0101")
        self.assertEqual(1.25 , self.q.value )
    def test_b1010(self):
        self.q.FromRawString("0b1010")
        self.assertEqual(2.5 , self.q.value )
    def test_b1111(self):
        self.q.FromRawString("0b1111")
        self.assertEqual(3.75 , self.q.value )
    def test_xF(self):
        self.q.FromRawString("0xF")
        self.assertEqual(3.75 , self.q.value )
        self.q.PrettyPrint()
    def test_x0(self):
        self.q.FromRawString("0x0")
        self.assertEqual(0 , self.q.value )
    def test_xA(self):
        self.q.FromRawString("0xA")
        self.assertEqual(2.5 , self.q.value )
    def test_x5(self):
        self.q.FromRawString("0x5")
        self.assertEqual(1.25 , self.q.value )
    def test_float_0(self):
        errReturn = self.q.FromFloating(0.0)
        #self.assertEqual(0 , errReturn )
        #self.assertEqual(0 , self.q.value )


class Test_q1_0_Basics(unittest.TestCase):
    def setUp(self):
        self.q = Qmn.Qunsigned(1,0)

    def tearDown(self):
        self.q = None
        
    def test_basic(self):
        self.q.FromRawString("0b0")
        self.assertEqual(   1 , self.q.resolution )
        self.assertEqual(   0 , self.q.min )
        self.assertEqual(   1 , self.q.max )
        
    def test_x0(self):
        self.q.FromRawString("0x0")
        self.assertEqual(0 , self.q.value )
    def test_x1(self):
        self.q.FromRawString("0x1")
        self.assertEqual(1 , self.q.value )
    def test_d1(self):
        self.q.FromRawString("0d1")
        self.assertEqual(1 , self.q.value )
        self.q.PrettyPrint()
    def test_d2(self):
        with self.assertRaises(AssertionError):
            self.q.FromRawString("0d2")
    def test_x2(self):
        with self.assertRaises(AssertionError):
            self.q.FromRawString("0x2")
    def test_b10(self):
        with self.assertRaises(AssertionError):
            self.q.FromRawString("010")


class Test_q0_1_Basics(unittest.TestCase):
    def setUp(self):
        self.q = Qmn.Qunsigned(0,1)

    def tearDown(self):
        self.q = None
        
    def test_basic(self):
        self.q.FromRawString("0b0")
        self.assertEqual( 0.5 , self.q.resolution )
        self.assertEqual(   0 , self.q.min )
        self.assertEqual( 0.5 , self.q.max )
        
    def test_x0(self):
        self.q.FromRawString("0x0")
        self.assertEqual(0 , self.q.value )
    def test_x1(self):
        self.q.FromRawString("0x1")
        self.assertEqual(0.5 , self.q.value )
        self.q.PrettyPrint()
    def test_d1(self):
        self.q.FromRawString("0d1")
        self.assertEqual(0.5 , self.q.value )
    def test_d2(self):
        with self.assertRaises(AssertionError):
            self.q.FromRawString("0d2")
    def test_x2(self):
        with self.assertRaises(AssertionError):
            self.q.FromRawString("0x2")
    def test_b10(self):
        with self.assertRaises(AssertionError):
            self.q.FromRawString("010")


class Test_q8_0_Basics(unittest.TestCase):
    def setUp(self):
        self.q = Qmn.Qunsigned(8,0)

    def tearDown(self):
        self.q = None
        
    def test_basic(self):
        self.q.FromRawString("0b0")
        self.assertEqual(   1 , self.q.resolution )
        self.assertEqual(   0 , self.q.min )
        self.assertEqual( 255 , self.q.max )
        
    def test_x00(self):
        self.q.FromRawString("0x00")
        self.assertEqual(0 , self.q.value )
    def test_x01(self):
        self.q.FromRawString("0x01")
        self.assertEqual(1 , self.q.value )
        self.q.PrettyPrint()
    def test_x80(self):
        self.q.FromRawString("0x80")
        self.assertEqual(128 , self.q.value )
    def test_x100(self):
        with self.assertRaises(AssertionError):
            self.q.FromRawString("0x100")


class Test_q32_0_Basics(unittest.TestCase):
    def setUp(self):
        self.q = Qmn.Qunsigned(32,0)

    def tearDown(self):
        self.q = None
        
    def test_x00(self):
        self.q.FromRawString("0x00")
        self.assertEqual(0 , self.q.value )
    def test_x01(self):
        self.q.FromRawString("0x01")
        self.assertEqual(1 , self.q.value )
        self.q.PrettyPrint()
    def test_x80(self):
        self.q.FromRawString("0x80")
        self.assertEqual(128 , self.q.value )
    def test_x100(self):
        with self.assertRaises(AssertionError):
            self.q.FromRawString("0x100000000")



class Test_q_n1_2_Basics(unittest.TestCase):
    def setUp(self):
        self.q = Qmn.Qunsigned(-1,2)

    def tearDown(self):
        self.q = None
        
    def test_basic(self):
        self.q.FromRawString("0b0")
        self.assertEqual( 0.25, self.q.resolution )
        self.assertEqual(   0 , self.q.min )
        self.assertEqual( 0.25 , self.q.max )
        
    def test_x0(self):
        self.q.FromRawString("0x0")
        self.assertEqual(0 , self.q.value )
    def test_x1(self):
        self.q.FromRawString("0x1")
        self.assertEqual(0.25 , self.q.value )
        self.q.PrettyPrint()
    def test_d1(self):
        self.q.FromRawString("0d1")
        self.assertEqual(0.25 , self.q.value )
    def test_d2(self):
        with self.assertRaises(AssertionError):
            self.q.FromRawString("0d2")
    def test_x2(self):
        with self.assertRaises(AssertionError):
            self.q.FromRawString("0x2")
    def test_b10(self):
        with self.assertRaises(AssertionError):
            self.q.FromRawString("0b10")


class Test_q_2_n1_Basics(unittest.TestCase):
    def setUp(self):
        self.q = Qmn.Qunsigned(2,-1)

    def tearDown(self):
        self.q = None
        
    def test_basic(self):
        self.q.FromRawString("0b0")
        self.assertEqual(   2  , self.q.resolution )
        self.assertEqual(   0  , self.q.min )
        self.assertEqual(   2  , self.q.max )
        
    def test_x0(self):
        self.q.FromRawString("0x0")
        self.assertEqual(0 , self.q.value )
    def test_x1(self):
        self.q.FromRawString("0x1")
        self.assertEqual( 2 , self.q.value )
        self.q.PrettyPrint()
    def test_d1(self):
        self.q.FromRawString("0d1")
        self.assertEqual(2 , self.q.value )
    def test_d2(self):
        with self.assertRaises(AssertionError):
            self.q.FromRawString("0d2")
    def test_x2(self):
        with self.assertRaises(AssertionError):
            self.q.FromRawString("0x2")
    def test_b10(self):
        with self.assertRaises(AssertionError):
            self.q.FromRawString("0b10")



class Test_q_n1_3_Basics(unittest.TestCase):
    def setUp(self):
        self.q = Qmn.Qunsigned(-1,3)

    def tearDown(self):
        self.q = None
        
    def test_basic(self):
        self.q.FromRawString("0b00")
        self.assertEqual( 0.125, self.q.resolution )
        self.assertEqual(   0  , self.q.min )
        self.assertEqual( 0.375 , self.q.max )
        
    def test_x0(self):
        self.q.FromRawString("0x0")
        self.assertEqual(0 , self.q.value )
    def test_x1(self):
        self.q.FromRawString("0x1")
        self.assertEqual(0.125 , self.q.value )
        self.q.PrettyPrint()
    def test_d1(self):
        self.q.FromRawString("0d1")
        self.assertEqual(0.125 , self.q.value )
    def test_d2(self):
        self.q.FromRawString("0d2")
        self.assertEqual(0.25 , self.q.value )
    def test_d3(self):
        self.q.FromRawString("0d3")
        self.assertEqual(0.375 , self.q.value )
    def test_d4(self):
        with self.assertRaises(AssertionError):
            self.q.FromRawString("0d4")
    def test_x4(self):
        with self.assertRaises(AssertionError):
            self.q.FromRawString("0x4")
    def test_b101(self):
        with self.assertRaises(AssertionError):
            self.q.FromRawString("0b101")



class Test_q_3_n1_Basics(unittest.TestCase):
    def setUp(self):
        self.q = Qmn.Qunsigned(3,-1)

    def tearDown(self):
        self.q = None
        
    def test_basic(self):
        self.q.FromRawString("0b0")
        self.assertEqual(   2  , self.q.resolution )
        self.assertEqual(   0  , self.q.min )
        self.assertEqual(   6  , self.q.max )
        
    def test_x0(self):
        self.q.FromRawString("0x0")
        self.assertEqual(0 , self.q.value )
    def test_x1(self):
        self.q.FromRawString("0x1")
        self.assertEqual( 2 , self.q.value )
        self.q.PrettyPrint()
    def test_d1(self):
        self.q.FromRawString("0d1")
        self.assertEqual(2 , self.q.value )
    def test_d2(self):
        self.q.FromRawString("0d2")
        self.assertEqual(4 , self.q.value )
    def test_d3(self):
        self.q.FromRawString("0d3")
        self.assertEqual(2+4 , self.q.value )
    def test_d4(self):
        with self.assertRaises(AssertionError):
            self.q.FromRawString("0d4")
    def test_x4(self):
        with self.assertRaises(AssertionError):
            self.q.FromRawString("0x4")
    def test_b101(self):
        with self.assertRaises(AssertionError):
            self.q.FromRawString("0b101")
            
# Q-1.3
# Q-4.?4
# Q3.-1
# Q?4.-4
# Q64.0
# Q0.64

        
        
 
if __name__ == '__main__':
 
    unittest.main()