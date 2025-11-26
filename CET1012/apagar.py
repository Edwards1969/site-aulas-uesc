import numpy as np
import numpy.linalg as nl
	
# Definindo a matriz A
A = np.array([[0.9, 0.3, 0.1],
[0.1, 0.5, 0.2],
[0.0, 0.2, 0.7]])
	
# Calculando a inversa de A
A_inv = nl.inv(A)
	
# Definindo o vetor b
b = np.array([30.0, 25.0, 10.0])
	
# Resolvendo o sistema A.x = b
x = nl.solve(A, b)
	
# Extraindo os valores de x
m1, m2, m3 = x[0], x[1], x[2]
	
# Exibindo os resultados
# print('O valor de m1 = {:.2f} Kg/s'.format(m1))
# print('O valor de m2 = {:.2f} Kg/s'.format(m2))
# print('O valor de m3 = {:.2f} Kg/s'.format(m3))

# Recalculando os valores de b com os resultados obtidos
k1 = 0.9*m1 + 0.3*m2 + 0.1*m3
k2 = 0.1*m1 + 0.5*m2 + 0.2*m3
k3 = 0.2*m2 + 0.7*m3
	
# Exibindo os valores comparativos
# print('Valor esperado b1 = 30.0, valor calculado k1 = {:.2f} Kg/s'.format(k1))
# print('Valor esperado b2 = 25.0, valor calculado k2 = {:.2f} Kg/s'.format(k2))
# print('Valor esperado b3 = 10.0, valor calculado k3 = {:.2f} Kg/s'.format(k3))

x = np.dot(A_inv, b)

print(x)