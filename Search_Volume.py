#coding:utf-8
PURPLE  = '\033[35m'
RED     = '\033[31m'
CYAN    = '\033[36m'
OKBLUE  = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL    = '\033[91m'
ENDC    = '\033[0m'

from time import sleep
import requests
import csv
import codecs

a = open('suggest_list.dat','r')
b = open('volume_list.csv','w')

for i in a:
	i = i.rstrip()
	print i
	URL = 'http://aramakijake.jp/keyword/index.php?keyword=' + i
	#print URL
	r = requests.get(URL)
	content = r.text
	if 'alt="Google"' in content:
		volume = content.split('alt="Google"',2)
		volume = volume[1]
		volume = volume.split('<span>',2)
		volume = volume[1]
		volume = volume.split('</span>',2)
		volume = volume[0]
		volume = volume.replace('<span>','')
		volume = volume.replace('/>','')
		volume = volume.replace(' ','')
		volume = volume.replace(' ','')
		volume = volume.replace('\t','')
		volume = volume.replace(',','')
		print OKGREEN + str(volume.encode('utf_8')) + ENDC
		b.write(i+','+ volume.encode('utf_8') + '\n')
	else:
		print OKGREEN + '0'  + ENDC
		b.write(i+','+ '0'  + '\n')
	sleep(1)

a.close()
