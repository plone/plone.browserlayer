from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='plone.browserlayer',
      version=version,
      description="Browser layer management for Zope 2 applications",
      long_description=open("README.txt").read() + "\n" + \
                       open(os.path.join("docs", "HISTORY.txt")).read(),,
      classifiers=[
        "Framework :: Plone",
        "Framework :: Zope2",
        "Framework :: Zope3",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='plone browser layer',
      author='Martin Aspeli',
      author_email='optilude@gmx.net',
      url='http://plone.org',
      license='LGPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['plone'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
      ],
      )
