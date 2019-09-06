#!/usr/bin/env python3

import sys
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from libnessus.parser import NessusParser

chrome_options = Options()
chrome_options.headless = True
driver = webdriver.Chrome('./chromedriver', options=chrome_options)

def verify_ssl(output):
	return re.search(r'SSL : yes', output)

def take_screenshot(ip, port, ssl):
	protocol = 'http'
	if ssl:
		protocol = 'https'

	port_str = ''
	if int(port) != 80 and int(port) != 443:
		port_str = ':{}'.format(port)

	url = '{}://{}{}'.format(protocol, ip, port_str) 
	print('[*] Taking screenshot of {}...'.format(url))
	filename = ip + '_' + port + '.png'
	driver.get(url)
	screenshot = driver.save_screenshot(filename)

def main():
	nessus_file = sys.argv[1]
	nessus = NessusParser.parse_fromfile(nessus_file)
	for host in nessus.hosts:
		for vuln in host.get_report_items:
			info = vuln.get_vuln_info
			if info['pluginID'] == '24260':
				port = info['port']
				ip = host.ip
				ssl = verify_ssl(info['plugin_output'])
				take_screenshot(ip, port, ssl)
				continue
	driver.quit()


if __name__ == '__main__':
	main()
