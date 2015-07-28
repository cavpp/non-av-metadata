#!/usr/bin/python
# -*- coding: UTF-8 -*-
from enum import Enum
from Model import Element
import Model.Instantiation
import re
from Model.CAPS_node import CAPS_node


class CompressionModes(Enum):
    LOSSLESS = "Lossless"
    LOSY = "Lossy"
    UNCOMPRESSED = "Uncompressed"


class Technical(CAPS_node):
    VALID_ATTRIBUTES = []
    def __init__(self,
                 fileFormat = None,
                 imageFormat = None,
                 width = None,
                 height = None,
                 chromaSubsampling = None,
                 colorBitDepth = None,
                 compressionMode = None):
        """
        :param str fileFormat:              Specifies the MIME type of the file.
        :param str imageFormat:             Specifies the encoding of the digital file. For example: JPEG200
        :param int width:                   Specifies the x dimensions of the digital file.
        :param int height:                  Specifies the y dimensions of the digital file
        :param str chromaSubsampling:       Specifies the Chroma Subsampling as a ratio in the format integer:integer:integer. For example 4:2:2.In the absence of subsampling, the value of this element is 4:4:4.
        :param colorDepth:                  The bit depth per channel
        :param str compressionMode:
        _fileFormat (str):                  Specifies the MIME type of the file.
        _imageFormat (str):                 Specifies the encoding of the digital file. For example: JPEG200
        _resolutionWidth                    Specifies the x dimensions of the digital file.
        _resolutionHeight                   Specifies the y dimensions of the digital file
        _colorSpace (str):                  Specifies the type of color space used by the digital file. For example: YUV
        _chromaSubsampling (str):           Specifies the Chroma Subsampling as a ratio in the format integer:integer:integer. For example 4:2:2.In the absence of subsampling, the value of this element is 4:4:4.
        _colorDepth                         The bit depth per channel
        _compressionMode                    Designates the type of compression. Please use only Lossless, Lossy, Uncompressed, or Unknown
        _additionalTechnicalNotes (str):    Additional techincal notes about the file that do not fit into other elements

        """
        super(Technical, self).__init__()
        self._fileFormat = None
        self._imageFormat = None
        self._resolutionWidth = None
        self._resolutionWidthUnit = None
        self._resolutionHeightUnit = None
        self._resolutionHeight = None
        self._colorSpace = None
        self._chromaSubsampling = None
        self._colorDepth = None
        self._compressionMode = None
        self._colorDepthUnit = None
        self._chromaSubsampling = None
        self._additionalTechnicalNotes = None


        self.fileFormat = fileFormat
        self.imageFormat = imageFormat


        if width:
            if isinstance(width, int):
                self.resolutionWidthUnit = "pixels"
                self.resolutionWidth = width
            else:
                raise TypeError("Expected int received " + str(type(width)))
        if height:
            if isinstance(height, int):
                self.resolutionHeightUnit = "pixels"
                self.resolutionHeight = height
            else:
                raise TypeError("Expected int received " + str(type(height)))

        if colorBitDepth:

            self.colorDepth = colorBitDepth
            self.colorDepthUnit = "bits"


        if compressionMode:
            self.compressionMode = compressionMode

        if chromaSubsampling:
            self.chromaSubsampling = chromaSubsampling




    def _make_xml(self):
        root = Element(tag="Technical")
        if self._fileFormat:
            root.add_child(Element(tag='fileFormat', data=self.fileFormat))

        if self._imageFormat:
            root.add_child(Element(tag='imageFormat', data=self.imageFormat))
        if self._resolutionWidth:
            if self._resolutionWidthUnit:
                root.add_child(Element(tag='resolutionWidth', data=self.resolutionWidth, attributes={"unit": self.resolutionWidthUnit}))
            else:
                raise Exception("resolutionWidth element is used but is missing a unit attribute.")
        if self._resolutionHeight:
            if self._resolutionHeightUnit:
                root.add_child(Element(tag='resolutionHeight', data=self.resolutionHeight, attributes={"unit": self.resolutionHeightUnit}))
            else:
                raise Exception("resolutionHeight element is used but is missing a unit attribute.")
        if self._colorSpace:
            root.add_child(Element(tag='colorSpace', data=self.colorSpace))
        if self._chromaSubsampling:
            root.add_child(Element(tag='chromaSubsampling', data=self.chromaSubsampling))
        if self._colorDepth:
            if self.colorDepthUnit:
                root.add_child(Element(tag='colorDepth', data=self.colorDepth, attributes={"unit": self.colorDepthUnit}))
            else:
                raise Exception("colorDepth element is used but is missing a unit attribute.")
        if self._compressionMode:
            root.add_child(Element(tag='compressionMode', data=self.compressionMode))
        if self._additionalTechnicalNotes:
            root.add_child(Element(tag='additionalTechnicalNotes', data=self.additionalTechnicalNotes))
        return root.xml

    def validate_attribute(self):
        # todo fill in validate_attribute
        pass

    def _check_required(self):
        missing_metatdata = []
        if not self.fileFormat:
            missing_metatdata.append("fileFormat")
        if not self.imageFormat:
            missing_metatdata.append("imageFormat")
        if not self.resolutionHeight:
            missing_metatdata.append("resolutionHeight")
        if not self.resolutionWidth:
            missing_metatdata.append("resolutionWidth")
        if not self.colorSpace:
            missing_metatdata.append("colorSpace")
        if not self.colorDepth:
            missing_metatdata.append("colorDepth")
        if not self.compressionMode:
            missing_metatdata.append("compressionMode")
        if len(missing_metatdata) > 0:
            raise Exception("Missing required metadata fields, '" + "', '".join(missing_metatdata) + "'.")

    @property
    def fileFormat(self):
        return self._fileFormat

    @fileFormat.setter
    def fileFormat(self, value):
        self._fileFormat = value


    @property
    def imageFormat(self):
        return self._imageFormat

    @imageFormat.setter
    def imageFormat(self, value):
        self._imageFormat = value


    @property
    def resolutionWidthUnit(self):
        return self._resolutionWidthUnit

    @resolutionWidthUnit.setter
    def resolutionWidthUnit(self, value):
        self._resolutionWidthUnit = value


    @property
    def resolutionWidth(self):
        return self._resolutionWidth

    @resolutionWidth.setter
    def resolutionWidth(self, value):
        self._resolutionWidth = value


    @property
    def resolutionHeightUnit(self):
        return self._resolutionHeightUnit

    @resolutionHeightUnit.setter
    def resolutionHeightUnit(self, value):
        self._resolutionHeightUnit = value


    @property
    def resolutionHeight(self):
        return self._resolutionHeight

    @resolutionHeight.setter
    def resolutionHeight(self, value):
        self._resolutionHeight = value


    @property
    def colorSpace(self):
        return self._colorSpace

    @colorSpace.setter
    def colorSpace(self, value):
        color_space_pattern = re.compile('\d+:\d+:\d+')
        # Todo: check if colorSpace, it is properly formated with regex
        if not color_space_pattern.match(value):
            raise ValueError( "'" + str(value) + "' is not a proper color space format")
        self._colorSpace = value


    @property
    def chromaSubsampling(self):
        return self._chromaSubsampling

    @chromaSubsampling.setter
    def chromaSubsampling(self, value):
        self._chromaSubsampling = value


    @property
    def colorDepth(self):
        return self._colorDepth

    @colorDepth.setter
    def colorDepth(self, value):
        if not isinstance(value, int):
            raise TypeError("Expected an int, received " + str(type(value)))
        self._colorDepth = value


    @property
    def colorDepthUnit(self):
        return str(self._colorDepthUnit)

    @colorDepthUnit.setter
    def colorDepthUnit(self, value):
        self._colorDepthUnit = value


    @property
    def compressionMode(self):
        return self._compressionMode

    @compressionMode.setter
    def compressionMode(self, value):
        # Todo: check if compression mode, it is the right ENUM
        if not isinstance(value, CompressionModes):
            raise TypeError("Expected an CompressionModes, received " + str(type(value)))
        self._compressionMode = value.value


    @property
    def additionalTechnicalNotes(self):
        return self._additionalTechnicalNotes

    @additionalTechnicalNotes.setter
    def additionalTechnicalNotes(self, value):
        self._additionalTechnicalNotes = value

