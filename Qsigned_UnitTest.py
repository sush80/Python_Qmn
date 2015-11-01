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
        self.assertEqual(  -1 , self.q.min )
        self.assertEqual(   1 , self.q.max )
        
    def test_x0(self):
        self.q.FromRawString("0x0")
        self.assertEqual(0 , self.q.value )

        
        
 
if __name__ == '__main__':
    
    unittest.main(  )