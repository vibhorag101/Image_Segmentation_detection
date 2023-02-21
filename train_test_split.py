import os
from sklearn.model_selection import train_test_split
import shutil

# Set the path to the directory containing images and labels
data_dir = ''


# do the following in batches of 1000 images
# Create the images and labels directories if they don't already exist

# Get a list of all image file names
images_length = len(os.listdir(os.path.join(data_dir, 'images')))
train_dir = os.path.join(data_dir, 'train')
test_dir = os.path.join(data_dir, 'test')
val_dir = os.path.join(data_dir, 'val')

train_dir_image = os.path.join(data_dir, 'train', 'images')
train_dir_labels = os.path.join(data_dir, 'train', 'labels')
test_dir_image = os.path.join(data_dir, 'test','images')
test_dir_labels = os.path.join(data_dir, 'test','labels')
val_dir_image = os.path.join(data_dir, 'val','images')
val_dir_labels = os.path.join(data_dir, 'val','labels')
os.makedirs(train_dir_image, exist_ok=True)
os.makedirs(train_dir_labels, exist_ok=True)
os.makedirs(test_dir_image, exist_ok=True)
os.makedirs(test_dir_labels, exist_ok=True)
os.makedirs(val_dir_image, exist_ok=True)
os.makedirs(val_dir_labels, exist_ok=True)
image_names = os.listdir(os.path.join(data_dir, 'images'))
train_names, rest_names = train_test_split(image_names, train_size=0.7, random_state=42)
val_names,test_names  = train_test_split(rest_names, train_size=0.7, random_state=42)
# Create the train and test directories if they don't already exist


# Move the image and label files to the train and test directories
for name in train_names:
    # Move the image file to the train directory
    src_path = os.path.join(data_dir, 'images', name)
    dst_path = os.path.join(train_dir,'images',name)
    shutil.move(src_path, dst_path)
    
    # Move the label file to the train directory
    src_path = os.path.join(data_dir, 'labels', name[:-4] + '.txt')
    dst_path = os.path.join(train_dir,'labels', name[:-4] + '.txt')
    shutil.move(src_path, dst_path)
    
for name in test_names:
    # Move the image file to the test directory
    src_path = os.path.join(data_dir, 'images', name)
    dst_path = os.path.join(test_dir,'images', name)
    shutil.move(src_path, dst_path)
    
    # Move the label file to the test directory
    src_path = os.path.join(data_dir, 'labels', name[:-4] + '.txt')
    dst_path = os.path.join(test_dir, 'labels',name[:-4] + '.txt')
    shutil.move(src_path, dst_path)


for name in val_names:
    # Move the image file to the test directory
    src_path = os.path.join(data_dir, 'images', name)
    dst_path = os.path.join(val_dir,'images', name)
    shutil.move(src_path, dst_path)
    
    # Move the label file to the test directory
    src_path = os.path.join(data_dir, 'labels', name[:-4] + '.txt')
    dst_path = os.path.join(val_dir, 'labels',name[:-4] + '.txt')
    shutil.move(src_path, dst_path)