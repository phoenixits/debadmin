#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import time

os.system("clear")
time.sleep(1)

ans=True
while ans:
   print("""
   1. Install Fail2Ban
   2. Check Fail2Ban log
   3. Run Speed Test
   4. Perform Updates
   5. Perform Upgrades
   6. Upgrade Distribution
   7. Clean Up Diskspace
   8. Quit
   """)
   ans=raw_input("What would you like to do? ")
   if ans=="1":
      print("\nInstalling Fail2Ban")
      time.sleep(2)
      os.system("apt-get install fail2ban")
      os.system("clear")
   elif ans=="2":
      time.sleep(2)
      os.system("cat /var/log/fail2ban.log")
   elif ans=="3":
      print("\nRunning Speed Test")
      time.sleep(2)
      os.system("wget -O /dev/null http://speedtest.wdc01.softlayer.com/downloads/test10.zip | grep 'in'")
   elif ans=="4":
      print("\nPerforming Updates")
      time.sleep(2)
      os.system("apt-get update")
   elif ans=="5":
      print("\nPerforming Upgrades")
      time.sleep(2)
      os.system("apt-get upgrade")
   elif ans=="6":
      print("\nPerforming Distribution Upgrades")
      time.sleep(2)
      os.system("apt-get dist-upgrade")
   elif ans=="7":
      time.sleep(2)
      os.system("apt-get clean")
   elif ans=="8":
      print("\nQuitting program...")
      ans = None
   else:
      time.sleep(1)
      print("\n You did something wrong. Try again")
