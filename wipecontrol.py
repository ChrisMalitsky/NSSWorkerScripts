﻿# $language = "python"
# $interface = "1.0"

#################################
# Filename      - wipecontrol.py#
# Author        - Joshua Gould  #
# Created       - 12-20-2018    #
# Last Modified - 12-28-2018    #
#################################

# Requirements  - This script runs on SECURE CRT terminals ONLY for CISCO devices
# Description   - Function definition for wiping a CISCO switch or router

def wipecontrol():

	crt.Screen.Synchronous = True
	crt.Screen.Send("admin" + chr(13))
	crt.Screen.WaitForString("Password: ")
        passwd = crt.Dialog.Prompt("Enter password:", "Login", "", True)            # Prompt for password as to not include it in the script
	crt.Screen.Send(passwd + chr(13))
	crt.Screen.WaitForString(">")
	crt.Screen.Send("en" + chr(13))
	crt.Screen.WaitForString("ssword:")
	crt.Screen.Send(passwd + chr(13))
	crt.Screen.WaitForString("#")
	crt.Screen.Send("wr er" + chr(13))
	crt.Screen.WaitForString("Erasing the nvram filesystem will remove all configuration files! Continue? [confirm]")
	crt.Screen.Send(chr(13))
	crt.Screen.WaitForString("#")
	crt.Screen.Send("delete vlan.dat" + chr(13))
	crt.Screen.WaitForString("[vlan.dat]?")
	crt.Screen.Send(chr(13))
	crt.Screen.WaitForString("[confirm]")
	crt.Screen.Send(chr(13))
	crt.Screen.WaitForString("#")
	crt.Screen.Send("reload" + chr(13))
	crt.Screen.WaitForString("Proceed with reload? [confirm]")
	crt.Screen.Send(chr(13))
wipecontrol()   #Call functon
