from __future__ import absolute_import
from setuptools import find_packages
from setuptools import setup


setup(
    name='url_montior',
    version='0.1',
    description='Monitor URL for downtime',
    classifiers=['Private :: Do Not Upload'],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'console_scripts': ['url_monitor = url_monitor:url_monitor']
    })
