from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Dense
from keras.layers import Flatten
from keras.preprocessing.image import ImageDataGenerator

import tensorflow as tf

#initialise the CNN
classifier = Sequential()

#step 1 - convolution
classifier.add(Convolution2D(filters = 32, kernel_size = (3, 3), input_shape = (64, 64, 3), activation='relu'))

#step 2 - max pooling
classifier.add(MaxPooling2D(pool_size=(2, 2)))

#another convolution layer
#classifier.add(Convolution2D(filters=32, kernel_size=(3, 3), input_shape = ))

#flattening
classifier.add(Flatten())

#full connection
classifier.add(Dense(units = 128, activation = 'relu'))
classifier.add(Dense(units = 5, activation = 'sigmoid'))

#compile CNN
classifier.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'] )

#pre
train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1./255)

training_set = train_datagen.flow_from_directory('Dataset/train',
                                                    target_size=(64, 64),
                                                    batch_size=32,
                                                    class_mode='categorical')

test_set = test_datagen.flow_from_directory('Dataset/test',
                                                        target_size=(150, 150),
                                                        batch_size=32,
                                                        class_mode='categorical')

classifier.fit_generator(training_set,
                         steps_per_epoch=4000,
                         epochs=25,
                         validation_data=test_set,
                         validation_steps=10)
