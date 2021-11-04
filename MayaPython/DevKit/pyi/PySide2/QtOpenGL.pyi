from typing import Any, Container, Dict, Generic, Iterable, Iterator, List, Optional, Set, Tuple, TypeVar, Union
from . import QtCore


from PySide2.QtGui import QPaintDevice as _QPaintDevice
from PySide2.QtWidgets import QWidget as _QWidget
from PySide2.QtCore import QObject as _QObject


if False:
    from typing import Dict, List, Tuple, Union, Optional

class _Object(object):
    __dict__ : dictproxy


class QGLShader(_QObject):
    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        ...
    def compileSourceCode(*args, **kwargs): ...
    def compileSourceFile(*args, **kwargs): ...
    def isCompiled(*args, **kwargs): ...
    def log(*args, **kwargs): ...
    def shaderId(*args, **kwargs): ...
    def shaderType(*args, **kwargs): ...
    def sourceCode(*args, **kwargs): ...
    @staticmethod
    def hasOpenGLShaders(*args, **kwargs): ...
    Fragment : ShaderTypeBit
    
    Geometry : ShaderTypeBit
    
    ShaderType : Type[ShaderType]
    
    ShaderTypeBit : Type[ShaderTypeBit]
    
    Vertex : ShaderTypeBit
    
    __new__ : builtin_function_or_method
    
    staticMetaObject : PySide2.QtCore.QMetaObject


class QGLPixelBuffer(_QPaintDevice):
    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        ...
    def bindTexture(*args, **kwargs): ...
    def bindToDynamicTexture(*args, **kwargs): ...
    def context(*args, **kwargs): ...
    def deleteTexture(*args, **kwargs): ...
    def devType(*args, **kwargs): ...
    def doneCurrent(*args, **kwargs): ...
    def drawTexture(*args, **kwargs): ...
    def format(*args, **kwargs): ...
    def generateDynamicTexture(*args, **kwargs): ...
    def handle(*args, **kwargs): ...
    def isValid(*args, **kwargs): ...
    def makeCurrent(*args, **kwargs): ...
    def metric(*args, **kwargs): ...
    def paintEngine(*args, **kwargs): ...
    def releaseFromDynamicTexture(*args, **kwargs): ...
    def size(*args, **kwargs): ...
    def toImage(*args, **kwargs): ...
    def updateDynamicTexture(*args, **kwargs): ...
    @staticmethod
    def hasOpenGLPbuffers(*args, **kwargs): ...
    __new__ : builtin_function_or_method


class QGLShaderProgram(_QObject):
    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        ...
    def addShader(*args, **kwargs): ...
    def addShaderFromSourceCode(*args, **kwargs): ...
    def addShaderFromSourceFile(*args, **kwargs): ...
    def attributeLocation(*args, **kwargs): ...
    def bind(*args, **kwargs): ...
    def bindAttributeLocation(*args, **kwargs): ...
    def disableAttributeArray(*args, **kwargs): ...
    def enableAttributeArray(*args, **kwargs): ...
    def geometryInputType(*args, **kwargs): ...
    def geometryOutputType(*args, **kwargs): ...
    def geometryOutputVertexCount(*args, **kwargs): ...
    def isLinked(*args, **kwargs): ...
    def link(*args, **kwargs): ...
    def log(*args, **kwargs): ...
    def maxGeometryOutputVertices(*args, **kwargs): ...
    def programId(*args, **kwargs): ...
    def release(*args, **kwargs): ...
    def removeAllShaders(*args, **kwargs): ...
    def removeShader(*args, **kwargs): ...
    def setAttributeArray2D(*args, **kwargs): ...
    def setAttributeArray3D(*args, **kwargs): ...
    def setAttributeArray4D(*args, **kwargs): ...
    def setAttributeBuffer(*args, **kwargs): ...
    def setAttributeValue(*args, **kwargs): ...
    def setGeometryInputType(*args, **kwargs): ...
    def setGeometryOutputType(*args, **kwargs): ...
    def setGeometryOutputVertexCount(*args, **kwargs): ...
    def setUniformValue(*args, **kwargs): ...
    def setUniformValueArray2D(*args, **kwargs): ...
    def setUniformValueArray2x2(*args, **kwargs): ...
    def setUniformValueArray2x3(*args, **kwargs): ...
    def setUniformValueArray2x4(*args, **kwargs): ...
    def setUniformValueArray3D(*args, **kwargs): ...
    def setUniformValueArray3x2(*args, **kwargs): ...
    def setUniformValueArray3x3(*args, **kwargs): ...
    def setUniformValueArray3x4(*args, **kwargs): ...
    def setUniformValueArray4D(*args, **kwargs): ...
    def setUniformValueArray4x2(*args, **kwargs): ...
    def setUniformValueArray4x3(*args, **kwargs): ...
    def setUniformValueArray4x4(*args, **kwargs): ...
    def setUniformValueArrayInt(*args, **kwargs): ...
    def setUniformValueArrayUint(*args, **kwargs): ...
    def shaders(*args, **kwargs): ...
    def uniformLocation(*args, **kwargs): ...
    @staticmethod
    def hasOpenGLShaderPrograms(*args, **kwargs): ...
    __new__ : builtin_function_or_method
    
    staticMetaObject : PySide2.QtCore.QMetaObject


