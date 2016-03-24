#!/usr/bin/env python3
# AUTHOR:   Ian Drobney
# DATE:     3/24/2016

import storage

index = None
template = None
data = {}
location = ''


# set the current working location
def set_location(loc):
    global location
    location = loc


def load_main():
    global index
    global template
    # load the index and template into memory
    index = storage.load_file(location + 'index.pickle')
    template = storage.load_file(location + index['template'])


# write everything to disk
def save_all():
    if index is not None:
        storage.save_file(index, location + 'index.pickle')
        if template is not None:
            storage.save_file(template, location + index['template'])
        if not len(data) == 0:
            for i in data.keys():
                storage.save_file(data[i], location + 'data/'
                                  + str(i) + '.pickle')


def new_field(field_name):
    global template
    template[field_name] = ''
    save_all()


def new_record(Name):
    data_out = template
    data_out['uuid'] = index['next_uuid']
    data_out['name'] = Name
    # add the new record to the index
    index['data'][data['uuid']] = {
        'name': Name,
        'file': str(data_out['uuid'] + '.pickle')
    }
    # make the new record, just to be safe
    storage.save_file(data_out, location + 'data/' +
                      str(data_out['uuid']) + '.pickle')
    # add the record to the in-memory data
    data[data_out['uuid']] = data_out
    # increment the uuid so there are no conflicts
    index['next_uuid'] = index['next_uuid'] + 1
    # save everything to file, so nothing gets lost if the program crashes
    save_all()
