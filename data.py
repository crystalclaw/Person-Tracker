#!/usr/bin/env python3
# AUTHOR:   Ian Drobney
# DATE:     3/24/2016

import os
import pickle


default_index = {
    'template': 'template.pickle',
    'version': '1.0.0',
    'data': {

    }
}

default_fields = {
    'name': '',
    'gender': '',
    'birthdate': {
        'year': '',
        'month': '',
        'day': '',
    },
    'hostmask': '',
    'address': {
        'street': '',
        'city': '',
        'state': '',
        'zip': '',
    },
    'nicks': {}
}


def load_file(file):
    target_file = open(file, 'rb')
    pickle.load(target_file)
    target_file.close()


def save_file(data, file):
    target_file = open(file, 'wb')
    pickle.dump(data, target_file, protocol=4)
    target_file.close()


def create_file_structure(location='', name='ptinfo'):
    main_folder = location + name
    if not os.path.exists(main_folder):
        os.mkdir(main_folder)
    else:
        return False
    save_file(default_index, main_folder + '/index.pickle')
    save_file(default_fields, main_folder + '/template.pickle')
    os.mkdir(main_folder + '/data')
    return True

print(create_file_structure())