class QGLFormat(_Object):
    def __copy__(*args, **kwargs): ...
    def __eq__(self, other: Any) -> bool:
        """
        x.__eq__(y) <==> x==y
        """
        ...
    def __ge__(self, other: Any) -> bool:
        """
        x.__ge__(y) <==> x>=y
        """
        ...
    def __gt__(self, other: Any) -> bool:
        """
        x.__gt__(y) <==> x>y
        """
        ...
    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        ...
    def __le__(self, other: Any) -> bool:
        """
        x.__le__(y) <==> x<=y
        """
        ...
    def __lt__(self, other: Any) -> bool:
        """
        x.__lt__(y) <==> x<y
        """
        ...
    def __ne__(self, other: Any) -> bool:
        """
        x.__ne__(y) <==> x!=y
        """
        ...
    def __repr__(self) -> str:
        """
        x.__repr__() <==> repr(x)
        """
        ...
    def accum(*args, **kwargs): ...
    def accumBufferSize(*args, **kwargs): ...
    def alpha(*args, **kwargs): ...
    def alphaBufferSize(*args, **kwargs): ...
    def blueBufferSize(*args, **kwargs): ...
    def depth(*args, **kwargs): ...
    def depthBufferSize(*args, **kwargs): ...
    def directRendering(*args, **kwargs): ...
    def doubleBuffer(*args, **kwargs): ...
    def greenBufferSize(*args, **kwargs): ...
    def hasOverlay(*args, **kwargs): ...
    def majorVersion(*args, **kwargs): ...
    def minorVersion(*args, **kwargs): ...
    def plane(*args, **kwargs): ...
    def profile(*args, **kwargs): ...
    def redBufferSize(*args, **kwargs): ...
    def rgba(*args, **kwargs): ...
    def sampleBuffers(*args, **kwargs): ...
    def samples(*args, **kwargs): ...
    def setAccum(*args, **kwargs): ...
    def setAccumBufferSize(*args, **kwargs): ...
    def setAlpha(*args, **kwargs): ...
    def setAlphaBufferSize(*args, **kwargs): ...
    def setBlueBufferSize(*args, **kwargs): ...
    def setDepth(*args, **kwargs): ...
    def setDepthBufferSize(*args, **kwargs): ...
    def setDirectRendering(*args, **kwargs): ...
    def setDoubleBuffer(*args, **kwargs): ...
    def setGreenBufferSize(*args, **kwargs): ...
    def setOption(*args, **kwargs): ...
    def setOverlay(*args, **kwargs): ...
    def setPlane(*args, **kwargs): ...
    def setProfile(*args, **kwargs): ...
    def setRedBufferSize(*args, **kwargs): ...
    def setRgba(*args, **kwargs): ...
    def setSampleBuffers(*args, **kwargs): ...
    def setSamples(*args, **kwargs): ...
    def setStencil(*args, **kwargs): ...
    def setStencilBufferSize(*args, **kwargs): ...
    def setStereo(*args, **kwargs): ...
    def setSwapInterval(*args, **kwargs): ...
    def setVersion(*args, **kwargs): ...
    def stencil(*args, **kwargs): ...
    def stencilBufferSize(*args, **kwargs): ...
    def stereo(*args, **kwargs): ...
    def swapInterval(*args, **kwargs): ...
    def testOption(*args, **kwargs): ...
    @staticmethod
    def defaultFormat(*args, **kwargs): ...
    @staticmethod
    def defaultOverlayFormat(*args, **kwargs): ...
    @staticmethod
    def fromSurfaceFormat(*args, **kwargs): ...
    @staticmethod
    def hasOpenGL(*args, **kwargs): ...
    @staticmethod
    def hasOpenGLOverlays(*args, **kwargs): ...
    @staticmethod
    def openGLVersionFlags(*args, **kwargs): ...
    @staticmethod
    def setDefaultFormat(*args, **kwargs): ...
    @staticmethod
    def setDefaultOverlayFormat(*args, **kwargs): ...
    @staticmethod
    def toSurfaceFormat(*args, **kwargs): ...
    CompatibilityProfile : OpenGLContextProfile
    
    CoreProfile : OpenGLContextProfile
    
    NoProfile : OpenGLContextProfile
    
    OpenGLContextProfile : Type[OpenGLContextProfile]
    
    OpenGLVersionFlag : Type[OpenGLVersionFlag]
    
    OpenGLVersionFlags : Type[OpenGLVersionFlags]
    
    OpenGL_ES_CommonLite_Version_1_0 : OpenGLVersionFlag
    
    OpenGL_ES_CommonLite_Version_1_1 : OpenGLVersionFlag
    
    OpenGL_ES_Common_Version_1_0 : OpenGLVersionFlag
    
    OpenGL_ES_Common_Version_1_1 : OpenGLVersionFlag
    
    OpenGL_ES_Version_2_0 : OpenGLVersionFlag
    
    OpenGL_Version_1_1 : OpenGLVersionFlag
    
    OpenGL_Version_1_2 : OpenGLVersionFlag
    
    OpenGL_Version_1_3 : OpenGLVersionFlag
    
    OpenGL_Version_1_4 : OpenGLVersionFlag
    
    OpenGL_Version_1_5 : OpenGLVersionFlag
    
    OpenGL_Version_2_0 : OpenGLVersionFlag
    
    OpenGL_Version_2_1 : OpenGLVersionFlag
    
    OpenGL_Version_3_0 : OpenGLVersionFlag
    
    OpenGL_Version_3_1 : OpenGLVersionFlag
    
    OpenGL_Version_3_2 : OpenGLVersionFlag
    
    OpenGL_Version_3_3 : OpenGLVersionFlag
    
    OpenGL_Version_4_0 : OpenGLVersionFlag
    
    OpenGL_Version_4_1 : OpenGLVersionFlag
    
    OpenGL_Version_4_2 : OpenGLVersionFlag
    
    OpenGL_Version_4_3 : OpenGLVersionFlag
    
    OpenGL_Version_None : OpenGLVersionFlag
    
    __new__ : builtin_function_or_method


