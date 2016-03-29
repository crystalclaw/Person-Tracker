#!/usr/bin/env python3
# AUTHOR:   Ian Drobney
# DATE:     3/24/2016

# This module handles all direct file loading and saving

import defaults
import os
import pickle


# load a .pickle file from disk and return it
# TODO(crystalclaw): sanatize this input to make sure it's not malicious;
# probably not an issue, and probably really hard, but try.
def load_file(file):
    target_file = open(file, 'rb')
    data_out = pickle.load(target_file)
    target_file.close()
    return data_out


# Save some data into a pickle file on disk.
def save_file(data, file):
    target_file = open(file, 'wb')
    pickle.dump(data, target_file, protocol=4)
    target_file.close()
    return True


# Create the default file structure
# TODO(crystalclaw): make sure this doesn't overwrite anything important
def create_file_structure(location='', name='ptinfo'):
    main_folder = location + name
    if not os.path.exists(main_folder):
        os.mkdir(main_folder)
    else:
        return False
    save_file(defaults.index, main_folder + '/index.pickle')
    save_file(defaults.fields, main_folder + '/template.pickle')
    os.mkdir(main_folder + '/data')
    return True
