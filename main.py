import numpy as np
import matplotlib.pyplot as plt

x1 = np.linspace(0, 11, 500)
y1 = (80 - 8 * x1) / 5
y2 = (5200 - 208 * x1) / 505

fig, ax = plt.subplots(figsize=(8, 7))

# Прямые ограничений
ax.plot(x1, y1, 'b-', label=r'$8x_1 + 5x_2 = 80$')
ax.plot(x1, y2, 'g-', label=r'$208x_1 + 505x_2 = 5200$')
ax.axvline(7, color='m', linestyle='-', label=r'$x_1 = 7$')

# Заливка ОДР (x1 <= 7)
x_fill = np.linspace(0, 7, 400)
y_top = np.minimum((80 - 8 * x_fill) / 5, (5200 - 208 * x_fill) / 505)
ax.fill_between(x_fill, 0, y_top, color='skyblue', alpha=0.35, label='ОДР')

# Целочисленная решетка внутри ОДР
for ix in range(8):
    for iy in range(12):
        if 8 * ix + 5 * iy <= 80 and 208 * ix + 505 * iy <= 5200:
            ax.plot(ix, iy, 'ko', markersize=4)

# Оптимальные точки и линии уровня
ax.plot(4.8, 8.32, 'bs', markersize=8, label='Непрерывный оптимум B(4.8; 8.32)')
ax.plot(5, 8, 'r*', markersize=14, label='Целочисленный оптимум (5; 8), Z=154')
ax.plot(x1, (156.16 - 10 * x1) / 13, 'k--', alpha=0.6, label='Z = 156.16')
ax.plot(x1, (154 - 10 * x1) / 13, 'r--', label='Z = 154')

# Вектор-градиент c = (10, 13) (в масштабе 1:4)
ax.arrow(0, 0, 2.5, 3.25, head_width=0.25, head_length=0.35, fc='darkorange', ec='darkorange', lw=2)
ax.text(2.6, 3.3, r'$\vec{c}=(10; 13)$', color='darkorange', fontsize=11)

ax.set_xlim(0, 11)
ax.set_ylim(0, 17)
ax.set_xticks(range(0, 12))
ax.set_yticks(range(0, 18))
ax.set_xlabel(r'$x_1$ (машины типа А)')
ax.set_ylabel(r'$x_2$ (машины типа Б)')
ax.set_title('Графическое решение задачи ЦЛП (Вариант 5)')
ax.grid(True, linestyle=':', alpha=0.7)
ax.legend(loc='upper right', fontsize=9)
plt.tight_layout()
plt.show()