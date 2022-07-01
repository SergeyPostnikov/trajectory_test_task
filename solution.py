class piecewise_func:
	def __init__(self, x:int, y:int):
		self._x = [x]
		self._y = [y]
		self.pieces = 0

	def __call__(self, x:int, y:int):
		if x in self._x:	
			position = self._x.index(x) 
			self._x[position] = x
			self._y[position] = y
		else:
			self._x += [x] 
			self._y += [y]
			self.pieces += 1
		return self

	def k(self, i:int):
		return (self._y[i + 1] - self._y[i]) / (self._x[i + 1] - self._x[i])

	def b(self, i:int):
		return self._y[i] - self.k(i) * self._x[i]

	def y(self, x:int):
		for i in range(self.pieces):
			if x <= self._x[i + 1]:
				return self.k(i) * x + self.b(i)
			elif x > self._x[i + 1]:
				return self.k(i - 1) * x + self.b(i - 1)