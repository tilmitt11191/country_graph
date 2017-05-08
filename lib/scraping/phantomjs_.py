# -*- coding: utf-8 -*-

import sys,os
import re

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotVisibleException
from http.client import RemoteDisconnected

class PhantomJS_(webdriver.PhantomJS):
	def __init__(self, executable_path="",\
					port=0, desired_capabilities=DesiredCapabilities.PHANTOMJS,\
					service_args=None, service_log_path=None):
		self.executable_path = executable_path
		self.port = port
		self.PHANTOMJS = desired_capabilities
		self.service_args = service_args
		self.service_log_path = service_log_path

		sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../lib/utils")
		from conf import Conf
		self.conf = Conf()
		from log import Log as l
		self.log = l.getLogger()
		self.log.debug(__class__.__name__ + "." + sys._getframe().f_code.co_name + " start")

		import logging, logging.handlers
		selenium_logger = logging.getLogger('selenium.webdriver.remote.remote_connection')
		selenium_logger.setLevel(logging.ERROR)
		if len(selenium_logger.handlers) < 1:
			rfh = logging.handlers.RotatingFileHandler(
				filename=self.conf.getconf("logdir")+self.conf.getconf("phantomjs_logfile"),
				maxBytes=self.conf.getconf("rotate_log_size"),
				backupCount=self.conf.getconf("backup_log_count")
			)
			formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
			rfh.setFormatter(formatter)
			selenium_logger.addHandler(rfh)

			stream_handler = logging.StreamHandler()
			stream_handler.setFormatter(formatter)
			stream_handler.setLevel(self.conf.getconf("loglevel_to_stdout"))
			selenium_logger.addHandler(stream_handler)


		if self.executable_path == "":
			self.executable_path = self.conf.getconf("phantomJS_pass")
		if self.service_args == None:
			self.service_args=["--webdriver-loglevel=DEBUG"]
		if self.service_log_path == None:
			self.service_log_path=self.conf.getconf("logdir") + self.conf.getconf("phantomjs_logfile")
		self.log.debug(__class__.__name__ + ".super().__init__ start")
		super().__init__(executable_path=self.executable_path, \
					port=self.port, desired_capabilities=self.PHANTOMJS, \
					service_args=self.service_args, service_log_path=self.service_log_path)


	def get(self, url, tag_to_wait="", by="xpath", timeout=30):
		retries = 10
		while retries > 0:
			try:
				self.log.debug("super().get(" + url + ") start")
				super().get(url)
				break
			except RemoteDisconnected as e:
				self.log.debug("PhantomJS caught RemoteDisconnected at get" + url)
				self.log.debug("%s", e)
				self.log.debug("retries[" + str(retries) + "]")
				super().__init__(executable_path=self.executable_path, \
						port=self.port, desired_capabilities=self.desired_capabilities, \
						service_args=self.service_args, service_log_path=self.service_log_path)
				retries -= 1
			except TimeoutException as e:
				self.log.warning("Caught TimeoutException at super().get(" + url + ")")
				self.log.warning("save_current_page to ../../var/ss/" + e.__class__.__name__ + re.sub(r"/|:|\?|\.", "", self.current_url) + ".html and png")
				self.log.warning(e, exc_info=True)
				self.save_current_page("../../var/ss/" + e.__class__.__name__ + re.sub(r"/|:|\?|\.", "", self.current_url) + ".html")
				self.save_current_page("../../var/ss/" + e.__class__.__name__ + re.sub(r"/|:|\?|\.", "", self.current_url) + ".png")
				self.log.warning("%s", e)
				self.execute_script("window.stop();")

		if retries == 0:
			self.log.error("PhantomJS caught ERROR RemoteDisconnected at get" + url)
			self.save_current_page("./samples/get_error.html")
			self.save_current_page("./samples/get_error.png")

		if tag_to_wait != "":
			self.wait_appearance_of_tag(by="xpath", tag=tag_to_wait, timeout=timeout)


	def find_elements_(self, by="", tag="", warning_messages=True, timeout=30):
		self.log.debug(__class__.__name__ + "." + sys._getframe().f_code.co_name + " start")
		self.log.debug("by[" + by + "], tag[" + tag + "]")

		try:
			if by=="xpath":
				elements = self.find_elements_by_xpath(tag)
			elif by=="css_selector":
				elements = self.find_elements_by_css_selector(tag)
			elif by=="name":
				elements = self.find_elements_by_name(tag)
			elif by=="tag_name":
				elements = self.find_elements_by_tag_name(tag)
			else:
				self.log.waring("type error by=" + by + ", tag: " + tag)
		except (TimeoutException, NoSuchElementException) as e:
			if warning_messages:
				self.log.warning("caught " + e.__class__.__name__ + " at find_elements. url[" + self.current_url + "]")
				self.log.warning("by[" + by + "], tag[" + tag + "]")
				self.log.warning("save_current_page to ../../var/ss/" + e.__class__.__name__ + re.sub(r"/|:|\?|\.", "", self.current_url) + ".html and png")
				self.log.warning(e, exc_info=True)
				self.save_current_page("../../var/ss/" + e.__class__.__name__ + re.sub(r"/|:|\?|\.", "", self.current_url) + ".html")
				self.save_current_page("../../var/ss/" + e.__class__.__name__ + re.sub(r"/|:|\?|\.", "", self.current_url) + ".png")
			else:
				self.log.debug("caught " + e.__class__.__name__ + " at find_elements. url[" + self.current_url + "]")
				self.log.debug("by[" + by + "], tag[" + tag + "]")
			self.log.debug("return False")
			return False

		self.log.debug(__class__.__name__ + "." + sys._getframe().f_code.co_name + " finished. return elements[" + str(len(elements)) + "]")
		return elements


	def wait_appearance_of_tag(self, by="xpath", tag="", warning_messages=True, timeout=30):
		self.log.debug("wait_appearance_of_tag start. tag: " + tag)
		try:
			if by=="xpath":
				WebDriverWait(self, timeout).until(lambda self: self.find_element_by_xpath(tag))
			elif by=="css_selector":
				WebDriverWait(self, timeout).until(lambda self: self.find_element_by_css_selector(tag))
			elif by=="name":
				WebDriverWait(self, timeout).until(lambda self: self.find_element_by_name(tag))
			elif by=="tag_name":
				WebDriverWait(self, timeout).until(lambda self: self.find_element_by_tag_name(tag))
			else:
				self.log.waring("type error by=" + by + ", tag: " + tag)
		except (TimeoutException, NoSuchElementException) as e:
			if warning_messages:
				self.log.warning("caught " + e.__class__.__name__ + " at wait_appearance_of_tag. url[" + self.current_url + "]")
				self.log.warning("by[" + by + "], tag[" + tag + "]")
				self.log.warning("save_current_page to ../../var/ss/" + e.__class__.__name__ + re.sub(r"/|:|\?|\.", "", self.current_url) + ".html and png")
				self.log.warning(e, exc_info=True)
				self.save_current_page("../../var/ss/" + e.__class__.__name__ + re.sub(r"/|:|\?|\.", "", self.current_url) + ".html")
				self.save_current_page("../../var/ss/" + e.__class__.__name__ + re.sub(r"/|:|\?|\.", "", self.current_url) + ".png")
			else:
				self.log.debug("caught " + e.__class__.__name__ + " at wait_appearance_of_tag. url[" + self.current_url + "]")
				self.log.debug("by[" + by + "], tag[" + tag + "]")
			self.log.debug("return False")
			return False

		self.log.debug("tag appeared. wait_appearance_of_tag Finished.return True")
		return True


	def reconnect(self, url=""):
		self.log.debug(__class__.__name__ + "." + sys._getframe().f_code.co_name + " start")
		self.__init__(executable_path=self.executable_path,\
					port=self.port, desired_capabilities=self.PHANTOMJS,\
					service_args=self.service_args, service_log_path=self.service_log_path)
		self.get(url)
		self.log.debug(__class__.__name__ + "." + sys._getframe().f_code.co_name + " finished")

	def save_current_page(self, filename):
		self.log.debug(__class__.__name__ + "." + sys._getframe().f_code.co_name + " start")
		path, suffix=os.path.splitext(filename)
		self.log.debug("path["+path+"], suffix["+suffix+"]")
		if suffix==".html":
			f = open(filename, 'w')
			f.write(self.page_source)
			f.close()
		elif suffix==".png":
			self.save_screenshot(filename)
		else:
			self.log.error(__class__.__name__ + "." + sys._getframe().f_code.co_name)
			self.log.error("TYPEERROR suffix["+suffix+"]")
		self.log.debug(__class__.__name__ + "." + sys._getframe().f_code.co_name + " finished")