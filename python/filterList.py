#!/usr/bin/python

import sys
import ast
import logging


class ItemNotString(Exception):
	pass


class FilterList(object):
	"""	docstring for FilterList
	"""

	def __init__(self, filterby):
		super(FilterList, self).__init__()
		self._filter = filterby

	def stringListItems(self, lst):

		for index, item in enumerate(lst):
			if type(item) == str:
				continue
			else:
				raise ItemNotString("%i item '%s' is not of type string" % (index+1, item))
		return True

	def filterList(self, lst):
		if self.stringListItems(lst):
			if not self._filter:
				logging.info("Nothing passed to filter list %s" % lst)
				return
			filteredList = []
			for eachItem in lst:
				if eachItem.startswith(self._filter):
					filteredList.append(eachItem)
			if filteredList == []:
				logging.info("The list %s doesn't have any matching string item starting with letter '%s'." %(lst, self._filter))
				return
			return filteredList

def main():
	logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
	# logging.basicConfig(filename='myapp.log', level=logging.INFO)
	try:
		filterby = sys.argv[2]
	except IndexError:
		filterby = None
	flObj = FilterList(filterby)
	lst = None
	try:
		lst = sys.argv[1]
	except IndexError:
		logging.info(" No List passed to filter")
	if lst:
		result = flObj.filterList(ast.literal_eval(lst))
		if result:
			logging.info(result)


if __name__ == "__main__":
	main()
