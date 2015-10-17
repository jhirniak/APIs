#!/opt/anaconda/bin/python

"""
Usage: pass url as command line argument
Output: CloudSightAPI description of the item in the picture

Example:
  * zimnoki - https://upload.wikimedia.org/wikipedia/commons/a/ab/Patates.jpg
"""

def postImage(picurl, geoloc=None, focus=None, lang='en', locale='en_GB'):
  import json
  import urllib.parse
  import urllib.request

  print ('Processing image from {}...'.format(picurl))

  url = 'http://api.cloudsightapi.com/image_requests'

  headers = {
    'Authorization': 'CloudSight uDm0TK41qU9LS1zkrrxMVw',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': 'application/json'
  }

  data = {
    'image_request[remote_image_url]': picurl,
    'image_request[language]': lang,
    'image_request[locale]': locale
  }

  if (geoloc):
    data['image_request[altitude]'] = geoloc.altitude
    data['image_request[latitude]'] = geoloc.latitude
    data['image_request[longitude]'] = geloc.longitue

  if (focus):
    data['focus[x]'] = focus.x
    data['focus[y]'] = focus.y

  data = urllib.parse.urlencode(data).encode('utf-8')

  req = urllib.request.Request(url, data=data, headers=headers)

  response = urllib.request.urlopen(req)

  return json.loads(response.read().decode('utf-8'))['token']

def getDescription(token):
  import json
  import urllib.parse
  import urllib.request

  url = 'https://api.cloudsightapi.com/image_responses/{}'.format(token)

  headers = {
    'Authorization': 'CloudSight uDm0TK41qU9LS1zkrrxMVw'
  }

  req = urllib.request.Request(url, headers=headers)

  response = urllib.request.urlopen(req)

  desc = json.loads(response.read().decode('utf-8'))

  if desc['name']:
    return desc['name']

if __name__ == "__main__":
  import argparse

  parser = argparse.ArgumentParser(description='Return description for image specified in URL using CloudSightAPI.')
  parser.add_argument('url', type=str, help='Image URL')
  
  args = parser.parse_args()

  imageUrl = args.url.strip()

  token = postImage(imageUrl)

  desc = getDescription(token)

  print ('Image description: {}'.format(desc))

