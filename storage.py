#!/usr/bin/env python3
# AUTHOR:   Ian Drobney
# DATE:     3/24/2016

import defaults
import os
import pickle


index = {}


def load_file(file):
    target_file = open(file, 'rb')
    data_out = pickle.load(target_file)
    target_file.close()
    return data_out


def save_file(data, file):
    target_file = open(file, 'wb')
    pickle.dump(data, target_file, protocol=4)
    target_file.close()
    return True


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
