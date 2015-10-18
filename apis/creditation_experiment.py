#!/opt/anaconda/bin/python

from cloudsight import postImage, getDescription

PULLS = 50

def runExperiment(url):
  import json

  from datetime import datetime
  from time import sleep

  descriptions = {}
  descriptions['errors'] = []

  print ("Submitting request for {}...".format(url))
  token = postImage(url)

  print ("Starting fetching results from the image (the total request remaining should be 1 less and not the number of pulls set to {}...".format(PULLS))    
  for i in range(PULLS):
    print ("Fetch: {}.".format(i))
    description = getDescription(token)
    print ("Recieved description: {}".format(description))

  print ("Finished the experiment.")

if __name__ == "__main__":
  import argparse

  parser = argparse.ArgumentParser(description='Run experiment on URL collecting all different descriptions of the same picture.')
  parser.add_argument('-u', '--url', type=str, help='image URL', default='https://upload.wikimedia.org/wikipedia/commons/a/ab/Patates.jpg', dest='url'
)

  args = parser.parse_args()

  url = args.url.strip()

  runExperiment(url)
