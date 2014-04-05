'''
Created on Apr 5, 2014

@author: hkr (elbauldelprogramador.com)

Licensed under GPLv3
'''

#!/usr/bin/env python

from distutils.core import setup

setup( name='GenPlaylistByLength',
    version='1.0',
    description='Generate playlist of mp3 and mp4 files of a length given',
    author='Alejandro Alcalde',
    author_email='',
    url='http://elbauldelprogramador.com/',
    requires=['mutagen'],
    packages=['playlistGenerator']
)