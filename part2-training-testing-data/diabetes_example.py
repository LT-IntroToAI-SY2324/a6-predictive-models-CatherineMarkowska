import matplotlib.pyplot as plt 
import numpy as np 

from sklearn import datasets, linear_model 
from sklearn.metrics import mean_squared_error, r2_score 
from sklearn.model_selection import train_test_split

#Load the dataset 
x, y = datasets.load_diabetes(return_X_y=True)
x = x[:, np.newaxis, 2]

xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size = .2)
# print(f"x {x}")
# print(f"y {y}")
# print(f"xtrain {xtrain}")
# print(f"xtest {xtest}")
# print(f"ytrain {ytrain}")
# print(f"ytest {ytest}")

model = linear_model.LinearRegression().fit(xtrain, ytrain)

coef = round(float(model.coef_), 2)
intercept = round(float(model.intercept_), 2)

print(coef, intercept)

prediction = model.predict(xtest)

print(f"Coefficient: {coef}")
print(f"Mean squared error: {mean_squared_error(ytest, prediction)}")
print(f"Coefficient of determination: {r2_score(ytest, prediction)}")

# plot the points 
plt.scatter(xtest, ytest, c="pink")
plt.scatter(xtrain, ytrain, c="purple")
plt.plot(xtest, ytrain, coef*xtest + intercept, c="blue", linewidth = 3)

plt.legend()
plt.xticks()
plt.yticks()
plt.show()
