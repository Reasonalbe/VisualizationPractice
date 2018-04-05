import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]
imput_values = [1, 2, 3, 4, 5]
plt.plot(imput_values, squares, linewidth=5)
plt.title("Square Numbers", fontsize=24)
plt.xlabel("value", fontsize=14)
plt.ylabel("square of value", fontsize=14)
plt.tick_params(axis='both', labelsize=14)

plt.show()