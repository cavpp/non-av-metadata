#!/usr/bin/python
# -*- coding: UTF-8 -*-
from abc import ABCMeta, abstractmethod, abstractproperty
from xml.dom.minidom import parseString
from xml.etree.ElementTree import tostring
from NonAVModel import Element



class CAPS_node(object):
    __metaclass__ = ABCMeta
    @abstractmethod
    def _make_xml(self):
        print("You shouldn't be here")
        pass

    # @abstractproperty
    @property
    def xml(self):
        self._check_required()
        xml = self._make_xml()

        return xml

    @classmethod
    def validate_tag(self):
        pass

    @abstractmethod
    def validate_attribute(self):
        pass

    @abstractmethod
    def _check_required(self):
        pass

    @classmethod
    def __init__(self):
        self.__xML_attributes = None

    def get_xml(self):
        pass

    def __str__(self):
        # print(self.xml)
        assert self.xml is not None
        etree = tostring(self.xml.xml, encoding="utf-8")
        dom = parseString(str(etree.decode()))
        return dom.toprettyxml()