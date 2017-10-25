from Matrix import *
from Vector import *
import unittest


class Test_Matrix(unittest.TestCase):
	# Testing method of  matmult
	def test_1(self):
		self.assertEqual([[1, 6], [1, 24]], Matrix.matmult([[1,0,1], [0,1,5]], [[1,2], [1,4], [0,4]]))	
	
	def test_2(self):
		self.assertRaises(ValueError, Matrix.matmult, *([[2,3,4]], [[4,1,6], [4,0, -1]]))
		
	def test_3(self):
		self.assertEqual([[3]], Matrix.matmult([[1]], [[3]]))
		
	def test_4(self):
		self.assertEqual([], Matrix.matmult([[]], [[]]))

	# Testing method of  inv
	def test_5(self):
		self.assertEqual([], Matrix.inv([[]]))		
		
	def test_6(self):
		self.assertEqual([[0.5]], Matrix.inv([[2]]))	
		
	def test_7(self):
		self.assertRaises(ValueError, Matrix.inv, [[2, 1]])	
		
	def test_8(self):
		self.assertEqual([[0.75, -0.25], [-0.5, 0.5]], Matrix.inv([[2, 1], [2, 3]]))	
				
	def test_9(self):
		self.assertRaises(ZeroDivisionError, Matrix.inv, [[4, 2], [2, 1]])	
		
	# Testing method of  T
	def test_10(self):
		self.assertEqual([], Matrix.T([[]]))
		
	def test_11(self):
		self.assertEqual([[5]], Matrix.T([[5]]))

	def test_12(self):
		self.assertEqual([[5, 1, 4], [8, 0, -1]], Matrix.T([[5, 8], [1, 0], [4, -1]] ))

	def test_13(self):
		self.assertEqual([[5, 1], [8, 0]], Matrix.T([[5, 8], [1, 0]] ))	

	# Testing method of scales
	def test_14(self):
		self.assertEqual([], Matrix.scales([[]]))
		
	def test_15(self):
		self.assertEqual([[5]], Matrix.scales([[5]]))

	def test_16(self):
		self.assertEqual([[-1.0, -1.0], [1.0, 1.0]], Matrix.scales([[2, 1], [3,5]]))

	def test_17(self):
		self.assertEqual([[-1.0, 1], [1.0, 1]], Matrix.scales([[2, 1], [5, 1]]))	
		
	# Testing method of add_ones_col_left
	def test_18(self):
		self.assertEqual([[1]], Matrix.add_ones_col_left([[]]))
		
	def test_19(self):
		self.assertEqual([[1,5]], Matrix.add_ones_col_left([[5]]))

	def test_20(self):
		self.assertEqual([[1, 2, 1], [1.0, 3, 5]], Matrix.add_ones_col_left([[2, 1], [3,5]]))

class Test_Vector(unittest.TestCase):
	# Testing method of  mserror
	def test_1(self):
		V = Vector([])
		self.assertRaises(ValueError, V.mserror, [])	

	def test_2(self):
		V = Vector([1,2,3])
		self.assertRaises(ValueError, V.mserror, [3,1])		

	def test_3(self):
		V = Vector([1,2,3])
		self.assertEqual(2, V.mserror([3,1,4]))	

	def test_4(self):
		V = Vector([1,2,3])
		self.assertEqual(0, V.mserror([1,2,3]))		
