import pymel.core as pm
import logging

log = logging.getLogger("ui")

class BaseTemplate(pm.ui.AETemplate):
    
    def addControl(self, control, label=None, **kwargs):
        pm.ui.AETemplate.addControl(self, control, label=label, **kwargs)
        
    def beginLayout(self, name, collapse=True):
        pm.ui.AETemplate.beginLayout(self, name, collapse=collapse)
        

class AECoronaSurfaceTemplate(BaseTemplate):
    def __init__(self, nodeName):
        BaseTemplate.__init__(self,nodeName)
        log.debug("AECoronaSurfaceTemplate")
        self.thisNode = None
        self.node = pm.PyNode(self.nodeName)
        pm.mel.AEswatchDisplay(nodeName)
        self.beginScrollLayout()
        self.buildBody(nodeName)
        self.addExtraControls("ExtraControls")
        self.endScrollLayout()
        
    def buildBody(self, nodeName):
        self.thisNode = pm.PyNode(nodeName)
        self.beginLayout("Diffuse" ,collapse=0)
        self.addControl("diffuse", label="Diffuse Color")
        self.addControl("diffuseMultiplier", label="Diffuse Level")
        self.addSeparator()
        self.addControl("translucency", label="Translucency")
        self.addControl("translucencyFraction", label="Translucency Fraction")
        self.addSeparator()
        self.addControl("alphaMode", label="Alpha Mode")
        self.addControl("opacity", label="Opacity")
        self.addControl("opacityMultiplier", label="Opacity Level")
        self.endLayout()
        self.beginLayout("Round Corners" ,collapse=0)
        self.addControl("roundCornersRadius", label="Radius")
        self.addControl("roundCornersSamples", label="Samples")
        self.endLayout()
        self.beginLayout("Reflection" ,collapse=0)
        self.addControl("reflectivity", label="Reflectivity")
        self.addControl("reflectivityMultiplier", label="Reflectivity Level")
        self.addControl("reflectionGlossiness", label="Glossiness")
        self.addControl("fresnelIorMultiplier", label="Fresnel Value")
        self.addControl("fresnelIor", label="Fresnel Map")
        self.addControl("anisotropy", label="Anisotropy")
        self.addControl("anisotropicRotation", label="Aniso Rotation")
        self.endLayout()
        self.beginLayout("Refraction" ,collapse=0)
        self.addControl("refractivity", label="Refractivity")
        self.addControl("refractivityMultiplier", label="Refractivity Level")
        self.addControl("refractionIndexMultiplier", label="Refraction Index")
        self.addControl("refractionIndex", label="Refraction Index Map")
        self.addControl("refractionGlossiness", label="Glossiness")
        self.addControl("glassType", label="Glass Mode")
        self.endLayout()
        self.beginLayout("Volume" ,collapse=0)
        self.addControl("attenuationColor", label="Absorption Color")
        self.addControl("attenuationDist", label="Absorption Distance")
        self.addSeparator()
        self.addControl("volumeScatteringAlbedo", label="Scatter Color")
        self.addControl("volumeMeanCosine", label="Scatter Directionality")
        self.addControl("volumeSSSMode", label="Use SSS Mode")
#         self.addSeparator()
#         self.addControl("volumeEmissionColor", label="Emission Color")
#         self.addControl("volumeEmissionDist", label="Emission Distance")
#         self.endLayout()
        self.beginLayout("Emission" ,collapse=0)
        self.beginNoOptimize()
        self.addControl("emissionColor", label="Emission Color")
        self.addControl("emissionColorMultiplier", label="Emission Multiplier")
        #self.addControl("iesProfile", label="IES Profile")
        #self.addControl("emissionDisableSampling", label="Disable Sampling")
        #self.addControl("emissionSharpnessFake", label="Sharpness Fake")
        #self.addControl("emissionSharpnessFakePoint", label="Sharpness Fake Point")
        self.endNoOptimize()
        self.endLayout()
        
        #self.beginLayout("Hardware Texturing" ,collapse=0)
        #pm.mel.eval('AEhardwareTextureTemplate "%s"' % self.nodeName + r'("diffuse emissionColor ")')
        #self.endLayout()
        