# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 15:52:17 2015

@author: sush
"""

import qmn_2 as Qmn

print "Tester for Qmn class"

Testnumber = 1

q = Qmn.Qnumber(2,2)
q.prettyPrintt()
q.fromString("0b0")
assert 0 == q.value , "Testnumber {} failed:".format(Testnumber)



q.fromString("0b0101")




    