import os
import glob
import time
from scipy.misc import imread,imsave
from skimage.segmentation import clear_border
from Extract_Letters_from_Image import Extract_Letters

start_time = time.time()
extract = Extract_Letters()

training_files=glob.glob('training/*.png')

folder_string = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz123456789'
name_counter = 600
for files in training_files:
    files=files.replace('\\','/')
    letters = extract.extractFile(files)
    
    string_counter = 0
    
    for i in letters:
        if string_counter > 60:
            string_counter = 0
        directory='training_characters_images/' + str(folder_string[string_counter])
        if not os.path.exists(directory):
            os.makedirs(directory)
        imsave('training_characters_images/' + str(folder_string[string_counter]) + '/' + str(name_counter) + '_snippet.png', i)
        string_counter += 1
        name_counter += 1
print (time.time() - start_time, "seconds" )