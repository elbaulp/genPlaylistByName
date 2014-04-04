'''
Created on Apr 4, 2014

@author: Alejandro Alcalde

Licensed under GPLv3
'''

import argparse
import fnmatch
from mutagen.mp3 import MP3 
from mutagen.mp4 import MP4
from os.path import os
from sys import argv


def main():
    
    parser = argparse.ArgumentParser(description='Generate playlists with the indicated length')
    parser.add_argument('-d','--directory', help='Directory with music files',type=str, required=True)
    parser.add_argument('-l', '--length', help='Length of the playlist, in minutes', type=int, required=True)

    args = parser.parse_args()
    
    directory = args.directory
    length =  args.length * 60
    
    
    path = r'./playlists/' 
    if not os.path.exists(path): os.makedirs(path)
    
    playlist_basename = argv[0] + str(length/60) + '_'
    playlist_number = 1
    curr_length = 0
    curr_items = []
    
    for music_file in os.listdir(directory):
        if fnmatch.fnmatch(music_file, '*.mp[43]'):
            if curr_length >= length:
                name = path + playlist_basename + str(playlist_number) + '.m3u'
                playlist_file = open(name, 'w')
                playlist_file.writelines(curr_items)
                playlist_file.close()
                print 'Playlist generated, name: ', name , ' length ', curr_length/60 , 'min'
                playlist_number += 1
                curr_length = 0
                curr_items = []
            elif music_file.endswith('.mp3'):
                try:
                    mp3_file = MP3(directory + music_file)
                except Exception as e:
                    handleException(e)
                else:
                    curr_length += mp3_file.info.length
                    curr_items.append(directory+music_file+'\n')
            elif music_file.endswith('.mp4'):
                try:
                    mp4_file = MP4(directory + music_file)
                except Exception as e:
                    handleException(e)
                else:
                    curr_length += mp4_file.info.length
                    curr_items.append(directory+music_file+'\n')
    
def handleException(e):
    print type(e)     # the exception instance
    print e.args      # arguments stored in .args
    print e           # __str__ allows args to printed directly

if __name__ == '__main__':
    main()