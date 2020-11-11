#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""print rise jupyter into pdf
It requires input arguments:
    i) token for your notebook
   ii) output resolution
  iii) name of output
"""
import os
import sys
import subprocess


def export_pdf(token, argvs):
    """
    Note:
        argvs[0] is file name
    """

    command = ('`npm bin`/decktape rise -s ' + str(argvs[2])
               + ' http://localhost:8888/notebooks/'
               + str(argvs[3])
               + '.ipynb?token='
               + token + ' ./' + str(argvs[3]) + '.pdf')

    os.system(command)

    # remove node module
    os.system('rm -rf node_modules package-lock.json')

def run():

    if os.path.exists('./node_modules/') is False:
        os.system('npm install decktape')

    notebook_list = \
        subprocess.run(['jupyter', 'notebook', 'list'],
                       stdout=subprocess.PIPE).stdout.decode('utf-8')

    notebook = notebook_list.split('token=', 1)[1].split()[0]

    print('rise2pdf')
    print(f'convert {notebook} to pdf file...')

    argvs = sys.argv
    print(argvs)

