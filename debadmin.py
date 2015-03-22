#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import time

os.system("clear")
time.sleep(1)

def Header():
   print("#" * 70)
   os.system("whoami")
   print("Server:")
   os.system("hostname -I")
   print("Uptime:")
   os.system("uptime")
   print("Status:")
   os.system("service apache2 status")
   print("#" * 70)

def Upgrade():
   print "####################################"
   print "# Running Upgrade Process          #"
   print "####################################"
   print "Please wait..."
   time.sleep(2)
   os.system("clear")
   print("Running package updates")
   time.sleep(2)
   os.system("apt-get update")
   os.system("clear")
   time.sleep(2)
   print "Completed..."
   time.sleep(2)
   os.system("clear")
   print "Upgrading Installed Packages"
   time.sleep(2)
   os.system("apt-get upgrade")
   os.system("clear")
   time.sleep(2)
   print "Completed..."
   time.sleep(2)
   os.system("clear")
   print("Upgrading Linux Distribution")
   time.sleep(2)
   os.system("apt-get dist-upgrade")
   os.system("clear")
   time.sleep(2)
   print("Completed...")
   time.sleep(2)
   os.system("clear")
   time.sleep(2)
   print("Cleaning Disk Space")
   time.sleep(2)
   os.system("apt-get clean")
   os.system("apt-get clean all")
   time.sleep(2)
   print("Completed...")
   time.sleep(2)
   os.system("clear")
   print("Process complete...")
   time.sleep(2)
   

def MemUsage():
   print "##########################"
   print "# Free Memory            #"
   print "##########################"
   time.sleep(2)
   os.system("free -m")
   print("Process complete...")
   time.sleep(2)

def SpeedTest():
   print "###########################"
   print "# Performing Speed Test   #"
   print "###########################"
   time.sleep(2)
   os.system("wget -O /dev/null http://speedtest.wdc01.softlayer.com/downloads/test10.zip | grep 'in'")
   print("Process complete...")
   time.sleep(2)

def InstallFB():
   print "##########################"
   print "# Installing Fail2Ban    #"
   print "##########################"
   time.sleep(2)
   os.system("apt-get install fail2ban")
   print("Process complete...")
   time.sleep(2)

def checkBanLog():
   print "##########################"
   print "# Checking Fail2Ban Log  #"
   print "##########################"
   time.sleep(2)
   os.system("cat /var/log/fail2ban.log")
   time.sleep(2)
   print("Process complete...")
   time.sleep(2)

def memoryUsage():
   print "##########################"
   print "# Checking Memory Usage  #"
   print "##########################"
   time.sleep(2)
   os.system("clear")
   print "#################################################"
   print "# Memory Usage                                  #"
   print "#                                               #"
   os.system("egrep --color 'Mem|Cache|Swap' /proc/meminfo")
   print "#################################################"

def installApache():
   print("#" * 70)
   print("Installing Apache2 and PHP")
   time.sleep(2)
   os.system("clear")
   print("Installing Apache2 now...")
   time.sleep(2)
   os.system("apt-get install apache2")
   print("Completed...")
   time.sleep(2)
   os.system("clear")
   print("Installing PHP5 now...")
   os.system("apt-get install php5 php-pear php5-mysql")
   print("Completed...")
   time.sleep(2)
   os.system("clear")
   print("Restarting Apache2...")
   time.sleep(2)
   os.system("service apache2 restart")
   print("Completed...")
   time.sleep(2)
   os.system("clear")
   print("Checking PHP Version...")
   time.sleep(2)
   os.system("php -v")
   time.sleep(2)
   
def startApache():
   print("#" * 70)
   print("Starting Apache2 Service please wait...")
   time.sleep(2)
   os.system("clear")
   os.system("service apache2 start")
   print("Apache2 Server service started...")
   time.sleep(2)

def stopApache():
   print("#" * 70)
   print("Stopping Apache2 Service please wait...")
   time.sleep(2)
   os.system("clear")
   os.system("service apache2 stop")
   time.sleep(2)

Header()        
ans=True
while ans:
   print("""
   1. Install Fail2Ban
   2. Check Fail2Ban log
   3. Run Speed Test
   4. Perform Updates & Upgrades & Clean Disk Space 
   5. Memory Usage and Free Memory
   6. Install Apache2 & PHP5
   7. Start Apache2 Service
   8. Stop Apache2 Service
   9. Quit
   """)
   ans=raw_input("What would you like to do? ")
   if ans=="1":
      InstallFB()
      os.system("clear")
      Header()
   elif ans=="2":
      checkBanLog()
      time.sleep(2)
      os.system("clear")
      Header()
   elif ans=="3":
      SpeedTest()
      time.sleep(2)
      os.system("clear")
      Header()
   elif ans=="4":
      Upgrade()
      time.sleep(2)
      os.system("clear")
      Header()
   elif ans=="5":
      memoryUsage()
      MemUsage()
      time.sleep(2)
      os.system("clear")
      Header()
   elif ans=="6":
      installApache()
      time.sleep(2)
      os.system("clear")
      Header()
   elif ans=="7":
      startApache()
      time.sleep(2)
      Header()
   elif ans=="8":
      stopApache()
      time.sleep(2)
      Header()
   elif ans=="9":
      print("\nQuitting program...")
      ans = None
   else:
      time.sleep(1)
      print("\n You did something wrong. Try again")

