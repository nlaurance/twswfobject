import os
import sys

from setuptools import setup, find_packages

execfile(os.path.join("tw", "swfobject", "release.py"))

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description = (
    '\n.. contents::\n\n' +
    'Detailed Documentation\n' +
    '**********************\n'
    + '\n' +
    read('README.txt')
    + '\n\n' +
    'Contributors\n' +
    '************\n'
    + '\n' +
    read('Contributors.txt')
    + '\n' +
    'Change history\n' +
    '**************\n'
    + '\n' +
    read('CHANGES.txt')
    + '\n'
    )

setup(
    name=__DISTRIBUTION__,
    version=__VERSION__,
    description=__DESCRIPTION__,
    author=__AUTHOR__,
    author_email=__EMAIL__,
    url=__URL__,
    install_requires=[
        "ToscaWidgets",
        ],
    packages=find_packages(exclude=['ez_setup', 'tests']),
    namespace_packages = ['tw'],
    zip_safe=False,
    include_package_data=True,
    test_suite = 'nose.collector',
    entry_points="""
        [toscawidgets.widgets]
        # Register your widgets so they can be listed in the WidgetBrowser
        widgets = tw.swfobject
        samples = tw.swfobject.samples
    """,
    keywords = [
        'toscawidgets.widgets',
    ],
    long_description=long_description,
    # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Environment :: Web Environment :: ToscaWidgets',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Widget Sets',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: TurboGears :: Widgets',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
    ],
)

