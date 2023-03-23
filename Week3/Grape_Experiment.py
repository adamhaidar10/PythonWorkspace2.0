from matplotlib import pyplot

fruits = ["apples", "banana", "mangos", "pears", "peaches"]
quantities = [100,50,75,200,130]

#pyplot.plot(fruits, quantities, color="green", marker="x", linestyle="dotted")
pyplot.bar(fruits, quantities)


pyplot.title("Fruits")
pyplot.ylabel("Quantiy")
pyplot.xlabel("Fruit name")

pyplot.show()
