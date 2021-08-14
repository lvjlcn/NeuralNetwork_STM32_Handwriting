import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,Dropout,Convolution2D,MaxPooling2D,Flatten
from tensorflow.keras.optimizers import Adam,SGD
from tensorflow.keras.utils import to_categorical
import numpy as np

mnist = tf.keras.datasets.mnist
(x_train,y_train) ,(x_test,y_test)  = mnist.load_data()

x_train = x_train.reshape(x_train.shape[0],-1)/255
x_test = x_test.reshape(x_test.shape[0],-1)/255

y_train = to_categorical(y_train,num_classes=10)  # convert to one hot format
y_test = to_categorical(y_test,num_classes=10)

model = Sequential()

model.add(Dense(units=30,  #输出维度，表示有几个神经元
                input_dim=784, #输入尺寸
                activation='sigmoid',
                name='lay1'))

model.add(Dense(units=10,  #输出维度，表示有几个神经元
                activation='sigmoid',
                name='lay2'))


sgd = SGD(lr=0.2)
model.compile(
    optimizer='adam',
    loss = 'categorical_crossentropy',
    metrics= ['accuracy']
)

model.fit(x_train,y_train,batch_size=64,epochs=20)

loss,accuracy = model.evaluate(x_test,y_test)

print(loss)
print('accuracy',accuracy)

weight_Dense,bias_Dense = model.get_layer('lay1').get_weights()

np.savetxt('weight1.txt',weight_Dense,fmt='%.06f,')
np.savetxt('bias1.txt',bias_Dense,fmt='%.06f,')

# print(weight_Dense,bias_Dense)

weight_Dense,bias_Dense = model.get_layer('lay2').get_weights()
np.savetxt('weight2.txt',weight_Dense,fmt='%.06f,')
np.savetxt('bias2.txt',bias_Dense,fmt='%.06f,')
# print(weight_Dense,bias_Dense)

model.save('2lays.h5')