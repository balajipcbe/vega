import os
import glob

for filename in glob.glob('*.JPG'):
    os.rename(filename,filename.lower())
