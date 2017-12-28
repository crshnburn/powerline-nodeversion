# vim:fileencoding=utf-8:noet

from setuptools import setup

setup(
    name         = 'powerline-nodeversion',
    description  = 'A Powerline segment for showing the current version of node.js',
    version      = '1.0.0',
    keywords     = 'powerline node.js status prompt',
    license      = 'Apache-2.0',
    author       = 'Andrew Smithson',
    author_email = 'smithson@uk.ibm.com',
    url          = '',
    packages     = ['powerline_nodeversion'],
    classifiers  = [
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache License',
        'Topic :: Terminals'
    ]
)