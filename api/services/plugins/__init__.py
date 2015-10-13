import os
from os import listdir
from os.path import isfile, join

current_path = os.path.dirname(os.path.realpath(__file__))

onlyfiles = [f.split('.')[0] for f in listdir(current_path) if
             isfile(join(current_path, f)) and f != '__init__.py' and not f.endswith('.pyc')]

__all__ = onlyfiles
