#!/opt/anaconda/bin/python

from cloudsight import postImage, getDescription

def runExperiment(interval, url, logfile):
  import json

  from datetime import datetime
  from time import sleep

  descriptions = {}

  while True:
    print ("TICK! Checking potatoes...")
    token = postImage(url)
    description = getDescription(token)
    when = str(datetime.now())
    print ("{} @ {}".format(description, when))

    if description in descriptions:
      descriptions[description].append(when)
    else:
      descriptions[description] = [when]

    with open(logfile, 'w+') as fh:
      print ("Updating file...")
      fh.write(json.dumps(descriptions))

    print ("Sleeping... zzz.... hrrrr.... zzzz....")
    sleep(interval)

if __name__ == "__main__":
  import argparse

  parser = argparse.ArgumentParser(description='Run experiment on URL collecting all different descriptions of the same picture.')
  parser.add_argument('interval', type=int, help='time interval in minutes')
  parser.add_argument('url', type=str, help='image URL')
  parser.add_argument('log', type=str, help='file to save output to')

  args = parser.parse_args()

  url = args.url.strip()
  interval = args.interval * 60 # to seconds
  log = args.log

  runExperiment(interval, url, log)
