import numpy as np 

def fun(x):
	F = x**2 - 4 
	return F

def bsc (a,b):
	if fun(a) * fun(b) >= 0:
		print('No solution using Bisection Method')
		return None
	tol = 0.00000001
	N = 76 # numero de interacoes
	for i in range (1,N+1):
		
		c = (a + b)/2
		if (fun(a)*fun(c)) < 0:
			b = c
		else:
			a = c
		i = i + 1

		print ( "%d \t %.6f\t %.6f\t %.6f\t %.6f" %(i-1 ,a ,b ,c ,fun(c)) )

	if abs((a-b)/2.0) < tol:
		print ('The root after %dth iteration is %.10f.'%(i-1,c) )
	else:
		print ('We were unable to meet tolerance within given iterations.')


ans = bsc(0,3)
