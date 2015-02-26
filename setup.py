from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
    name='ckanext-dataset_rating',
    version=version,
    description="dataset 5 star rating",
    long_description='''
    ''',
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='Janos Farkas',
    author_email='farkas48@uniba.sk',
    url='',
    license='',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.dataset_rating'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points='''
        [ckan.plugins]
        # Add plugins here, e.g.
        dataset_rating=ckanext.dataset_rating.plugin:DatasetRatingPlugin
    ''',
)
