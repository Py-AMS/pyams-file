#
# Copyright (c) 2015-2019 Thierry Florac <tflorac AT ulthar.net>
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#

"""PyAMS_file.include module

This module is used for Pyramid integration
"""

__docformat__ = 'restructuredtext'

import logging

try:
    import pillow_avif
except ImportError:
    logging.getLogger('PyAMS (file)').warning("Missing pillow_avif plug-in. AVIF image format will not be supported...")


def include_package(config):
    """Pyramid package include"""

    # add translations
    config.add_translation_dirs('pyams_file:locales')

    config.scan()
