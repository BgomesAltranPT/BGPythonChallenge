# -*- coding: utf-8 -*-

import handler_xml as xhandler
import handler_json as jhandler
import data
import copy
import lxml.etree as etree


def generate_xml():
    xhandler.xml_handler(data.data).generate()

def generate_json():
    jhandler.json_handler().generate()

def validate_test():
    sch_doc = etree.parse(open("schema.xsd"))
    schema = etree.XMLSchema(sch_doc)
    file = etree.parse(open("test.xml"))
    print schema.validate(file)

def get_values():
    sch_doc = etree.parse(open("schema.xsd"))
    root = copy.copy(sch_doc.getroot()[0])
    il_data = data.data[0]
    ll_keys = il_data.keys()

    ll_keys.remove("file")

    lv_filename = "test.xml"

    for lv_key in ll_keys:
        etree.SubElement(root, lv_key).text = str(il_data[lv_key])


    etree.ElementTree(root).write(lv_filename, pretty_print=True)
