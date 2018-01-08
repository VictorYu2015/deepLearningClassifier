import tensorflow as tf 
import pandas as pd 
import urllib
import wget
import requests
import urllib.request
import cv2
import os
import numpy as np 

REQUIRED = 1000
IMG_SIZE = 50

def download_images(url, type, label):
	start = 1
	end = int(.8 * REQUIRED)
	count = 1
	folder = 'train/'

	if type == 'test':
		start = end
		end = REQUIRED
		folder = 'test/'

	for i in range(start, end):
		try:
			fileName = folder + label + str(count) + '.jpg'
			print("downloading %s" % (url[i]))
			urllib.request.urlretrieve(url[i], fileName)
			img = cv2.imread(fileName,cv2.IMREAD_GRAYSCALE)
			resized_image = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
			cv2.imwrite(fileName, resized_image)
			count += 1
		except Exception as e:
			print(str(e))

def find_uglies(folder):
	folder = 'train'
	match = False
	if(folder == 'test'):
		folder = 'test'
	for file_type in ['test']:
		for img in os.listdir(file_type):
			for ugly in os.listdir('uglies'):
				try:
					current_image_path = str(file_type) + '/' + str(img)
					ugly = cv2.imread('uglies/' + str(ugly))
					question = cv2.imread(current_image_path)
					if ugly.shape == question.shape and not(np.bitwise_xor(ugly,question).any()):
						print('That is one ugly pic! Deleting!')
						print(current_image_path)
						os.remove(current_image_path)
				except Exception as e:
					print(str(e))

link = 'http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n02101006'
link = 'http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n02123159'
url = urllib.request.urlopen(link).read().decode().split('\n')
label = 'cat'
download_images(url , 'train', label)
download_images(url, 'test', label)
find_uglies('train')
find_uglies('test')
