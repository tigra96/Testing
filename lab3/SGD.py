import numpy as np


class SGD2:
	def __init__(self, X, y, w):
		self.X = X
		self.y = y
		self.w = w
		


	def stochastic_gradient_descent(self, eta=1e-2, max_iter=1e6,
									min_weight_dist=1e-8, seed=42, verbose=False):
 
 
		def stochastic_gradient_step(X, y, w, train_ind, eta=0.01):
			return w + 2 * eta/X.shape[0] * X[train_ind] * (y[train_ind] - linear_prediction(X[train_ind], w))


		def linear_prediction(X, w):
			return np.dot(X, w)
 
		weight_dist = np.inf
    
		w = self.w

		errors = []

		iter_num = 0

		np.random.seed(seed)

		while weight_dist > min_weight_dist and iter_num < max_iter:

			random_ind = np.random.randint(self.X.shape[0])

			w_new = stochastic_gradient_step(self.X, self.y.to_array(), w, random_ind, eta)
			weight_dist = np.linalg.norm(w - w_new)
			w = w_new
			errors.append(self.y.mserror(linear_prediction(self.X, w)))
			iter_num += 1
        
        
		return w, errors