# -*- coding: utf-8 -*-
"""Main Module.
This module is used to analyse the input used o this work
Example:
    To run this module you have to specify what do you want to run:
        $ python main.py --clean
Attributes:
    clean: used to inform the application that have to clean the observation file
"""
import argparse
from src.group_data_files import GroupDataFiles
from src.my_enums import RUNNING_MODE

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', help='Mode to run de application groupdata| grupresultdata| mergegroupeddata | mergeresultanddata')

    args = parser.parse_args()

    if args.mode is not None and args.mode in RUNNING_MODE.get_all_values():
        operation_mode = args.mode
        if (args.mode == RUNNING_MODE.GROUPDATA.value):
            GroupDataFiles()
        else:
            print("Não foi possível rodar a aplicação.")
