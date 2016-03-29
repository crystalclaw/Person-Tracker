#!/usr/bin/env python3
# AUTHOR:   Ian Drobney
# DATE:     3/24/2016

# This module handles all of the data access and most in-memory storage

import storage

# The index data is loaded into this variable
index = None
# This variable holds the data in the template file, which is used to
# add pre-made fields to a record/person, and as a set of default fields
# for a new record/person.
# TODO(crystalclaw): maybe seperate this out into a new-record/person template
# and a possible fields template? This will get rid of unneccesary fields in
# new records. Could also just delete unused fields after creation.
template = None
# Stores currently loaded records in memory. Not all are loaded at once, folder
# memory management reasons.
# TODO(crystalclaw): add something to unload records from data, possibly with
# automatic cleanup of some sort
data = {}
# The location of the data.
# TODO(crystalclaw): possibly change how this is handled (a file location
# handling function?) and test it to make sure it works with everything
location = ''


# set the current working location
def set_location(loc):
    global location
    location = loc


# pretty much a reload/init function; probably won't call this much after
# startup. Just loads the index and template into memory from file.
def load_main():
    global index
    global template
    index = storage.load_file(location + 'index.pickle')
    template = storage.load_file(location + index['template'])


# write everything to disk, except when certain critical data is missing.
# FIXME(crystalclaw): Currently, these checks fail silently
# FIXME(crystalclaw): make the saving happen all at once, so that data
# mismatches don't happen
def save_all():
    # check if the index is empty; if it is, don't save it or anything else.
    # It was probably cleared accidentally, and should never be empty.
    if index is not None:
        storage.save_file(index, location + 'index.pickle')
        # same for the template
        if template is not None:
            storage.save_file(template, location + index['template'])
        # don't bother saving nothing.
        if not len(data) == 0:
            for i in data.keys():
                storage.save_file(data[i], location + 'data/'
                                  + str(i) + '.pickle')


# add a field to the template
# FIXME(crystalclaw): don't save_all here. Maybe just save template; might want
# some data to not be saved for some reason sometimes, like data that's
# currently being edited.
def new_field(field_name):
    global template
    template[field_name] = ''
    save_all()


# add a new record to the system.
# NOTE(crystalclaw): probably safe to save_all here, but keep it in mind
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
