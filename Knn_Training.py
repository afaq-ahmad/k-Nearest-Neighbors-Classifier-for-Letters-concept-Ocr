import numpy as np
import os
import scipy.ndimage
from sklearn.neighbors import KNeighborsClassifier
from sklearn.externals import joblib
import glob
tr_data_dir='training_characters_images'

data_folders=glob.glob(tr_data_dir+'/*')

print ('Loading data from directory: ',tr_data_dir)

features_list = []
features_label = []
# load labeled training / test data
# loop over the 10 directories where each directory stores the images of a digit
for digit in range(len(data_folders)):
    label = data_folders[digit].split('\\')[1]
    for filename in os.listdir(data_folders[digit]):
        if (filename.endswith('.png')):
            training_digit_image = scipy.misc.imread(data_folders[digit]+'/' + filename)

            features_list.append(training_digit_image.reshape(-1,))
            features_label.append(label)
features_list=np.array(features_list)
features_label=np.array(features_label)

n_neighbors=3

print ('Training Knn on Nearest Neighbors Numbers: ' ,n_neighbors)
knn = KNeighborsClassifier(n_neighbors=n_neighbors)
knn.fit(features_list, features_label)


# save trained model
print ('Saving the Trained Model')
if not os.path.exists('models'):
    os.makedirs('models')
joblib.dump(knn, 'models/knn_model.model')