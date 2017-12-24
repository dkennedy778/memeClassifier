#this class made with help from https://blog.keras.io/building-powerful-image-classification-models-using-very-little-data.html
from keras.preprocessing.image import ImageDataGenerator, array_to_img,img_to_array,load_img
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
import numpy as np

#first we create a datagenerator that'll randomly modify our samples to diversify our limited sample of images, here we are doing the following
#1.Randomly rotating the image within 40 degrees of the origin
#2.randomly translating the images horizontally and vertically by at most 20%
#3.scaling the models by a 1/255. factor to make it easier for our model to process, traditional RGB coefficents in the 0-255 range are too high for the model to process in a resonable amount of time
#4. Randomly applying a range of shearing transformations https://en.wikipedia.org/wiki/Shear_mapping
#5.randomly zooming the picture by up to 20%
#6. sometimes flipping the picture horizontally (are meme's assymetric?)
#7. Filling in pixels created after a rotation or width/height shift

datagen = ImageDataGenerator(rotation_range=40,width_shift_range=.2,height_shift_range=.2,rescale=1./255,shear_range=.2,zoom_range=.2,horizontal_flip=True,fill_mode='nearest')

#load the image
img = load_img('dog_meme.jpg')
x = img_to_array(img)
x = x.reshape((1,) + x.shape)

#randomly transform the image and output it to a save directory
i = 0
for batch in datagen.flow(x, batch_size=1,save_to_dir='sampleMemePermutations',save_prefix='dogMeme',save_format='jpeg'):
    i+=1
    #making 20 permutations
    if i > 20:
        break
#Now 1 data point has become 20!

#Using 3 convolution layers here
model = Sequential()
model.add(Conv2D(32, (3, 3), input_shape=(3, 150, 150)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(32, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(64, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())  # this converts our 3D feature maps to 1D feature vectors
model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(1))
model.add(Activation('sigmoid'))

model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

batch_size = 16

generator = datagen.flow_from_directory(
        'data/train',
        target_size=(150, 150),
        batch_size=batch_size,
        class_mode=None,  # this means our generator will only yield batches of data, no labels
        shuffle=False)  # our data will be in order, so all first 1000 images will be cats, then 1000 dogs
# the predict_generator method returns the output of a model, given
# a generator that yields batches of numpy data
bottleneck_features_train = model.predict_generator(generator, 2000)
# save the output as a Numpy array
np.save(open('bottleneck_features_train.npy', 'w'), bottleneck_features_train)

generator = datagen.flow_from_directory(
        'data/validation',
        target_size=(150, 150),
        batch_size=batch_size,
        class_mode=None,
        shuffle=False)
bottleneck_features_validation = model.predict_generator(generator, 800)
np.save(open('bottleneck_features_validation.npy', 'w'), bottleneck_features_validation)

train_data = np.load(open('bottleneck_features_train.npy'))
# the features were saved in order, so recreating the labels is easy
train_labels = np.array([0] * 1000 + [1] * 1000)

validation_data = np.load(open('bottleneck_features_validation.npy'))
validation_labels = np.array([0] * 400 + [1] * 400)

model = Sequential()
model.add(Flatten(input_shape=train_data.shape[1:]))
model.add(Dense(256, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(1, activation='sigmoid'))

model.compile(optimizer='rmsprop',
              loss='binary_crossentropy',
              metrics=['accuracy'])

model.fit(train_data, train_labels,
          epochs=50,
          batch_size=batch_size,
          validation_data=(validation_data, validation_labels))
model.save_weights('bottleneck_fc_model.h5')