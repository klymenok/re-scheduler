"""
This file is subject to the terms and conditions defined in the
file 'LICENSE.txt.txt', which is a part of this source code package.
"""

import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()
setuptools.setup(
    name='re_scheduler',
    version='0.0.1',
    scripts=['re_scheduler'],
    author='Oleksii Klymenok',
    author_email='klymenok.a@gmail.com',
    description='Re-scheduler for django-celery non-periodic tasks',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/klymenok/re-scheduler',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
