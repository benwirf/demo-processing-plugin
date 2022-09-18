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
"""

__author__ = 'Ben Wirf'
__date__ = '2022-09-11'
__copyright__ = '(C) 2022 by Ben Wirf'

# This will get replaced with a git SHA1 when you do a git archive

__revision__ = '$Format:%H$'

import os
from PyQt5.QtGui import QIcon
from qgis.core import QgsProcessingProvider
# Import your algorithm classes from your processing script files...
from .reproject_raster import ReprojectRaster
from .copy_vector import CopyVector


iconPath = os.path.dirname(__file__)


class DemoProcessingPluginProvider(QgsProcessingProvider):

    def __init__(self):
        QgsProcessingProvider.__init__(self)

    def load(self):
        self.refreshAlgorithms()
        return True

    def unload(self):
        """
        Unloads the provider. Any tear-down steps required by the provider
        should be implemented here.
        """
        pass

    def isActive(self):
        return True

    def loadAlgorithms(self):
        """
        Loads all algorithms belonging to this provider.
        """
        # Load algorithms (instances of your algorithm classes)
        self.alglist = [ReprojectRaster(),
                        CopyVector()]

        for alg in self.alglist:
            self.addAlgorithm(alg)

    def icon(self):
        return QIcon(os.path.join(iconPath, "smiley.png"))

    def id(self):
        """
        Returns the unique provider id, used for identifying the provider. This
        string should be a unique, short, character only string, eg "qgis" or
        "gdal". This string should not be localised.
        """
        return 'demo-processing-plugin'

    def name(self):
        """
        Returns the provider name, which is used to describe the provider
        within the GUI.
        This string should be short (e.g. "Lastools") and localised.
        """
        return 'Demo Processing Plugin'

    def longName(self):
        """
        Returns the a longer version of the provider name, which can include
        extra details such as version numbers. E.g. "Lastools LIDAR tools
        (version 2.2.1)". This string should be localised. The default
        implementation returns the same string as name().
        """
        return self.name()