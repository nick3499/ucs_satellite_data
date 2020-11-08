#! /bin/python3
'''Get satellite data, then render template to browser.'''
# data: https://www.ucsusa.org/media/11493 (1 August 2020)
from flask import Flask
from flask import render_template
import csv

APP = Flask(__name__)  # Flask instance
SAT_DATA = []  # satellite data

@APP.route('/')  # route to root
def get_sat_data():
    '''Get satellite data, then render template to browser.'''
    with open('data/ucs_satellite_data.tsv', 'r') as tsv_read:
        csv_read = csv.reader(tsv_read, delimiter='\t')  # init CSV reader obj
        next(csv_read)  # skip column header row
        for row in csv_read:
            SAT_DATA.append(row)  # append CSV record to SAT_DATA
    return render_template('template.htm', sat_data=SAT_DATA)  # render template

if __name__ == '__main__':
    APP.run(host='127.0.0.1', port=3000)  # if standalone
