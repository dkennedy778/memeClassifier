# memeClassifier
a ML algorithm which determines if images are memes or not

This project using a machine learning process sourced from [keras's blog](https://blog.keras.io/building-powerful-image-classification-models-using-very-little-data.html) to determine if images are memes or not. 
The long term goals of the project is to derive a ML algorithim that can detect memes with a success rate of over 95%, and then use an OCR algorithim on a large dataset of memes to analyze the characteristics of their text.

The project presents a significant classification problem. What constitutes a meme? Browsing a modern repository like [/r/dankmemes](https://www.reddit.com/r/dankmemes/) will present a user with a dizzying array of image
and text formats. Gathering, classifying, and pruning a comphrensive meme dataset is a signficant challenge.

To form my dataset, I used a lightly modified version of [hardikvava's google image downloader](https://github.com/hardikvasa/google-images-download) to gather 10,000 "meme-like" images from google. I then pruned these images by hand
to form an inital dataset of representative memes. As of now, I am only analyzing memes which follow the classic [top text bottom text](https://imgflip.com/memegenerator) style. Please message me if you'd like a copy of the dataset.

I am currently seeking out larger, more comphrensive meme datasets. Ideally these would not require extensive human modification, and represent a wide array of meme types and styles.  





