# -*- coding: utf-8 -*-

import xml.etree.cElementTree as etree
import urllib2
import time

try:
	start_time = time.time()
	xmlDoc = open('../../xml.xml')

	xmlDocData = xmlDoc.read()
	xmlDocTree = etree.XML(xmlDocData)    
	
	#ids = [str(x['id']).replace('L', '') for x in Object.objects.values('id')]	
	
	msg, msg2 = '', ''	
	test_xml = xmlDocTree.iter('object')
	result = []
	for object in test_xml:
		kwargs, photos = {}, ''
		
		for field in object:			
			kwargs[field.tag] = field.text
			
			
												
		
		result.append(kwargs)

	test_res = []
	for line in result:
		if line['personal_beach'] and line['garage'] and line['balcony']:
			test_res.append(line)

	print "after modified"
	print test_res

except urllib2.HTTPError, e:
	raise(e)