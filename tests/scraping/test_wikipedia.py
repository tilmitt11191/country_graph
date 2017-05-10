# -*- coding: utf-8 -*-

import unittest
import sys,os
import time

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
		self.log.debug(
			__class__.__name__ + "." + sys._getframe().f_code.co_name + " start")
		self.site.get(keywords="country")
		continents, urls = self.site.get_urls_of_continents()
		self.assertEqual(
			[
			"Africa",
			"Antarctica",
			"Asia",
			"Europe",
			"North America",
			"Oceania",
			"South America"
			], continents)
		self.assertEqual(
			[
			"https://en.wikipedia.org/wiki/List_of_sovereign_states_and_dependent_territories_in_Africa",
			"https://en.wikipedia.org/wiki/Territorial_claims_in_Antarctica",
			"https://en.wikipedia.org/wiki/List_of_sovereign_states_and_dependent_territories_in_Asia",
			"https://en.wikipedia.org/wiki/List_of_sovereign_states_and_dependent_territories_in_Europe",
			"https://en.wikipedia.org/wiki/List_of_sovereign_states_and_dependent_territories_in_North_America",
			"https://en.wikipedia.org/wiki/List_of_sovereign_states_and_dependent_territories_in_Oceania",
			"https://en.wikipedia.org/wiki/List_of_sovereign_states_and_dependent_territories_in_South_America"
			], urls)

		self.log.debug(__class__.__name__ + "." + sys._getframe().f_code.co_name + " finished")
	"""
	"""
	def test_get_urls_of_countries(self):
		self.log.debug(
			__class__.__name__ + "." + sys._getframe().f_code.co_name + " start")
		countries, urls = self.site.get_urls_of_countries()
		for country in countries:
			print(country)
		print("len(country): " + str(len(country)))
		print("len(urls): " + str(len(urls)))
		
		self.log.debug(
			__class__.__name__ + "." + sys._getframe().f_code.co_name + " finished")
	"""
	def test_get_flag(self):
		self.log.debug(
			__class__.__name__ + "." + sys._getframe().f_code.co_name + " start")
		url = "https://en.wikipedia.org/wiki/Algeria"
		tag = '//div[@class="suggestions-special"]'
		self.site.driver.get(url, tag_to_wait=tag, by="xpath")
		self.site.get_flag(path="../../data/flags/", filename="country")
		# self.site.driver.save_current_page("../../var/ss/algeria_wait.png")
		# self.site.driver.save_current_page("../../var/ss/algeria_wait.html")

		self.log.debug(
			__class__.__name__ + "." + sys._getframe().f_code.co_name + " finished")
	"""
	def test_get_flags_and_urls(self):
		url = "https://en.wikipedia.org/wiki/List_of_sovereign_states_and_dependent_territories_in_Africa"
		urls = self.site.get_flags(url=url)
		#self.site.driver.save_current_page("../../var/ss/africa.png")
		#self.site.driver.save_current_page("../../var/ss/africa.html")
	"""

if __name__ == '__main__':
	unittest.main()
