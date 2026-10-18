import numpy as np
import matplotlib.pyplot as plt

N = 3
samples = [1,2,3]
BASE_NAME = "Base OpenSubtitles"

x = np.arange(N)
y = np.array(samples)

plt.scatter(x, y)
plt.ylim(0, 40)  

plt.xlabel("Índice da frase")
plt.ylabel("Número de palavras")
plt.title(BASE_NAME)
plt.text(0, 38, f"Número médio de palavras por frase: {y.mean():.2f}")
plt.text(0, 35, f"Total de frases: {y.size}")
plt.show()
