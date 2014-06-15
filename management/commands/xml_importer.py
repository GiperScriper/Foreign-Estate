# -*- coding: utf-8 -*-

from django.core.management.base import NoArgsCommand, CommandError
from django.http import HttpResponse

import xml.etree.cElementTree as etree
import urllib2
import time

from foreign_estate.models import Object

# your custom command must reference the base management classes like this:
class Command(NoArgsCommand):
    # it's useful to describe what the function does:
    help = 'XML import to Database'

    def handle_noargs(self, **options):
		try:
			start_time = time.time()
			
			xmlDoc = urllib2.urlopen('http://tranio.ru/export-static/utf-8/digital_team.xml')
			xmlDocData = xmlDoc.read()
			xmlDocTree = etree.XML(xmlDocData)    
			
			# Получаем список ids которые уже есть в БД
			ids = [str(x['id']).replace('L', '') for x in Object.objects.values('id')]

			# Поля для проверки, не должны быть пустыми
			fields_to_check = ['description_full', 'rooms_living', 'area_object', 'country', 'region', 'locality']
			
			# Проходим по дереву, добавляем в словарь и сохраняем
			for object in xmlDocTree.iter('object'):
				kwargs, photos = {}, ''
				flag = True

				if object[0].text not in ids:
					for field in object:
						
						if field.tag == 'address_splitted':
							for address in field:
								kwargs[address.tag] = address.text
						
						elif field.tag == 'photos':
							for url in field:
								photos += "{0} ".format(url.text)
							kwargs['photos'] = photos.split()				
						
						elif field.tag in fields_to_check:
							if not field.text:
								flag = False
							else:
								kwargs[field.tag] = field.text

						else:
							kwargs[field.tag] = field.text					
					
					if flag:
						object = Object( **kwargs ).save()
				
			# Время работы скрипта
			total_work_time = time.time() - start_time
			return 'Время работы: {0} cек.'.format(total_work_time)
		
		except urllib2.HTTPError, e:
			print 'xml файл не найден, {0}'.format(e)		