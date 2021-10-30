# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 11:22:17 2020

@author: Alejandro
"""


acl= input("what is the IPV4 ACL number? ")
acl=int(acNum)
print("\n"*2)
if acl>= 1 and acl<=99:
    print("This is a standart IPv4 ACL.")
    
  elif acl>=100 and acl<=199:
      print("This is a extended IPv4 ACL.")
  else:
      print("This is not a standart or extended IPv4 ACL")
          