#!/usr/bin/env python3
# AUTHOR:   Ian Drobney
# DATE:     3/24/2016

# This module is just for defining first-run defaults for creating default
# files. In a seperate place so it's easier to read and examine.

index = {
    'template': 'template.pickle',
    'version': '1.0.0',
    'next_uuid': 0,
    'data': {

    }
}
# basically, the default template file as it stands. This might change.
fields = {
    'uuid': 0,
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
