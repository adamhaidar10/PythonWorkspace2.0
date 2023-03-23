from matplotlib import pyplot as plt

years = [2010, 2011, 2012, 2013, 2014, 2015, 2016]

infile = open("Week2\gdp_info_copy.csv")
states = []
populations = []
areas = []


for line in infile:
    linevalues = line.rstrip().split(",")
    state = linevalues[0]
    #states.append(state)
    population = int(linevalues[1])
    #populations.append(population)
    area = int(linevalues[2])
    #areas.append(area)
    plt.scatter(population, area)

    #plt.legend()

plt.show()
infile.close()