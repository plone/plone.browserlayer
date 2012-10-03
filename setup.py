from setuptools import setup, find_packages

version = '2.1.2'

setup(name='plone.browserlayer',
      version=version,
      description="Browser layer management for Zope 2 applications",
      long_description=open("README.txt").read() + "\n" + \
                       open("CHANGES.txt").read(),
      classifiers=[
          "Environment :: Web Environment",
          "Framework :: Plone",
          "Framework :: Zope2",
          "License :: OSI Approved :: GNU General Public License (GPL)",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
        ],
      keywords='plone browser layer',
      author='Plone Foundation',
      author_email='plone-developers@lists.sourceforge.net',
      url='http://pypi.python.org/pypi/plone.browserlayer',
      license='GPL version 2',
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
          'zope.traversing >= 3.9.0',
          'Products.CMFCore',
          'Products.GenericSetup>=1.4',
          'Zope2',
      ],
      )
