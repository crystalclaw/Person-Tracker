#!/usr/bin/env python3
# AUTHOR:   Ian Drobney
# DATE:     4/1/2016

# just a basic UI, potentailly expand this later
import data
import defaults
import menus
import pycase
import version


# main menu init
def main_menu():
    data.load_main()
    num_result, menu_item = menus.basic_menu(
        defaults.init_menu,
        title='Person Tracker v' + version.VERSION
        )
    for case in pycase.switch(menu_item):
        if case('Show all'):
            if get_record_list() != []:
                print(menus.basic_menu(
                    get_record_list(),
                    title='Person Tracker v' + version.VERSION)
                    )
            else:
                main_menu()

            break
        if case('New'):
            pass
            break
        if case('Search'):
            pass
            break
        if case('Edit Fields'):
            pass
            break
        if case():
            pass
            break
        print(menu_item)


def get_record_list():
    output = []
    index = data.get_index()
    for i, v in index['data']:
        output.append(v['name'])
    return output


def new_record():
    pass
