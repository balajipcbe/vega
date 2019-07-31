from PIL import Image
import imagehash
import argparse
import shelve

ap = argparse.ArgumentParser()
ap.add_argument("-d","--dataset",required=True,
                help = "path to dataset of images")
ap.add_argument("-s","--shelve", required=True,
                help = "output shelve database")
ap.add_argument("-q", "--query", required=True,
                help = "path to the query Image")
args =  vars(ap.parse_args())

db = shelve.open(args["shelve"])
query = Image.open(args["query"])
h = str(imagehash.dhash(query))

#filenames = db.get(h)
for key in db.keys():
    if len(db[key]) > 1:
        print(db[key])
#if filenames:
#    print("Found images", len(filenames))
#    for filename in filenames:
#        image = Image.open(args["dataset"]+"/"+filename)
#        image.show()
#else:
#    print('image not found')
db.close()
