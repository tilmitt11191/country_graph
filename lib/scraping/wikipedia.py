# -*- coding: utf-8 -*-

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../../lib/utils")
from conf import Conf
from log import Log
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../../lib/scraping")
from phantomjs_ import PhantomJS_

class Wikipedia:
	def __init__(self):
		self.log = Log.getLogger()
		self.driver = PhantomJS_()
		self.log.debug("class " + __class__.__name__ + " created.")

	def get(self, url= "", keywords="", by="", tag=""):
		self.log.debug(__class__.__name__ + "." + sys._getframe().f_code.co_name + " start")
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

	def find_elements(self, by="", tag=""):
		self.log.debug(__class__.__name__ + "." + sys._getframe().f_code.co_name + " start")
		self.log.debug("by[" + by + "], tag[" + tag + "]")
		if by == "" or tag == "":
			self.log.warning("by and/or tag not set. return []")
			return []

		elements = self.driver.find_elements_(by=by, tag=tag)
		self.log.debug(__class__.__name__ + "." + sys._getframe().f_code.co_name + " finished")
		return elements
	

	def get_flags(self, url="", path="../../data/flags/", filename="country"):
		self.log.debug(__class__.__name__ + "." + sys._getframe().f_code.co_name + " start")
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