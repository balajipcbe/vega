from PIL import Image
import imagehash
import argparse
import shelve
import glob


ap = argparse.ArgumentParser()
ap.add_argument("-d","--dataset",required=True,
                help="path to input datasets")
ap.add_argument("-s","--shelve",required=True,
                help="output shelve database")
args = vars(ap.parse_args())

db = shelve.open(args["shelve"], writeback=True)

for imagePath in glob.glob(args["dataset"]+"/*.jp*g"):
    print(imagePath)
    image = Image.open(imagePath)
    h = str(imagehash.dhash(image))
    filename = imagePath[imagePath.rfind("/")+1:]
    db[h] = db.get(h,[]) + [filename]

for key in db.keys():
    if len(db[key]) > 1:
        print(db[key])
db.close()
