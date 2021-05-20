import os
from os import path
from setuptools import setup

# read the contents of your README file
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name = 'rf_calc',
    author='Pruthiraj Jayasingh',
    author_email='pruthirajjayasingh.4u@gmail.com',
    version = '0.0.7',
    install_requires =['numpy>=1.19.4','pandas>=1.1.5','tabulate>=0.8.9'] ,
    description = 'Often we spend lots of time calculating the Receptive field of a CNN model.This Module can calculate the receptive field, Output image size  from a model object',
    long_description=long_description,
    long_description_content_type='text/markdown',
    py_modules = ["rf_calc"],
    package_dir = {'':'src'},
    classifiers= [
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
        "Operating System :: OS Independent",],
    )