class QGL(_Object):
    AccumBuffer : FormatOption
    
    AlphaChannel : FormatOption
    
    ColorIndex : FormatOption
    
    DebugContext : FormatOption
    
    DeprecatedFunctions : FormatOption
    
    DepthBuffer : FormatOption
    
    DirectRendering : FormatOption
    
    DoubleBuffer : FormatOption
    
    FormatOption : Type[FormatOption]
    
    FormatOptions : Type[FormatOptions]
    
    HasOverlay : FormatOption
    
    IndirectRendering : FormatOption
    
    NoAccumBuffer : FormatOption
    
    NoAlphaChannel : FormatOption
    
    NoDebugContext : FormatOption
    
    NoDeprecatedFunctions : FormatOption
    
    NoDepthBuffer : FormatOption
    
    NoOverlay : FormatOption
    
    NoSampleBuffers : FormatOption
    
    NoStencilBuffer : FormatOption
    
    NoStereoBuffers : FormatOption
    
    Rgba : FormatOption
    
    SampleBuffers : FormatOption
    
    SingleBuffer : FormatOption
    
    StencilBuffer : FormatOption
    
    StereoBuffers : FormatOption


class QGLFramebufferObject(_QPaintDevice):
    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        ...
    def attachment(*args, **kwargs): ...
    def bind(*args, **kwargs): ...
    def devType(*args, **kwargs): ...
    def drawTexture(*args, **kwargs): ...
    def format(*args, **kwargs): ...
    def handle(*args, **kwargs): ...
    def isBound(*args, **kwargs): ...
    def isValid(*args, **kwargs): ...
    def metric(*args, **kwargs): ...
    def paintEngine(*args, **kwargs): ...
    def release(*args, **kwargs): ...
    def size(*args, **kwargs): ...
    def texture(*args, **kwargs): ...
    def toImage(*args, **kwargs): ...
    @staticmethod
    def bindDefault(*args, **kwargs): ...
    @staticmethod
    def blitFramebuffer(*args, **kwargs): ...
    @staticmethod
    def hasOpenGLFramebufferBlit(*args, **kwargs): ...
    @staticmethod
    def hasOpenGLFramebufferObjects(*args, **kwargs): ...
    Attachment : Type[Attachment]
    
    CombinedDepthStencil : Attachment
    
    Depth : Attachment
    
    NoAttachment : Attachment
    
    __new__ : builtin_function_or_method


