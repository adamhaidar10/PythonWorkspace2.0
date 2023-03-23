from matplotlib import pyplot

# two lines representing data about GDP on the same graph

# years = [1960, 1970, 1980, 1990, 2000, 2010]
# gdpMalaysia = [1.92, 3.86, 24.49, 44.02, 93.79, 255.02]
# gdpSingapore = [0.70, 1.92, 11.89, 36.15, 95.83, 236.42]

# pyplot.plot(years, gdpMalaysia, color= "blue", marker= "x", linestyle= "solid")
# pyplot.plot(years, gdpSingapore, color="green", marker="x", linestyle="solid")

# pyplot.title("Malaysia GDP")
# pyplot.ylabel("$ Billions")
# pyplot.xlabel("Year")

# pyplot.show()

# countries = ["China", "India", "USA", "Indonesia", "Pakistan",
# "Brazil", "Nigeria", "Bangladesh", "Russia", "Mexico"]
# populations = [1401.5, 1359.3, 329.4, 265.0, 208.2, 211.2, 188.5, 168.2, 146.9, 126.6]

# pyplot.bar(range(len(countries)), populations)
# pyplot.xticks(range(len(countries)), countries)
# pyplot.title("Highest population countries")
# pyplot.ylabel("Millions")

# pyplot.show()


# plot that shows GDP from CSVfile = gdp_info.csv
# years = [2010, 2011, 2012, 2013, 2014, 2015, 2016]
# infile = open("gdp_info.csv")
# for line in infile:
#     linevalues = line.rstrip().split(",")
#     linelbl = linevalues[0]
#     linevalues.pop(0)
#     linevalues.reverse()
#     for i in range(0, len(linevalues)):
#         linevalues[i] = int(linevalues[i])
#     print(linevalues)
#     pyplot.plot(years, linevalues, linestyle="solid", label= linelbl)
#     pyplot.legend()
# pyplot.show()
# infile.close()

# scatter graph to show the states csv file


# names = []
# populations = []
# areas = []

# infile = open("states_info.csv")
# for line in infile:
#     # print(line)
#     linevalues = line.rstrip().split(",")
#     print(linevalues)
#     names.append(linevalues[0])
#     populations.append(int(linevalues[1]))
#     areas.append(int(linevalues[2]))

# infile.close()

# print(names)
# print(populations)
# print(areas)

# pyplot.scatter(areas, populations)

# for name, area, population in zip(names, areas, populations):
#     pyplot.annotate(name, xy=(area, population), xytext=(5, -5), textcoords="offset points")

# pyplot.xlabel("Area")
# pyplot.ylabel("Population")
# pyplot.title("Areas and populations of states of Malaysia")
# pyplot.show()

    
    

    

# Scatter plot

# widgets = [5, 7, 9, 13, 86, 103]
# gromits = [23, 38, 77, 102, 165, 198]
# labels = ["Alice", "Bob", "Carol", "Derek", "Ernie", "Fiona"]

# pyplot.scatter(widgets, gromits)

# for label, widget, gromit, in zip(labels, widgets, gromits):
#     pyplot.annotate(label, xy=(widget, gromit), xytext=(10, -10), textcoords="offset points")

# pyplot.xlabel("Widgets")
# pyplot.ylabel("Gromits")
# pyplot.title("Widgets and Gromits")
# pyplot.show() 

# 1
#x = [10.0, 8.0, 13.0, 9.0, 11.0, 14.0, 6.0, 4.0, 12.0, 7.0, 5.0]
#y = [8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68]

# 2
#x = [10.0, 8.0, 13.0, 9.0, 11.0, 14.0, 6.0, 4.0, 12.0, 7.0, 5.0]
#y = [9.14, 8.14, 8.74, 8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74]

# 3
x = [10.0, 8.0, 13.0, 9.0, 11.0, 14.0, 6.0, 4.0, 12.0, 7.0, 5.0]
y = [7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73]

# 4
#x = [8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 19.0, 8.0, 8.0, 8.0]
#y = [6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 12.50, 5.56, 7.91, 6.89]

pyplot.scatter(x, y)
pyplot.show()