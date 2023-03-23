from matplotlib import pyplot as plt

infile = open("Week2\datadata.csv")

fig, axs = plt.subplots(2, 2)

for line in infile:
    linevalues = line.rstrip().split(",")
    print(line)
    x1 = float(linevalues[0])
    y1 = float(linevalues[1])
    x2 = float(linevalues[2])
    y2 = float(linevalues[3])
    x3 = float(linevalues[4])
    y3 = float(linevalues[5])
    x4 = float(linevalues[6])
    y4 = float(linevalues[7])

    axs[0,0].scatter(x1,y1)
    axs[0,0].set_title('Data 1')
    axs[0,1].scatter(x2, y2)
    axs[0,1].set_title('Data 2')
    axs[1,0].scatter(x3,y3)
    axs[1,0].set_title('Data 3')
    axs[1,1].scatter(x4, y4)
    axs[1,1].set_title('Data 4')
    
plt.show()

infile.close()
