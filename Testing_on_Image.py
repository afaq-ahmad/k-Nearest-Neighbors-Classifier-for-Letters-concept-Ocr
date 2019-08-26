testing_files=['testing\\shazam.png']
print ('Testing on: ',testing_files[0])
import numpy as np
import os
import scipy.ndimage
from sklearn.neighbors import KNeighborsClassifier
import scipy
import glob
import time
from scipy.misc import imread,imsave
from Extract_Letters_from_Image import Extract_Letters

from sklearn.externals import joblib


print ('Loading the Trained Knn model from (model) directory')
knn = joblib.load('models/knn_model.model')


print ('Converting the Testing Image to Character Imgaes')

start_time = time.time()
extract = Extract_Letters()

# testing_files=glob.glob('testing/*.png')

name_counter = 0
for files in testing_files:
    files=files.replace('\\','/')
    letters = extract.extractFile(files)
        
    for i in letters:
        directory='testing_characters_images'
        if not os.path.exists(directory):
            os.makedirs(directory)
        
        imsave('testing_characters_images/' + str(name_counter) + '_test.png', i)
        name_counter += 1


print ('Reading the ground Truth file from Testing directory')
testing_files[0].replace('.png','_ground_truth.txt')
ground_truth_dir=testing_files[0].replace('.png','_ground_truth.txt').replace('\\','/')
with open(ground_truth_dir,'r',encoding="utf8") as f:
    text_Data=f.read()
text_Data=text_Data.replace('\n','').replace('.','').replace(',','').replace('“','').replace(' ','').replace('”','').replace('’','').replace(')','').replace('(','').replace('‘','').replace('-','')
ground_truth=list(map(str, text_Data))


test_chr_folders_images=glob.glob('testing_characters_images/*.png')
features_list = []
for filename in (test_chr_folders_images):
    
    if (filename.endswith('.png')):
        test_digit_image = scipy.misc.imread(filename)

        features_list.append(test_digit_image.reshape(-1,))
features_list=np.array(features_list)
print ('Knn score(PREDICTED VS Ground Truth): ',knn.score(features_list,np.array(ground_truth)[:len(features_list)]))

predicted_output=knn.predict(features_list)
output_prediction=' '.join(list(predicted_output))
print ('Predicted Text: ')
print (output_prediction)

print (time.time() - start_time, "seconds" )