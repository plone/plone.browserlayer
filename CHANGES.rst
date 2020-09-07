Changelog
=========

.. You should *NOT* be adding new change log entries to this file.
   You should create a file in the news directory instead.
   For helpful instructions, please see:
   https://github.com/plone/plone.releaser/blob/master/ADD-A-NEWS-ITEM.rst

.. towncrier release notes start

2.2.4 (2020-09-07)
------------------

Bug fixes:


- Fixed deprecation warning for ``zope.component.interfaces.IComponentRegistry``.
  [maurits] (#3130)


2.2.3 (2020-04-20)
------------------

Bug fixes:


- Minor packaging updates. (#1)


2.2.2 (2018-09-28)
------------------

Bug fixes:

- Fix tests for py3
  [pbauer]


2.2.1 (2018-02-02)
------------------

Bug fixes:

- Add Python 2 / 3 compatibility
  [pbauer]


2.2.0 (2017-02-12)
------------------

Bug fixes:

- Fixed test when using Zope 4.  [maurits]


2.1.7 (2016-11-01)
------------------

Fixes:

- Removed ZopeTestCase.  We were importing from it but not using it...
  [ivanteoh, maurits]


2.1.6 (2015-10-27)
------------------

Fixes:

- Minor cleanup in order to follow plone code style conventions.
  [jensens]


2.1.5 (2015-04-29)
------------------

- Rerelease for clarity, because 2.1.4 got released twice.
  [maurits]


2.1.4 (2015-04-29)
------------------

- Move tests to plone.app.testing.
  [sdelcourt,timo]


2.1.3 (2014-02-25)
------------------

- Fix tests with diazo.
  [davisagli]


2.1.2 (2012-10-03)
------------------

- Add support for calling many times remove in export (ie:even when no corresponding layer is registred, remove option should not throw exception).
  [toutpt]

2.1.1 (2011-11-24)
------------------

- Added uninstall support to browserlayer.xml with the 'remove' option.
  [maurits]

- GS export xml is now repeatable. Before two consecutive exports could
  yield differently ordered results.
  [do3cc]


2.1 - 2011-05-12
----------------

- Update import of BeforeTraverseEvent to come from zope.traversing instead
  of zope.app.publication.
  [davisagli]

- Add MANIFEST.in
  [WouterVH]


2.0.1 - 2010-09-21
------------------

- Make sure the layers don't get applied twice if the site is traversed more
  than once (such as in a vhosting URL).
  [davisagli]


2.0 - 2010-07-18
----------------

- Update license to GPL version 2 only.
  [hannosch]

- Package metadata cleanup, require Zope2 distribution.
  [hannosch]


1.0.1 - 2009-09-09
------------------

- Be more robust against broken layer registrations. These can occur when
  packages with registered layers are removed.
  [wichert]

- Clarified license and copyright.
  [hannosch]

- Register ourselves for the more generic ISiteRoot from CMFCore and not
  IPloneSiteRoot.
  [hannosch]

- Declare test dependencies in an extra.
  [hannosch]

- Specify package dependencies.
  [hannosch]


1.0.0 - 2008-04-20
------------------

- Unchanged from 1.0rc4


1.0rc4 - 2008-04-13
-------------------

- Register the GenericSetup import and export steps using zcml. This means you
  will no longer need to install this package manually.
  [wichert]


1.0rc3 - 2008-03-09
-------------------

- Include README.txt and HISTORY.txt in the package's long description.
  [wichert]

- Add metadata.xml to the GenericSetup profile. This fixes a deprecation
  warning for Plone 3.1 and later.
  [wichert]


1.0b1 - 2007-09-23
------------------

- Initial package structure.
  [zopeskel]
