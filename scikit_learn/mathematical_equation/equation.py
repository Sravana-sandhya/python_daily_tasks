#----------eq:7a+3b+4c+9d----------------

from random import randint
from sklearn.linear_model import LinearRegression
#Training data settings
TRAIN_SET_LIMIT = 1000
TRAIN_SET_COUNT = 100
#empty list
TRAIN_INPUT = []
TRAIN_OUTPUT = []
#Generate training data
for i in range(TRAIN_SET_COUNT):
    a = randint(0, TRAIN_SET_LIMIT)
    b = randint(0, TRAIN_SET_LIMIT)
    c = randint(0, TRAIN_SET_LIMIT)
    d = randint(0, TRAIN_SET_LIMIT)
    y = (7*a) + (3*b) + (4*c) + (9*d)
    TRAIN_INPUT.append([a, b, c, d])
    TRAIN_OUTPUT.append(y)
#create and train model
model = LinearRegression(n_jobs=-1)
model.fit(TRAIN_INPUT, TRAIN_OUTPUT)
#test data
X_TEST = [[10, 20, 30, 40]]
# prediction
outcome = model.predict(X_TEST)
coefficients = model.coef_
print('Outcome : {}\nCoefficients : {}'.format(outcome, coefficients))
