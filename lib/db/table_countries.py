
# -*- coding: utf-8 -*-

import sys,os

from sqlalchemy import create_engine, Column
from sqlalchemy.dialects.mysql import INTEGER, TINYTEXT
from sqlalchemy.dialects.mysql import BIGINT
from sqlalchemy.ext.declarative import declarative_base

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../../lib/utils")
from log import Log

import mysql_operator

"""
id int, \
name tinytext, \
contents_path tinytext, \
flag_path tinytext);\
"""
Base = declarative_base()
class Table_countries(Base):
	__tablename__ = 'tf_countries'

	id = Column("id", INTEGER, primary_key=True)
	name = Column("name", TINYTEXT)
	contents_path = Column("contents_path", TINYTEXT)
	flag_path = Column("flag_path", TINYTEXT)

	def __init__(self, id="", name="", contents_path="", flag_path=""):
	
		self.log = Log.getLogger()
		
		self.db = mysql_operator.Mysql_operator()
		
		self.id = id
		self.name = name
		self.contents_path = contents_path
		self.flag_path = flag_path

	def __repr__(self):
		return 'Table_countries'

	def insert(self):
		if self.id == "":
			self.id = self.db.get_available_id(__class__)
		self.db.insert(self)
		self.db.session.expunge(self)
		self.db.session.close()

	def renewal_insert(self):
		pass

	def close(self):
		self.db.close()
	
	def get_vars(self):
		import inspect
		methods = []
		for method in inspect.getmembers(self, inspect.ismethod):
			methods.append(method[0])
		
		vars = ""
		for var in self.__dir__():
			if var != "db" and var != "metadata" and var !="log" and not var.startswith("_") and not var in methods:
				vars += var + "[" + str(eval("self."+var)) + "]"
		return vars

