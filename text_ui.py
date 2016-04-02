#!/usr/bin/env python3
# AUTHOR:   Ian Drobney
# DATE:     4/1/2016

# just a basic UI, potentailly expand this later
import data
import defaults
import menus
import version


# main menu init
def main_menu():
    menus.basic_menu(defaults.init_menu,
                     title='Person tracker v' + version.VERSION)
