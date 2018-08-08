# -*- coding: utf-8 -*-

import handler_xml  as xhandler
import handler_json as jhandler
import data



def generate_xml():
    xhandler.xml_handler(data.data).generate()

def generate_json():
    jhandler.json_handler().generate()