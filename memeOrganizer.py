#Small script to rename and collect all memes into a superfile.
# The scraper will put memes into unique folders with 100 pictures each. For ease of use this script just gives all of those images unique identifiers and collects
# them into one file. This functionality will later be implemented directly into the parser, after which this script will be deprecated
import os
import shutil
import random


# loop for organizing decentralized meme results (sub folders of 100 images)
def organizeDecentralizedMemes():
    i = 0
    for folder in os.listdir(directory):
        for picture in os.listdir(directory + folder):
            oldDir = directory + folder + '/' + picture
            shutil.move(oldDir, newDir + picture + str(i) + ".jpg") #Formatting of the name doesn't matter, just need to be able to shunt them all off to the same folder
        i = i + 1

#loop for organizing a centralized repository of meme result (one folder of n size). Image results are organized on search but we don't want the ML algorithim to see a restricted data set
def organizeCentralizedMemes():
    i = 0
    for picture in os.listdir(directory):
        random_filename = random.choice([
                                            x for x in os.listdir(directory)
                                            if os.path.isfile(os.path.join(directory, x))
                                            ])
        shutil.move(directory + random_filename, newDir +random_filename)  # Formatting of the name doesn't matter, just need to be able to shunt them all off to the same folder
        i = i + 1

#input directories here 
directory = ('')
newDir = ''
organizeCentralizedMemes()
