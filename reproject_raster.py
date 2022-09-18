from qgis.PyQt.QtCore import QCoreApplication
from qgis.core import (QgsProcessing, QgsProcessingAlgorithm,
                        QgsProcessingParameterFile,
                        QgsProcessingParameterFeatureSource,
                        QgsProcessingParameterFolderDestination,
                        QgsCoordinateReferenceSystem)

import processing
import os
                       
class ReprojectRaster(QgsProcessingAlgorithm):
    INPUT_DIR = 'INPUT_DIR'
    BOUNDARY = 'BOUNDARY'
    OUTPUT_DIR = 'OUTPUT_DIR'
 
    def __init__(self):
        super().__init__()
 
    def name(self):
        return "reproject_raster"
         
    def displayName(self):
        return "Reproject raster"
 
    def group(self):
        return "Raster"
 
    def groupId(self):
        return "raster"
 
    def shortHelpString(self):
        return "Reproject an input raster layer."
         
    def createInstance(self):
        return type(self)()
   
    def initAlgorithm(self, config=None):
        self.addParameter(QgsProcessingParameterFile(self.INPUT_DIR, "Input directory", behavior=QgsProcessingParameterFile.Folder))
        self.addParameter(QgsProcessingParameterFeatureSource(self.BOUNDARY, "Boundary layer", [QgsProcessing.TypeVectorPolygon]))
        self.addParameter(QgsProcessingParameterFolderDestination(self.OUTPUT_DIR, "Output directory"))
 
    def processAlgorithm(self, parameters, context, feedback):
        data_dir = self.parameterAsString(parameters, self.INPUT_DIR, context)
        output_dir = self.parameterAsString(parameters, self.OUTPUT_DIR, context)
        
        # Input parameter Boundary Layer...
        boundary = self.parameterAsSource(parameters, self.BOUNDARY, context)
        # ...Do whatever you want with boundary
        
        filename = "LC08_L1TP_104069_20170721_20170728_01_T1_B3.TIF"
        Landsat_Image1_NIR = os.path.join(data_dir, filename)
        
        params = {'INPUT':Landsat_Image1_NIR,
                    'SOURCE_CRS':None,
                    'TARGET_CRS':QgsCoordinateReferenceSystem('EPSG:28353'),
                    'RESAMPLING':0,
                    'NODATA':None,
                    'TARGET_RESOLUTION':None,
                    'OPTIONS':'',
                    'DATA_TYPE':0,
                    'TARGET_EXTENT':None,
                    'TARGET_EXTENT_CRS':None,
                    'MULTITHREADING':False,
                    'EXTRA':'',
                    'OUTPUT':os.path.join(output_dir,'Landsat_Image1_NIR_repr.tif')}
                    
        reprojected = processing.run('gdal:warpreproject', params, context=context, feedback=feedback, is_child_algorithm=True)
        
        # Load output layer on completion
        details = context.LayerDetails(reprojected['OUTPUT'], context.project())
        context.addLayerToLoadOnCompletion(reprojected['OUTPUT'], details)
 
        return {'OUTPUT': reprojected['OUTPUT']}
