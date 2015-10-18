#!/opt/anaconda/bin/python

from cloudsight import postImage, getDescription

MAX_ATTEMPTS = 5
TIMEOUT_FETCH = 5
TIMEOUT_VERIFY = 5

def runExperiment(interval, url, logfile):
  import json

  from datetime import datetime
  from time import sleep

  descriptions = {}
  descriptions['errors'] = []

  while True:
    startTime = datetime.now()
    print ("TICK! Checking potatoes...")
    token = postImage(url)

    attempt = 0
    description = None
    print ("Fetching description. {} attempts in {}s intervals.".format(MAX_ATTEMPTS, TIMEOUT_FETCH))
    while not description and attempt < MAX_ATTEMPTS:
      sleep(TIMEOUT_FETCH)
      print ("{} attempt to fetch result...".format(attempt))
      attempt += 1
      description = getDescription(token)
      when = str(datetime.now())
      print ("{} @ {}".format(description, when))

    print (" * Veryfing that data assigned to returned token is immutable in {}s intervals...".format(TIMEOUT_VERIFY))
    desc_unique = set([description])
    for i in range(4):
      sleep(TIMEOUT_VERIFY)
      print ("{} fetch.".format(i))
      descu = getDescription(token)
      desc_unique.add(descu)

    if len(desc_unique) > 1:
      print ("!! Got different descriptions out of one token: {}".format(desc_unique))
      descriptions['errors'].append((description, str(desc_unique)))
    
    if description in descriptions:
      descriptions[description].append(when)
    else:
      descriptions[description] = [when]

    with open(logfile, 'w+') as fh:
      print ("Updating file...")
      fh.write(json.dumps(descriptions))

    print ("Sleeping... zzz.... hrrrr.... zzzz....")

    delta = (datetime.now() - startTime).seconds
    snooze = interval - delta

    if snooze > 0:
      print ("Work took {}s. Sleeping for {}s... (interval is {}s)".format(delta, snooze, interval))
      sleep(snooze)

if __name__ == "__main__":
  import argparse

  parser = argparse.ArgumentParser(description='Run experiment on URL collecting all different descriptions of the same picture.')
  parser.add_argument('-i', '--interval', type=float, help='time interval in minutes', default=1.0, dest='interval')
  parser.add_argument('-u', '--url', type=str, help='image URL', default='https://upload.wikimedia.org/wikipedia/commons/a/ab/Patates.jpg', dest='url'
)
  parser.add_argument('-o', '--output', type=str, help='file to save output to', default=None, dest='log')

  args = parser.parse_args()

  url = args.url.strip()
  interval = int(args.interval * 60.0) # to seconds
  log = args.log

  if not log:
    log = "potato_experiment.json"

  import os
  def getLogName(i):
    return "potato_experiment.json.{}".format(i)

  i = 0

  while os.path.exists(getLogName(i)):
    i += 1

  log = getLogName(i)
  print ("Saving log to {}.".format(log))

  runExperiment(interval, url, log)
