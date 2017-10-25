class Vector:
	def __init__(self, ver):
		self.ver = ver
		
	def length(self):
		return len(self.ver)
		
	def n(self, n):
		return self.ver[n]
		
	def to_array(self):
		return self.ver
		
	def mserror(self, y_pred):
		def mean(data):
			return sum(data) / len(data)
			
		if self.length() == 0 or len(y_pred) == 0:
			raise ValueError ('Вектора пусты !')

		if self.length() != len(y_pred):
			 raise ValueError ('Вектора разной длины !')
			 
		return mean([(self.n(i) - y_pred[i])**2 for i in range(self.length())])