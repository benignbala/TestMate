#!/usr/bin/python

from setuptools import setup, find_packages
import os

name = "testmate"
version = "0.1"

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

setup(
    name=name,
    version=version,
    description="A Test case and Requirement management system in Python/Flask.",
    long_description=read('README'),
    # Get strings from http://www.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[],
    keywords="",
    author="",
    author_email='',
    url='',
    license='',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'Flask',
        'SQLAlchemy'
    ],
    entry_points="""
    [console_scripts]
    flask-ctl = testmate.script:run
    
    [paste.app_factory]
    main = testmate.script:make_app
    debug = testmate.script:make_debug
        """,
    )
