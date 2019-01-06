import tensorflow as tf

mnist = tf.keras.datasets.mnist # 28x28 images of handwritten digits 0-9
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train = tf.keras.utils.normalize(x_train, axis=1).reshape(x_train[0].shape[0], -1)
x_test = tf.keras.utils.normalize(x_test, axis=1).reshape(x_test[0].shape[0], -1)

model = tf.keras.models.Sequential()
#model.add(tf.keras.layers.Flatten(input_shape=x_train[0].shape)) # flatten it 
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu)) # layer1
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu)) # layer2
# 10 -> the number of classifications, softmax -> probability distribution
model.add(tf.keras.layers.Dense(10, activation=tf.nn.softmax)) # output layers 

model.compile(optimizer='adam', 
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
model.fit(x_train, y_train, epochs=3)

val_loss, val_acc = model.evaluate(x_test, y_test)
print(val_loss, val_acc)


model.save('epic_num_reader.model')
new_model = tf.keras.models.load_model('epic_num_reader.model')
predictions = new_model.predict([x_test])

import numpy as np
import matplotlib.pyplot as plt
print(np.argmax(predictions[0]))
plt.imshow(x_test[0])
plt.show()







#plt.imshow(x_train[0], cmap = plt.cm.binary)
#plt.show()
#print(x_train[0])
