from setuptools import find_packages
from setuptools import setup


version = "3.0.1"

setup(
    name="plone.browserlayer",
    version=version,
    description="Browser layer management for Zope applications",
    long_description=(open("README.rst").read() + "\n" + open("CHANGES.rst").read()),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 6.0",
        "Framework :: Plone :: Core",
        "Framework :: Zope :: 5",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    keywords="plone browser layer",
    author="Plone Foundation",
    author_email="plone-developers@lists.sourceforge.net",
    url="https://github.com/plone/plone.browserlayer",
    license="GPL version 2",
    packages=find_packages(),
    namespace_packages=["plone"],
    include_package_data=True,
    zip_safe=False,
    extras_require=dict(
        test=[
            "plone.app.testing",
            "plone.testing",
            "transaction",
            "zope.event",
        ]
    ),
    install_requires=[
        "setuptools",
        "zope.component",
        "zope.interface",
        "zope.traversing >= 3.9.0",
        "Products.CMFCore",
        "Products.GenericSetup>=1.4",
        "Zope",
    ],
)
