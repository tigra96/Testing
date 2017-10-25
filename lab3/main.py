from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput
import pandas as pd
import numpy as np
import math
from Matrix import *
from Vector import *
from SGD import *
from matplotlib import pyplot as plt
from pandas.parser import CParserError


def draw_SGD_error(stoch_errors_by_iter):
	plt.plot(range(len(stoch_errors_by_iter)), stoch_errors_by_iter)
	plt.xlabel('Iteration number')
	plt.ylabel('MSE')


def main():
	graphviz = GraphvizOutput()
	graphviz.output_file = 'C:/Users/Sasha/Documents/Univer/Testing/lab3/2.png'
	
	try:
		file_obj = open('advertising.csv', 'r')
		file_list = list(file_obj)
	except UnicodeDecodeError:
		print('File is empty or damaged !')
		raise KeyboardInterrupt    
	except FileNotFoundError:
		print('No file !')
		raise KeyboardInterrupt

	X = []
	for row in file_list:
		try:
			X.append([float(i) for i in row.replace("\n", "").split(",")])        
		except:
			pass



	with PyCallGraph(output=graphviz):
		y = Vector([X[i][len(X[i])-1] for i in range(len(X))])
		X = Matrix([X[i][1:-1] for i in range(len(X))])	
		
		X_tr = X.transform()	

		norm_eq_weights = X.weights(y.to_array())
		norm_eq_weights = [float(i[0]) for i in norm_eq_weights]	
		
		print ('MSE with matrix decomposition method = ', y.mserror(np.dot(X_tr, norm_eq_weights)))
		

		StGD = SGD2(np.array(X_tr), y, np.zeros(4))
		stoch_grad_desc_weights, stoch_errors_by_iter = StGD.stochastic_gradient_descent()

		draw_SGD_error(stoch_errors_by_iter)
		
		y_pred = Matrix.matmult(X_tr, stoch_grad_desc_weights.reshape([4,1]))
		print('MSE with SGD method = ', y.mserror([y[0] for y in y_pred]))
		
if __name__ == "__main__":
    main()