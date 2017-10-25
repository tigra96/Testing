import math

class Matrix:
	def __init__(self, Marr):
		self.Marr = Marr
	
	def shape(Marr):
		if [i for i in Marr if i]:
			return (len(Marr), len(Marr[0]))
		else:
			return(0,0)

	def T(Marr):
		Marr_T = []
		for i in zip(*Marr):
			Marr_T.append(list(i))
		return Marr_T

	def scales(Marr):

		if Matrix.shape(Marr) == (0,0):
			return []
			
		def mean(data):
			return sum(data) / len(data)
	
		def std(data):
			return math.sqrt(sum([(i - mean(data)) ** 2  for i in data]) / len(data))
		
		means = [mean([Marr[j][i] for j in range(len(Marr))]) for i in range(len(Marr[0]))]
		stds = [std([Marr[j][i] for j in range(len(Marr))]) for i in range(len(Marr[0]))]

		for i in range(len(Marr)):
			Marr[i] = [(Marr[i][j] - means[j]) / stds[j] if stds[j] != 0 else Marr[i][j] for j in range(len(Marr[0]))]
		return Marr

	def add_ones_col_left(Marr):
		Marr = [[1] + Marr[i] for i in range(len(Marr))]
		return Marr
	
	def inv(Marr):

		if Matrix.shape(Marr) == (0,0):
			return []
			
		if Matrix.shape(Marr)[0] != Matrix.shape(Marr)[1]:
			raise ValueError (r"Матрица должна быть квадратной !")
			
		N = Matrix.shape(Marr)[1]
		E =  [[1 if i == j else 0 for i in range(N) ] for j in range(N)]
		M = [Marr[i] + E[i] for i in range(N)]
		
		for col in range(N):
			main_el = M[col][col]
			if main_el == 0:
				raise ZeroDivisionError  (' Определитель = 0! Обратная матрица не может быть посчитана ! ')
			for i in range(2*N):
				M[col][i] /= main_el
			for row in range(N):
				if col != row:
					M[row] = [M[row][i] - M[row][col]*M[col][i] for i in range(2*N)]
				

		return [[M[i][j] for j in range(N, N*2)] for i in range(N)]
	
	def matmult(a, b):	
		if Matrix.shape(a)[1] != Matrix.shape(b)[0]:
			raise ValueError(" Число столбцов первой матрицы не совпадает с числом строк второй !")

		
		if Matrix.shape(a) == (0,0):
			return []
			
		Z = []
		for row_a in a:
			zip_b = zip(*b)
			Z.append([sum(ele_a*ele_b for ele_a, ele_b in zip(row_a, col_b)) for col_b in zip_b])
		return Z
	
	def pseudo_inverse(Marr):  
		Marr_T = Matrix.T(Marr)		
		Marr = Matrix.matmult(Marr_T, Marr)
		Marr = Matrix.inv(Marr)
		return Matrix.matmult(Marr, Marr_T)
				

	def transform(self):
		self.Marr = Matrix.scales(self.Marr)
		self.Marr = Matrix.add_ones_col_left(self.Marr)
		return self.Marr
	
	def weights(self, y):
		self.Marr = Matrix.pseudo_inverse(self.Marr)
		return Matrix.matmult(self.Marr, Matrix.T([y]))
	
	