class QGLContext(_Object):
    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        ...
    def bindTexture(*args, **kwargs): ...
    def chooseContext(*args, **kwargs): ...
    def colorIndex(*args, **kwargs): ...
    def contextHandle(*args, **kwargs): ...
    def create(*args, **kwargs): ...
    def deleteTexture(*args, **kwargs): ...
    def device(*args, **kwargs): ...
    def deviceIsPixmap(*args, **kwargs): ...
    def doneCurrent(*args, **kwargs): ...
    def drawTexture(*args, **kwargs): ...
    def format(*args, **kwargs): ...
    def initialized(*args, **kwargs): ...
    def isSharing(*args, **kwargs): ...
    def isValid(*args, **kwargs): ...
    def makeCurrent(*args, **kwargs): ...
    def moveToThread(*args, **kwargs): ...
    def overlayTransparentColor(*args, **kwargs): ...
    def requestedFormat(*args, **kwargs): ...
    def reset(*args, **kwargs): ...
    def setDevice(*args, **kwargs): ...
    def setFormat(*args, **kwargs): ...
    def setInitialized(*args, **kwargs): ...
    def setValid(*args, **kwargs): ...
    def setWindowCreated(*args, **kwargs): ...
    def swapBuffers(*args, **kwargs): ...
    def windowCreated(*args, **kwargs): ...
    @staticmethod
    def areSharing(*args, **kwargs): ...
    @staticmethod
    def currentContext(*args, **kwargs): ...
    @staticmethod
    def fromOpenGLContext(*args, **kwargs): ...
    @staticmethod
    def setTextureCacheLimit(*args, **kwargs): ...
    @staticmethod
    def textureCacheLimit(*args, **kwargs): ...
    BindOption : Type[BindOption]
    
    BindOptions : Type[BindOptions]
    
    CanFlipNativePixmapBindOption : BindOption
    
    DefaultBindOption : BindOption
    
    InternalBindOption : BindOption
    
    InvertedYBindOption : BindOption
    
    LinearFilteringBindOption : BindOption
    
    MemoryManagedBindOption : BindOption
    
    MipmapBindOption : BindOption
    
    NoBindOption : BindOption
    
    PremultipliedAlphaBindOption : BindOption
    
    TemporarilyCachedBindOption : BindOption
    
    __new__ : builtin_function_or_method


class QGLFramebufferObjectFormat(_Object):
    def __copy__(*args, **kwargs): ...
    def __eq__(self, other: Any) -> bool:
        """
        x.__eq__(y) <==> x==y
        """
        ...
    def __ge__(self, other: Any) -> bool:
        """
        x.__ge__(y) <==> x>=y
        """
        ...
    def __gt__(self, other: Any) -> bool:
        """
        x.__gt__(y) <==> x>y
        """
        ...
    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        ...
    def __le__(self, other: Any) -> bool:
        """
        x.__le__(y) <==> x<=y
        """
        ...
    def __lt__(self, other: Any) -> bool:
        """
        x.__lt__(y) <==> x<y
        """
        ...
    def __ne__(self, other: Any) -> bool:
        """
        x.__ne__(y) <==> x!=y
        """
        ...
    def attachment(*args, **kwargs): ...
    def internalTextureFormat(*args, **kwargs): ...
    def mipmap(*args, **kwargs): ...
    def samples(*args, **kwargs): ...
    def setAttachment(*args, **kwargs): ...
    def setInternalTextureFormat(*args, **kwargs): ...
    def setMipmap(*args, **kwargs): ...
    def setSamples(*args, **kwargs): ...
    def setTextureTarget(*args, **kwargs): ...
    def textureTarget(*args, **kwargs): ...
    __new__ : builtin_function_or_method


