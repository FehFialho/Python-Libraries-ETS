import pandas as pd
import matplotlib.pyplot as plt

fig2, eixo2 = plt.subplots(nrows = 1, ncols = 2, figsize = (10,7))

data1 = []
data2 = []

ticks = [-20, -10, 0, 10, 20]
x = []

for i in range(-20, 21,1):
    data1.append(i**2)
    data2.append(i**3)
    x.append(i)
    
    
eixo2[0].plot(x, data1, color = 'darkred', marker = 'o', linewidth = 10, markersize = 1)
eixo2[0].set_xticks(ticks)
eixo2[0].set_title("f(x) = x²")
eixo2[0].grid()

eixo2[1].plot(x, data2, color = 'forestgreen', marker = 'o', linewidth = 10, markersize = 1)
eixo2[1].set_xticks(ticks)
eixo2[1].set_title("g(x) = x³")
eixo2[1].grid()

# NUMPY
# x = np.linspace(-20,20,200) A partir de -20 e até 20 pega 200 valores igualmente espaçados