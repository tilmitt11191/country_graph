
# -*- coding: utf-8 -*-

import unittest
import sys,os
import re
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../../lib/utils")
from log import Log
from conf import Conf

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../../lib/scraping")
from phantomjs_ import PhantomJS_


class webdriver_test(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		
		cls.log = Log().getLogger()
		cls.log.debug("test")
		cls.driver = PhantomJS_()
		cls.conf = Conf()
		cls.log.info("\n\n"+__class__.__name__+ "."+sys._getframe().f_code.co_name+" finished.\n---------- start ---------")

	def setUp(self):
		pass
	"""
	def test_get(self):
		self.log.debug(__class__.__name__ + "." + sys._getframe().f_code.co_name + " start")
		url = "http://ieeexplore.ieee.org/Xplore/home.jsp"
		self.driver.get(url)
		self.driver.save_current_page("../../var/ss/test_get.png")
		self.log.debug(__class__.__name__ + "." + sys._getframe().f_code.co_name + " finished")
	"""
	"""
	def test_reconnect(self):
		self.log.debug(__class__.__name__ + "." + sys._getframe().f_code.co_name + " start")
		url = "http://ieeexplore.ieee.org/Xplore/home.jsp"
		self.driver.reconnect(url)
		#self.driver.save_current_page("./samples/test_reconnect.png")
		self.log.debug(__class__.__name__ + "." + sys._getframe().f_code.co_name + " finished")

	def test_save_current_page(self):
		self.log.debug(__class__.__name__ + "." + sys._getframe().f_code.co_name + " start")
		url = "http://ieeexplore.ieee.org/document/1055638/"
		self.driver.get(url)
		self.driver.save_current_page("../../var/ss/" + re.sub(r"/|:|\?|\.", "", url) + ".png")
		self.driver.save_current_page("../../var/ss/" + re.sub(r"/|:|\?|\.", "", url) + ".html")

		self.log.debug(__class__.__name__ + "." + sys._getframe().f_code.co_name + " finished")
	"""
	def test_convert_svg_to_png(self):
		self.log.debug(__class__.__name__ + "." + sys._getframe().f_code.co_name + " start")
		svg_path = "../../var/flags/Algeria.svg"
		self.driver.convert_svg_to_png(svg_path)
		self.log.debug(__class__.__name__ + "." + sys._getframe().f_code.co_name + " finished")

if __name__ == '__main__':
	unittest.main()
