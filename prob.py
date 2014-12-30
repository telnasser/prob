# Write a script called "prob.py" that outputs frequencies, as well as creates and saves a boxplot, a histogram, 
# and a QQ-plot for the data in this lesson. 

import collections
import matplotlib.pyplot as plt
import numpy as np 
import scipy.stats as stats

x = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]
c = collections.Counter(x)
print c

# calculate the number of instances in the list
count_sum = sum(c.values())

for k,v in c.iteritems():
  print "The frequency of number " + str(k) + " is " + str(float(v) / count_sum)

plt.boxplot(x)

# This will save the plot to a png file that you may load later on!
# You call it on the plt object and pass in the filename you wish to use

plt.savefig("boxplot.png")
plt.show()

plt.hist(x, histtype='bar')
plt.savefig("histogram-plot.png")
plt.show()



plt.figure()
graph1 = stats.probplot(x, dist="norm", plot=plt)
plt.savefig("qq-plot.png")
plt.show() #this will generate the first graph
