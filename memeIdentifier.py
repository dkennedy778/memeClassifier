#this class made with help from https://blog.keras.io/building-powerful-image-classification-models-using-very-little-data.html
from keras.preprocessing.image import ImageDataGenerator, array_to_img,img_to_array,load_img
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
import numpy as np
import os

#sample datagen which does the following
#1.Randomly rotating the image within 40 degrees of the origin
#2.randomly translating the images horizontally and vertically by at most 20%
#3.scaling the models by a 1/255. factor to make it easier for our model to process, traditional RGB coefficents in the 0-255 range are too high for the model to process in a resonable amount of time
#4. Randomly applying a range of shearing transformations https://en.wikipedia.org/wiki/Shear_mapping
#5.randomly zooming the picture by up to 20%
#6. sometimes flipping the picture horizontally (are meme's assymetric?)
#7. Filling in pixels created after a rotation or width/height shift

datagen = ImageDataGenerator(rotation_range=40,width_shift_range=.2,height_shift_range=.2,rescale=1./255,shear_range=.2,zoom_range=.2,horizontal_flip=True,fill_mode='nearest')

#sample permutation code, the implemented generators handle this automatically 
#inputDir = ""
# for image in os.listdir(inputDir):
#     load the image
    # img = load_img(image)
    # x = img_to_array(img)
    # x = x.reshape((1,) + x.shape)

    #randomly transform the image and output it to a save directory
    # i = 0
    # for batch in datagen.flow(x, batch_size=1,save_to_dir='sampleMemePermutations',save_prefix=image + 'perm',save_format='jpeg'):
    #     i+=1
        #making 20 permutations
        # if i > 20:
        #     break
    #Now 1 data point has become 20!

model = Sequential()
model.add(Conv2D(32, (3, 3), input_shape=(150, 150,3)))
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

# this is the augmentation configuration we will use for training
train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)

# this is the augmentation configuration we will use for testing:
# only rescaling
test_datagen = ImageDataGenerator(rescale=1./255)
try:
# this is a generator that will read pictures found in
# subfolers of 'data/train', and indefinitely generate
# batches of augmented image data

#Input your source directories here 
    train_generator = train_datagen.flow_from_directory(
       '',  # this is the target directory
        target_size=(150, 150),  # all images will be resized to 150x150
        batch_size=batch_size,
        class_mode='binary')  # since we use binary_crossentropy loss, we need binary labels

# this is a similar generator, for validation data
    validation_generator = test_datagen.flow_from_directory(
        '',
        target_size=(150, 150),
        batch_size=batch_size,
        class_mode='binary')
    model.fit_generator(
        train_generator,
        steps_per_epoch=2000 // batch_size,
        epochs=50,
        validation_data=validation_generator,
        validation_steps=800 // batch_size)
    model.save_weights('first_try.h5')  # always save your weights after training or during training
except Exception as e:
    print ("error", e)
