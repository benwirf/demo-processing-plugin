from qgis.PyQt.QtCore import QCoreApplication, QVariant
from qgis.core import (QgsField, QgsFeature, QgsFeatureSink, QgsFeatureRequest,
                        QgsProcessing, QgsProcessingAlgorithm,
                        QgsProcessingParameterFeatureSource,
                        QgsProcessingParameterFeatureSink)
                      
class CopyVector(QgsProcessingAlgorithm):
    INPUT = 'INPUT'
    OUTPUT = 'OUTPUT'

    def __init__(self):
        super().__init__()

    def name(self):
        return "copy_vector"
        
    def displayName(self):
        return "Copy vector"

    def group(self):
        return "Vector"

    def groupId(self):
        return "vector"

    def shortHelpString(self):
        return "Example script which copies features from an input vector to an output vector"
        
    def createInstance(self):
        return type(self)()
  
    def initAlgorithm(self, config=None):
        self.addParameter(QgsProcessingParameterFeatureSource(self.INPUT, "Input layer", [QgsProcessing.TypeVectorAnyGeometry]))
        self.addParameter(QgsProcessingParameterFeatureSink(self.OUTPUT, "Output layer", QgsProcessing.TypeVectorAnyGeometry))

    def processAlgorithm(self, parameters, context, feedback):
        source = self.parameterAsSource(parameters, self.INPUT, context)
        (sink, dest_id) = self.parameterAsSink(parameters, self.OUTPUT, context,
                                               source.fields(), source.wkbType(), source.sourceCrs())

        features = source.getFeatures(QgsFeatureRequest())
        for feat in features:
            out_feat = QgsFeature()
            out_feat.setGeometry(feat.geometry())
            out_feat.setAttributes(feat.attributes())
            sink.addFeature(out_feat, QgsFeatureSink.FastInsert)

        return {self.OUTPUT: dest_id}