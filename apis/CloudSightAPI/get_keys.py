#!/opt/anaconda/bin/python

import json

def keys(fn):
  with open(fn) as fh:
    data = json.load(fh)
    for key in filter(lambda k: k not in ["errors"], data.keys()):
      yield key

if __name__ == '__main__':
  import argparse

  parser = argparse.ArgumentParser(description='Extract keys out of JSON.')
  parser.add_argument('filename', type=str)
  parser.add_argument('-l', '--aready-listed-file', type=str, default=None, dest='listed')

  args = parser.parse_args()
  fn = args.filename
  
  listed = []
  if 'listed' in args and args.listed:
    listedFN = args.listed
    with open(listedFN) as _fn:
      listed = json.load(_fn)['listed']

  print ("\n".join([ " * {}".format(key) for key in  keys(fn) if key not in listed ]))
