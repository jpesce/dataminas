import sys
import json
from sklearn.linear_model import Ridge
import numpy as np
import pylab

#sklearn.linear_model.LinearRegression(fit_intercept=True, normalize=False, copy_X=True)

   
data = json.load(open('sp501.json', 'r'))
data = json.load(open('vander.json', 'r'))

D = ['New York', 'Austin', 'San Francisco']
if len(sys.argv) < 2:
    dataset = D[0]
else: dataset = D[int(sys.argv[1])]

print 'Using', dataset

Y = []
for x in data:
    Y.append(x[dataset])

X = [i for i in xrange(1, len(Y)+1)]


deg = 3
'''
for degree in [deg]:
    ridge = Ridge()
    K = np.vander(X, degree)
    print 'shape', K.shape
    ridge.fit(np.vander(X, degree), Y)
    pylab.plot(X, ridge.predict(np.vander(X, degree)),
        label="degree %d" % degree)
'''

coefs = np.polyfit(X,Y,deg)

func = np.poly1d(coefs)
Y2 = [func(x) for x in X]
Z = [ Y[i]-Y2[i] for i in xrange(len(Y)) ]

std = np.std(Z)
mean = np.mean(Z)
print '%.15f'%mean, '%.10f'%std

outliers_x = [i for i, x in enumerate(Z) if (mean-std > x) or (mean+std < x)]
outliers_y = [Y[i] for i in outliers_x]

outliers_xx = [i for i, x in enumerate(Z) if (mean-std*2 > x) or (mean+std*2 < x)]
outliers_yy = [Y[i] for i in outliers_xx]



pylab.scatter(X, Y, color='black')
pylab.plot(X, Y2, color='purple')
pylab.title('%s(%d) #outliers = %d/%d'%(dataset, len(X), len(outliers_x), len(outliers_xx)))

pylab.scatter(outliers_x, outliers_y, color='orange')
pylab.scatter(outliers_xx, outliers_yy, color='red')

pylab.savefig('%s.png'%dataset)

