#!/usr/bin/env python

'''
Created on Apr 4, 2014

@author: Alejandro Alcalde

Licensed under GPLv3
'''

import argparse
import fnmatch

from mutagen.mp3 import MP3
from mutagen.mp4 import MP4

from os.path import os, basename
from sys import argv
from random import shuffle

def main():

    parser = argparse.ArgumentParser(description='Generate playlists with the indicated length')
    parser.add_argument('-d','--directory', help='Directory with music files',type=str, required=True)
    parser.add_argument('-l', '--length', help='Length of the playlist, in minutes', type=int, required=True)

    args = parser.parse_args()

    directory = args.directory
    length =  args.length * 60


    path = r'./playlists/'
    if not os.path.exists(path): os.makedirs(path)

    playlist_basename = basename(argv[0][:-3]) + str(length/60) + '_'
    playlist_number = 1
    curr_length = 0
    curr_items = []
    too_long_items = []
    all_items = []

    for music_file in os.listdir(directory):
        if fnmatch.fnmatch(music_file, '*.mp[43]'):
            all_items.append(directory + music_file)
    
    shuffle(all_items)
    
    for item in all_items:
        if curr_length >= length:
            name = path + playlist_basename + str(playlist_number) + '.m3u'
            playlist_file = open(name, 'w')
            playlist_file.writelines(curr_items)
            playlist_file.close()
            print 'Playlist generated, name: ', name , ' length ', curr_length/60 , 'min'
            playlist_number += 1
            curr_length = 0
            curr_items = []
        else:
            encoding = item[-4:]
            encodings = {'.mp3': MP3, '.mp4': MP4}
            try:
                music_file = encodings[encoding](item)
            except Exception as e:
                handleException(e)
            else:
                file_length = music_file.info.length
                if file_length > length:
                    too_long_items.append(item)
                    print 'File %s exceed the given length (%s min)' % (item, file_length/60)
                else:
                    curr_length += file_length
                    curr_items.append(item+'\n')

    print '\nThis files exceeded the given length and were not added to any playlist...\n'
    for i in too_long_items:
        print basename(i)

def handleException(e):
    print type(e)     # the exception instance
    print e.args      # arguments stored in .args
    print e           # __str__ allows args to printed directly

if __name__ == '__main__':
    main()