# -*- coding: utf-8 -*-
from setuptools import find_packages
from setuptools import setup

version = '2.2.4'

setup(
    name='plone.browserlayer',
    version=version,
    description="Browser layer management for Zope 2 applications",
    long_description=(
        open("README.rst").read() +
        "\n" +
        open("CHANGES.rst").read()
    ),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 5.0",
        "Framework :: Plone :: 5.1",
        "Framework :: Plone :: 5.2",
        "Framework :: Plone :: Core",
        "Framework :: Zope2",
        "Framework :: Zope :: 4",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    keywords='plone browser layer',
    author='Plone Foundation',
    author_email='plone-developers@lists.sourceforge.net',
    url='https://pypi.org/project/plone.browserlayer',
    license='GPL version 2',
    packages=find_packages(),
    namespace_packages=['plone'],
    include_package_data=True,
    zip_safe=False,
    extras_require=dict(
        test=[
           'plone.app.testing',
        ]
    ),
    install_requires=[
        'setuptools',
        'zope.component',
        'zope.interface',
        'zope.traversing >= 3.9.0',
        'Products.CMFCore',
        'Products.GenericSetup>=1.4',
        'Zope2',
    ],
)
