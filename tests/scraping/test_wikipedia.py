# -*- coding: utf-8 -*-

import unittest
import sys,os

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../../lib/utils")
from log import Log
from conf import Conf

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../../lib/scraping")
from wikipedia import Wikipedia

class wikipedia_test(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		
		cls.log = Log().getLogger()
		cls.site = Wikipedia()
		cls.log.info("\n\n"+__class__.__name__+ "."+sys._getframe().f_code.co_name+" finished.\n---------- start ---------")

	def setUp(self):
		pass
	"""
	def test_init(self):
		self.log.debug(__class__.__name__ + "." + sys._getframe().f_code.co_name + " start")
		self.log.debug(__class__.__name__ + "." + sys._getframe().f_code.co_name + " finished")

	def test_get(self):
		self.log.debug(__class__.__name__ + "." + sys._getframe().f_code.co_name + " start")
		self.site.get(keywords="country", by="xpath", tag='\
			//th[@scope="row" and @class="navbox-group"]')
		self.log.debug(__class__.__name__ + "." + sys._getframe().f_code.co_name + " finished")
	"""
	"""
	def test_find_elements_of_continents_in_top_page(self):
		self.log.debug(__class__.__name__ + "." + sys._getframe().f_code.co_name + " start")
		self.site.get(keywords="country")
		elements = self.site.find_elements(by="xpath", tag=\
			'//td[@class="navbox-list navbox-odd hlist"]/div/ul/li/a')
		#<td class="navbox-list navbox-even hlist" style="text-align:left;border-left-width:2px;border-left-style:solid;width:100%;padding:0px">
		for el in elements:
			print("#" + el.text + "    " + el.get_attribute("href"))
		self.log.debug(__class__.__name__ + "." + sys._getframe().f_code.co_name + " finished")
		#Africa    https://en.wikipedia.org/wiki/List_of_sovereign_states_and_dependent_territories_in_Africa
		#Antarctica    https://en.wikipedia.org/wiki/Territorial_claims_in_Antarctica
		#Asia    https://en.wikipedia.org/wiki/List_of_sovereign_states_and_dependent_territories_in_Asia
		#Europe    https://en.wikipedia.org/wiki/List_of_sovereign_states_and_dependent_territories_in_Europe
		#North America    https://en.wikipedia.org/wiki/List_of_sovereign_states_and_dependent_territories_in_North_America
		#Oceania    https://en.wikipedia.org/wiki/List_of_sovereign_states_and_dependent_territories_in_Oceania
		#South America    https://en.wikipedia.org/wiki/List_of_sovereign_states_and_dependent_territories_in_South_America
	"""

	def test_get_flags_and_urls(self):
		url = "https://en.wikipedia.org/wiki/List_of_sovereign_states_and_dependent_territories_in_Africa"
		urls = self.site.get_flags(url=url)
		#self.site.driver.save_current_page("../../var/ss/africa.png")
		#self.site.driver.save_current_page("../../var/ss/africa.html")


if __name__ == '__main__':
	unittest.main()
