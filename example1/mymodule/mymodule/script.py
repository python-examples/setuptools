
from __future__ import print_function

def main():
   try:
      import requests
      print('requests is present. kudos!')
   except ImportError:
      raise RuntimeError('how the heck did you install this?')

