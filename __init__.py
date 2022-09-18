# -*- coding: utf-8 -*-
"""
/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""

__author__ = 'Your Name'
__date__ = '2022-09-18'
__copyright__ = '(C) 2022 by Your Name'


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load DemoProcessingPlugin class from file demo_processing_plugin.py
    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .demo_processing_plugin import DemoProcessingPlugin
    return DemoProcessingPlugin(iface)