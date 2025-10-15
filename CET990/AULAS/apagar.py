import numpy as np
import matplotlib.pyplot as plt

# Parâmetros físicos
m = 100.0            # massa de água (kg)
Cp = 4180.0          # calor específico (J/kg°C)
eta = 0.95           # eficiência
P_max = 1000.0       # potência máxima (W)
hA = 15.0            # coeficiente global de perda térmica (W/°C)
T_amb = 25.0         # temperatura ambiente (°C)

# Parâmetros de simulação
dt = 1.0             # passo de tempo (s)
t_final = 2000       # tempo total (s)
n = int(t_final / dt)

# Sinal de referência (setpoint)
T_sp = 60.0          # °C

# Parâmetros do PID
Kp = 8.0
Ki = 0.02
Kd = 100.0

# Variáveis de controle
integral = 0.0
erro_anterior = 0.0

# Vetores de armazenamento
tempo = np.arange(0, t_final, dt)
T = np.zeros(n)
T[0] = 25.0          # temperatura inicial
u = np.zeros(n)      # sinal de controle (0–100%)
I_mA = np.zeros(n)   # corrente do transmissor

# Funções de instrumentação virtual
def sensor(temp_real):
    """Sensor com ruído aleatório"""
    ruido = np.random.normal(0, 0.2)
    return temp_real + ruido

def transmissor(temp_sensor):
    """Converte 0–100 °C em 4–20 mA"""
    return 4 + (16/100) * temp_sensor

def atuador(u_percent):
    """Converte 0–100% em potência (W)"""
    return (u_percent/100) * P_max

# Simulação
for i in range(1, n):
    # Sensor
    T_sensor = sensor(T[i-1])
    
    # Erro de controle
    erro = T_sp - T_sensor
    
    # PID discreto
    integral += erro * dt
    derivada = (erro - erro_anterior) / dt
    u[i] = Kp*erro + Ki*integral + Kd*derivada
    erro_anterior = erro
    
    # Saturação (0 a 100%)
    u[i] = max(0, min(100, u[i]))
    
    # Atuador (potência elétrica)
    P = atuador(u[i])
    
    # Modelo térmico (integração de Euler)
    dTdt = (eta*P - hA*(T[i-1] - T_amb)) / (m*Cp)
    T[i] = T[i-1] + dTdt*dt
    
    # Transmissor (corrente em mA)
    I_mA[i] = transmissor(T_sensor)

# Plot dos resultados
plt.figure(figsize=(10,6))
plt.plot(tempo, T, label='Temperatura (°C)')
plt.axhline(T_sp, color='r', linestyle='--', label='Setpoint (°C)')
plt.xlabel('Tempo (s)')
plt.ylabel('Temperatura (°C)')
plt.legend()
plt.grid(True)
plt.title('Resposta da Temperatura no Tanque')
plt.show()

plt.figure(figsize=(10,6))
plt.plot(tempo, u, label='Sinal de controle (%)')
plt.xlabel('Tempo (s)')
plt.ylabel('Controle (%)')
plt.legend()
plt.grid(True)
plt.title('Ação de Controle PID')
plt.show()

plt.figure(figsize=(10,6))
plt.plot(tempo, I_mA, label='Sinal do Transmissor (mA)')
plt.xlabel('Tempo (s)')
plt.ylabel('Corrente (mA)')
plt.legend()
plt.grid(True)
plt.title('Sinal de Corrente Enviado pelo Transmissor')
plt.show()