__author__ = 'Gonzalo Mateo-García, Ana Ruescas'

import pandas as pd
from sklearn.model_selection import train_test_split

PATH_TO_DATA_SYKE = "/Users/abruescas/Desktop/Conferencias_2022/IOCCG/mlregocean-cdom/data/SYKE_S3_header.txt"
PATH_TO_MODELS_SYKE = "/Users/abruescas/Desktop/Conferencias_2022/IOCCG/mlregocean-cdom/models/"

###2.1 Possible inputs
bands_S3_SYKE = ['S3400','S3412.5','S3442.5','S3490','S3510','S3560',
                  'S3620','S3665','S3673.75','S3681.25',
                 'S3708.75', 'S3753.75']
bands_S3ratio = ['S3ratio1','S3ratio2']
bands_S3_plus_ratios_SYKE = bands_S3_SYKE + bands_S3ratio

ALL_BANDS_SYKE = bands_S3_plus_ratios_SYKE
target_band_SYKE = 'a400 (1/m)'

bands_try_SYKE=dict([('S3ratio1',['S3ratio1']),
                   ('S3ratio2',['S3ratio2']),
                   ('S3bands&ratios', bands_S3_plus_ratios_SYKE)])

'''
bands_try_SYKE=dict([('S3ratio1',['S3ratio1']),
           ('S3ratio2',['S3ratio2']),
           ("ratios_S3",bands_S3ratio),
           ("S3bands",bands_S3_SYKE),
           ("S3bands&ratios", bands_S3_plus_ratios_SYKE)])
'''

def load_SYKE(path_to_data=PATH_TO_DATA_SYKE):
    skdata = pd.read_csv(path_to_data, sep='\t', na_values=' ')
    skdata['S3ratio1'] = skdata['S3665'] / skdata['S3490']
    skdata['S3ratio2'] = skdata['S3708.75'] / skdata['S3490']

    skdata_X_train, skdata_X_test, skdata_y_train, skdata_y_test = train_test_split(skdata[ALL_BANDS_SYKE],
                                                                                    skdata[target_band_SYKE], test_size=0.25, random_state=42)
    skdata_y_train = skdata_y_train.values
    skdata_y_test = skdata_y_test.values

    return skdata_X_train, skdata_X_test, skdata_y_train, skdata_y_test

