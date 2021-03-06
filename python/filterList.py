#!/usr/bin/python

import sys
import logging


class FilterListException(Exception):
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
				raise FilterListException("%i item '%s' is not of type string" % (index+1, item))
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

def main(args):
	logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
	# logging.basicConfig(filename='myapp.log', level=logging.INFO)
	filterby = args.filter
	flObj = FilterList(filterby)
	result = flObj.filterList(eval(args.lst))
	if result:
		logging.info(result)
		

if __name__ == "__main__":
	main()
