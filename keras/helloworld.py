# Import package
import numpy as np
np.random.seed(1337)
from keras.models import Sequential
from keras.layers import Dense
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# 1.Build the trainning data
X=np.linspace(-1,1,200)
np.random.shuffle(X)
np.random.normal()
Y=0.5*X+2+np.random.normal(0,0.05,(200,))
plt.scatter(X,Y)
plt.show()
X_train,Y_train=X[:160],Y[:160]
X_test,Y_test=X[160:],Y[160:]
print(X)
print("*******************************************")
print(Y)

# 2.Build a neural network from the 1st layer to the last layer
model=Sequential()
model.add(Dense(output_dim=1,input_dim=1))

#3. Choose loss function and optimzing method
model.compile(loss='mse',optimizer='sgd')

#4. Trainning
print("Training......")
for step in range(1400):
        cost=model.train_on_batch(X_train,Y_train)
        if step % 100 ==0:
                print('train cost',cost)
#5.Test
print("\n Testing...........")
cost=model.evaluate(X_test,Y_test,batch_size=40)
print("Test cost:",cost)
W,b=model.layers[0].get_weights()
print('Weight=',W,"\nbiases=",b)

#6.Plotting the prediction
Y_pred=model.predict(X_test)
plt.scatter(X_test,Y_test)
plt.plot(X_test,Y_pred)
plt.show()
