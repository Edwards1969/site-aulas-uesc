import numpy as np

# Declaração explícita das frações molares (dados ajustados)
# Coluna 2 (topo y2j e fundo x2j)
y21, y22, y23, y24 = 0.40, 0.30, 0.20, 0.10
x21, x22, x23, x24 = 0.1029198, 0.14320896, 0.39827039, 0.35560085

# Coluna 3 (topo y3j e fundo x3j)
y31, y32, y33, y34 = 0.54115045, 0.24517245, 0.20441150, 0.00926560
x31, x32, x33, x34 = 0.05, 0.10, 0.40, 0.45

# Alimentacao
F = 70.0
z1, z2, z3, z4 = 0.35, 0.25, 0.25, 0.15

# Monta matriz A (colunas: y2j, x2j, y3j, x3j) e vetor b
A = np.array([[y21, x21, y31, x31],
              [y22, x22, y32, x32],
              [y23, x23, y33, x33],
              [y24, x24, y34, x34]])
b = F * np.array([z1, z2, z3, z4])

# Resolve o sistema A v = b
v = np.linalg.solve(A, b)   # [D2, B2, D3, B3]
D2, B2, D3, B3 = v

print("Solução (D2, B2, D3, B3) =")
print(np.round(v,8))

# Calcula D1 e B1
D1 = D2 + B2
B1 = D3 + B3
print("\nD1 = {:.8f}  B1 = {:.8f}".format(D1, B1))

# Composição de D1
if abs(D1) < 1e-12:
    print("\nD1 = 0 (indeterminado). Composição de D1 não definida.")
else:
    y1j = (D2 * np.array([y21, y22, y23, y24]) + B2 * np.array([x21, x22, x23, x24])) / D1
    print("\nComposição de D1 (y1j) =")
    print(np.round(y1j,8))

# Composição de B1
x1j = (D3 * np.array([y31, y32, y33, y34]) + B3 * np.array([x31, x32, x33, x34])) / B1
print("\nComposição de B1 (x1j) =")
print(np.round(x1j,8))

# Verificação do balanço A @ v == b
print("\nVerificação: A @ v - b =")
print(np.round(A.dot(v) - b,12))
