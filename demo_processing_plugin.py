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

__author__ = 'Your Name'
__date__ = '2022-09-18'
__copyright__ = '(C) 2022 by Your Name'

# This will get replaced with a git SHA1 when you do a git archive

__revision__ = '$Format:%H$'

import os
import sys
import inspect
import processing

from PyQt5.QtWidgets import QAction
from PyQt5.QtGui import QIcon
from qgis.core import QgsProcessingAlgorithm, QgsApplication
# import the provider class from the provider .py file...
from .demo_processing_plugin_provider import DemoProcessingPluginProvider

cmd_folder = os.path.split(inspect.getfile(inspect.currentframe()))[0]

iconPath = os.path.dirname(__file__)

if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)


class DemoProcessingPlugin(object):

    def __init__(self, iface):
        self.iface = iface
        self.provider = DemoProcessingPluginProvider()

    def initGui(self):
        QgsApplication.processingRegistry().addProvider(self.provider)
        
        self.action_1 = QAction(self.icon(), u"Reproject raster", self.iface.mainWindow())
        self.action_1.triggered.connect(self.runAlg_1)
        self.iface.addPluginToMenu(u"&Demo Plugin", self.action_1)
        self.iface.addToolBarIcon(self.action_1)
        
        self.action_2 = QAction(self.icon(), u"Copy vector", self.iface.mainWindow())
        self.action_2.triggered.connect(self.runAlg_2)
        self.iface.addPluginToMenu(u"&Demo Plugin", self.action_2)
        self.iface.addToolBarIcon(self.action_2)
        
    def runAlg_1(self):
        processing.execAlgorithmDialog("demo-processing-plugin:reproject_raster")

    def runAlg_2(self):
        processing.execAlgorithmDialog("demo-processing-plugin:copy_vector")

    def unload(self):
        QgsApplication.processingRegistry().removeProvider(self.provider)
        
    def icon(self):
        return QIcon(os.path.join(iconPath, "smiley.png"))
    
        