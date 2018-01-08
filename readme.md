# Dog vs Cat Classifier

## Introduction

This project aims to build a deep learning model to classify the images of dogs and cats. 

**Motivation:** Using similar principle, different classifier could be trained and modeled for various use case.

 
## Usage:

Clone this project. Folders named train and test are already created here.
1. **extractData.py** : Downloads the data from the imagenet url and separates them into the train and test folder with label. Link has to be changed for each object to be downloaded from Imagenet.
2. **train.py**: Convolution Neural Network is implemented to train the model. The model is then tested using the test data. The train and test data are split here prior to start of training.


## DataSet:
Since the motivation of this project was to extend this classifier to be able to use in similar case scenario. Instead of downloading data from kaggle as in traditional approach. I decided to extract images from [Imagent.](http://www.image-net.org/). This enables in the future to get any images and train & test with this model.

For this project I decided to train only around 1000 images. Feel free to download more and play with more data or you can get started with the dataset from kaggle [here.](https://www.kaggle.com/c/dogs-vs-cats-redux-kernels-edition/data)

The training and testing data are included in this project. Start the project with

    python train.py

## Further
Because of the restriction in computation power in my system, I am planning to make use of Papersace train the model further. If you too do not have such huge computation power in the system, here is the [$10 in credit](https://www.paperspace.com/&R=56563PG) to get started. This will give a descent 10-20 hours of computational time. 

## Requirement

The basic knowledge of TensorFlow and Deep Learning was acquired from Tensorflow [Tutorial.](https://www.tensorflow.org/get_started/get_started) 
Also, if you wish to learn more follow [here.](https://pythonprogramming.net) 

## Result
With 1000 training data set , the accuracy of prediction is not quite good as shown in the figure. 
![](https://github.com/suraz09/deepLearningClassifier/blob/master/result.png)

But with the help of training the model using Paperspace, I believe we will achieve a descent predictive model. 
