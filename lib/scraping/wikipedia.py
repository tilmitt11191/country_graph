# -*- coding: utf-8 -*-
"""Wikipedia class."""
import sys
import os
import re
from selenium.common.exceptions import StaleElementReferenceException

sys.path.append(
	os.path.dirname(os.path.abspath(__file__)) + "/../../lib/utils")
from conf import Conf
from log import Log
sys.path.append(
	os.path.dirname(os.path.abspath(__file__)) + "/../../lib/scraping")
from phantomjs_ import PhantomJS_

class Wikipedia:
	"""Wikipedia class."""
	def __init__(self):
		"""__init__."""
		self.log = Log.getLogger()
		self.driver = PhantomJS_()
		self.log.debug("class " + __class__.__name__ + " created.")

	def get(self, url= "", keywords="", by="", tag=""):
		"""get."""
		self.log.debug(
			__class__.__name__ + "." + sys._getframe().f_code.co_name + " start")
		if url == "":
			url = Conf.getconf("wikipedia_top_page") + keywords
		self.log.debug("driver.get(" + url + ")")
		self.driver.get(url)
		if by == "" or tag == "":
			self.log.debug("not wait")
		else:
			self.driver.wait_appearance_of_tag(by=by, tag=tag)
		#self.driver.save_current_page("../../var/ss/country_test.png")
		#self.driver.save_current_page("../../var/ss/country_test.html")
		self.log.debug(__class__.__name__ + "." + sys._getframe().f_code.co_name + " finished")

	def get_urls_of_continents(self):
		"""get_urls_of_continents."""
		self.log.debug(
			__class__.__name__ + "." + sys._getframe().f_code.co_name + " start")
		tag = '//td[@class="navbox-list navbox-odd hlist"]/div/ul/li/a'

		self.get(keywords="country", by="xpath", tag=tag)
		elements = self.driver.find_elements_with_handling_exceptions(
			by="XPATH", tag=tag, warning_messages=True, timeout=30, url="")

		continents = []
		urls = []
		for el in elements:
			continents.append(el.text)
			urls.append(el.get_attribute("href"))

		self.log.debug(
			__class__.__name__ + "." + sys._getframe().f_code.co_name + 
			" finished. return urls and continents[" + str(len(urls)) + "]")
		return continents, urls

	def get_urls_of_countries(self):
		"""get_urls_of_continents."""
		self.log.debug(
			__class__.__name__ + "." + sys._getframe().f_code.co_name + " start")
		continents, urls_of_continents = self.get_urls_of_continents()
		tag = '//tr/td/a'
		elements = []
		for url in urls_of_continents:
			self.driver.get(url, tag_to_wait=tag, by="xpath")
			elements.extend(
				self.driver.find_elements_with_handling_exceptions(
				by="XPATH", tag=tag))

		countries = []
		urls = []
		for el in elements:
			try:
				print("urls[" + str(len(urls)) + "], els[" + str(len(elements)) + "]")
				countries.append(el.text)
				urls.append(el.get_attribute("href"))
				print(el.text)
			except StaleElementReferenceException as e:
				self.log.debug("caught " + e.__class__.__name__ + " at click(el.text).")
				self.log.debug("this is flag element. skip.")


		self.log.debug(
			__class__.__name__ + "." + sys._getframe().f_code.co_name + 
			" finished. return urls and countries[" + str(len(urls)) + "]")
		return countries, urls

	def get_flag(self, path="../../data/flags/", filename="country"):
		self.log.debug(
			__class__.__name__ + "." + sys._getframe().f_code.co_name + " start")
		if not re.match("https://en.wikipedia.org/wiki/*", self.driver.current_url):
			self.log.warning(
				"invalid url at " +
				__class__.__name__ + "." + sys._getframe().f_code.co_name)
			return False

		country_name=self.driver.title.split("-")[0].replace(" ", "")
		print("country_name: " + country_name)
		if filename=="country":
			filename=country_name
		print("filename: " + filename)

		tag = '//table[@class="maptable"]/tbody/tr/td/div/a'
		element = self.driver.find_element_with_handling_exceptions(
			by="XPATH", tag=tag)
		flag_url = element.get_attribute("href")
		print("flag_url: " + flag_url)
		
		flag_path = path + filename
		self.log.debug("downloading flag of " + country_name)
		command = "wget \"" + flag_url + "\" -O \"" + flag_path + ".svg\""
		self.log.debug(command)
		try:
			self.log.debug(os.system(command))
		except:
			self.log.warning("error at " + command)

		self.log.debug(
			__class__.__name__ + "." + sys._getframe().f_code.co_name + " finished")
		

	def get_flags(self, url="", path="../../data/flags/", filename="country"):
		self.log.debug(
			__class__.__name__ + "." + sys._getframe().f_code.co_name + " start")
		self.log.debug("url: " + url)
		if url == "":
			return False
		if self.driver.current_url != url:
			self.get(url=url, by="xpath", tag='//div[@class="floatnone"]/a')

		elements = self.driver.find_elements_(by="xpath", tag='//div[@class="floatnone"]/a')
		self.log.debug("len(elements)[" + str(len(elements)) + "]")

		country_name = elements[0].get_attribute("href").split("_")[-1]
		if filename == "" or filename == "country":
			filename = country_name + ".png"

		flag_url = elements[0].find_element_by_css_selector('img').get_attribute("src")

		self.log.debug("downloading flag of " + country_name)
		#ommand = "wget -p \"" + flag_url + "\" -O \"" + path + filename + "\""
		command = "wget \"" + flag_url + "\" -O \"" + path + filename + "\""
		self.log.debug(command)
		try:
			self.log.debug(os.system(command))
		except:
			self.log.warning("error at " + command)

		self.log.debug(__class__.__name__ + "." + sys._getframe().f_code.co_name + " finished")
		return {country_name: flag_url}