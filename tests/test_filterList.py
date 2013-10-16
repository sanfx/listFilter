import unittest
import filterList
import mox

class TestFilterList(unittest.TestCase):
	"""	docstring for TestFilterList
	"""

	def setUp(self):
		self._filterby = 'B'
		self.flObj = filterList.FilterList(self._filterby)
		self.mox = mox.Mox()

	def tearDown(self):
		self.mox.UnsetStubs()
		self.mox.ResetAll()
		

	def test_stringListItems(self):
		self.assertRaises(filterList.ItemNotString, self.flObj.stringListItems, ['hello', 'Boy', 1])

	def test_stringListItems_True(self):
		self.assertTrue(self.flObj.stringListItems(['Boy','Bar','Home']))

	def test_filterList(self):
		self.assertEquals(['Boy', 'Bar'], self.flObj.filterList(['Home', 'Boy','Bar']))

	def test_usingMox(self):
		self.mox.StubOutWithMock(self.flObj,'stringListItems')
		mockLst = ['Boy','Bar','Home']
		self.flObj.stringListItems(mockLst).AndReturn(True)
		self.mox.ReplayAll()
		filteredList = self.flObj.filterList(mockLst)
		self.assertEquals(['Boy','Bar'], filteredList)
		self.mox.VerifyAll()

if __name__ == '__main__':
	unittest.main()