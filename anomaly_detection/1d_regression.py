
import json
from sklearn import linear_model
import numpy as np
import pylab

#sklearn.linear_model.LinearRegression(fit_intercept=True, normalize=False, copy_X=True)

   
data = json.load(open('sp501.json', 'r'))
Y = []
for x in data:
    Y.append([x['price']])

X = [[i] for i in xrange(1, len(Y)+1)]

model = linear_model.LinearRegression()
model.fit(X,Y)

print 'coeficientes', model.coef_, model.intercept_

pylab.scatter(X, Y, color='black')
pylab.plot(X, model.predict(X), color='red')

pylab.show()