class QGLColormap(_Object):
    def __copy__(*args, **kwargs): ...
    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        ...
    def entryColor(*args, **kwargs): ...
    def entryRgb(*args, **kwargs): ...
    def find(*args, **kwargs): ...
    def findNearest(*args, **kwargs): ...
    def handle(*args, **kwargs): ...
    def isEmpty(*args, **kwargs): ...
    def setEntry(*args, **kwargs): ...
    def setHandle(*args, **kwargs): ...
    def size(*args, **kwargs): ...
    __new__ : builtin_function_or_method


class QGLBuffer(_Object):
    def __getattribute__(*args, **kwargs):
        """
        x.__getattribute__('name') <==> x.name
        """
        ...
    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        ...
    def allocate(*args, **kwargs): ...
    def bind(*args, **kwargs): ...
    def bufferId(*args, **kwargs): ...
    def create(*args, **kwargs): ...
    def destroy(*args, **kwargs): ...
    def isCreated(*args, **kwargs): ...
    def map(*args, **kwargs): ...
    def read(*args, **kwargs): ...
    def setUsagePattern(*args, **kwargs): ...
    def size(*args, **kwargs): ...
    def type(*args, **kwargs): ...
    def unmap(*args, **kwargs): ...
    def usagePattern(*args, **kwargs): ...
    def write(*args, **kwargs): ...
    @staticmethod
    def release(*args, **kwargs): ...
    Access : Type[Access]
    
    DynamicCopy : UsagePattern
    
    DynamicDraw : UsagePattern
    
    DynamicRead : UsagePattern
    
    IndexBuffer : Type
    
    PixelPackBuffer : Type
    
    PixelUnpackBuffer : Type
    
    ReadOnly : Access
    
    ReadWrite : Access
    
    StaticCopy : UsagePattern
    
    StaticDraw : UsagePattern
    
    StaticRead : UsagePattern
    
    StreamCopy : UsagePattern
    
    StreamDraw : UsagePattern
    
    StreamRead : UsagePattern
    
    Type : Type[Type]
    
    UsagePattern : Type[UsagePattern]
    
    VertexBuffer : Type
    
    WriteOnly : Access
    
    __new__ : builtin_function_or_method


class QGLWidget(_QWidget):
    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        ...
    def autoBufferSwap(*args, **kwargs): ...
    def bindTexture(*args, **kwargs): ...
    def colormap(*args, **kwargs): ...
    def context(*args, **kwargs): ...
    def deleteTexture(*args, **kwargs): ...
    def doneCurrent(*args, **kwargs): ...
    def doubleBuffer(*args, **kwargs): ...
    def drawTexture(*args, **kwargs): ...
    def event(*args, **kwargs): ...
    def format(*args, **kwargs): ...
    def glDraw(*args, **kwargs): ...
    def glInit(*args, **kwargs): ...
    def grabFrameBuffer(*args, **kwargs): ...
    def initializeGL(*args, **kwargs): ...
    def initializeOverlayGL(*args, **kwargs): ...
    def isSharing(*args, **kwargs): ...
    def isValid(*args, **kwargs): ...
    def makeCurrent(*args, **kwargs): ...
    def makeOverlayCurrent(*args, **kwargs): ...
    def overlayContext(*args, **kwargs): ...
    def paintEngine(*args, **kwargs): ...
    def paintEvent(*args, **kwargs): ...
    def paintGL(*args, **kwargs): ...
    def paintOverlayGL(*args, **kwargs): ...
    def qglClearColor(*args, **kwargs): ...
    def qglColor(*args, **kwargs): ...
    def renderPixmap(*args, **kwargs): ...
    def renderText(*args, **kwargs): ...
    def resizeEvent(*args, **kwargs): ...
    def resizeGL(*args, **kwargs): ...
    def resizeOverlayGL(*args, **kwargs): ...
    def setAutoBufferSwap(*args, **kwargs): ...
    def setColormap(*args, **kwargs): ...
    def swapBuffers(*args, **kwargs): ...
    def updateGL(*args, **kwargs): ...
    def updateOverlayGL(*args, **kwargs): ...
    @staticmethod
    def convertToGLFormat(*args, **kwargs): ...
    __new__ : builtin_function_or_method
    
    staticMetaObject : PySide2.QtCore.QMetaObject



