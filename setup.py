from setuptools import setup, find_packages

version = '1.0b2'

setup(name='plone.browserlayer',
      version=version,
      description="Browser layer management for Zope 2 applications",
      long_description="""\
This package makes it possible to register new browser layers, which are 
automatically applied to the request when the appropriate product is installed.
""",
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
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
      zip_safe=True,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
