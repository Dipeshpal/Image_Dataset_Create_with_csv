# This code will create classes folder according to CSV file
# It will read image name and its class from CSV file and create respected folder in "train" directory

# Import Libraries
import pandas as pd
import os
import shutil

# Get Current Working Directory
print(os.getcwd())

# Read CSV
df = pd.read_csv('labels.csv')

# Image Directory
image_dir = 'train'


def cpy(file, des):
    file = 'train/'+file
    des = 'train_120/'+des+"/"
    shutil.copy(file, des)
    print(file + ' copied to ' + des + ' successfully')


def create_dir(dir):
    path = 'train_120/' + dir
    try:
        os.mkdir(path)
    except OSError:
        print("Creation of the directory %s failed" % path)
    else:
        print("Successfully created the directory %s " % path)


def start(f):
    c = -1
    for i in df['id']:
        c += 1
        if f == i+'.jpg':
            dir = df['breed'][c]
            create_dir(dir)
            cpy(f, dir)


# Read files in
for root, dirs, files in os.walk(image_dir):
    for file in files:
        start(file)
        print(file)

