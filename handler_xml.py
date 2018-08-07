# -*- coding: utf-8 -*-

import xmltodict as xmldict
from lxml import etree as etree
import messages

gv_url      = "http://example.org/types"
gv_rootname = "a"

class xml_handler:
    def __init__(self, il_data = {}):
        self._gl_data = il_data

    def generate(self):
        for ll_data in self._gl_data:
            self.__create_xml(ll_data)

    def __create_xml(self, il_data ={}):

        name    = etree.QName(gv_url, gv_rootname)
        root    = etree.Element(name, nsmap={"bit":gv_url})
        ll_keys = il_data.keys()
        lv_file = il_data.get("file")

        ll_keys.remove("file")

        for lv_key in ll_keys:
            etree.SubElement(root, lv_key).text = str(il_data[lv_key])

        if self.__validate(etree.ElementTree(root)):
            etree.ElementTree(root).write(lv_file, pretty_print=True)
            print messages.gen_xml_created % lv_file
        else:
            print messages.gen_xml_error % lv_file

    def __validate(self, iv_tree = etree.ElementTree()):

        try:
            sch_doc = etree.parse(open("schema.xsd"))
            schema = etree.XMLSchema(sch_doc)
            return schema.validate(iv_tree)
        except etree.XMLSyntaxError as e:
            print(e)
        except IOError:
            print messages.error_xml_sche

        return False

    @staticmethod
    def get_dict_from_xml(iv_path):

        with open(iv_path, 'r') as lv_file:
            return xmldict.parse(lv_file)

        raise Exception(messages.error_xml_file)

