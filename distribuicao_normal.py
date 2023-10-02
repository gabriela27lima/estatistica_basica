import pandas as pd
from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt


media = 0.18
desvio_padrao = 0.11
valor = 0.24

probabilidade = norm.cdf(valor, loc=media, scale=desvio_padrao)
probabilidade_final = probabilidade * 100

print(f'A probabilidade de obter um valor menor ou igual a {valor} é: {probabilidade_final:.4f}')

x = np.linspace(media - 4*desvio_padrao, media + 4*desvio_padrao, 1000)
y = norm.pdf(x, loc=media, scale=desvio_padrao)

#plot do gráfico de distribuição

plt.figure(figsize=(10, 6))

plt.plot(x, y, label='Distribuição Normal', color='teal')
plt.fill_between(x, y, where=(x <= valor), color='sandybrown', alpha=0.3, label='Área até $x$')
plt.axvline(x=valor, color='darkred', linestyle='--', label='Valor: {:.2f}'.format(valor))
plt.text(valor + 0.15, 0.7, 'Probabilidade = {:.2%}'.format(probabilidade), color='teal')


plt.title('Distribuição Normal e Probabilidade Cumulativa')
plt.xlabel('Valores')
plt.ylabel('Densidade de Probabilidade')
plt.legend()
plt.grid(True)

plt.show()


# In[ ]:




