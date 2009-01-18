from setuptools import setup, find_packages
import os

version = '2.0'

setup(name='plone.browserlayer',
      version=version,
      description="Browser layer management for Zope 2 applications",
      long_description=open(os.path.join("plone", "browserlayer", "README.txt")).read() + "\n" + \
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='plone browser layer',
      author='Martin Aspeli',
      author_email='optilude@gmx.net',
      url='http://plone.org',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['plone'],
      include_package_data=True,
      zip_safe=False,
      extras_require=dict(
        test=[
            'Products.PloneTestCase',
        ]
      ),
      install_requires=[
          'setuptools',
          'zope.component',
          'zope.interface',
          'zope.app.publication',
          'Plone',
          'Products.CMFCore',
          'Products.GenericSetup>=1.4',
          # 'Zope2',
      ],
      )
