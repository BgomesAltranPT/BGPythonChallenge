# -*- coding: utf-8 -*-

from handler_xml import xml_handler
import json
import messages
import os


class json_handler:

    def __init__(self):
        self.__gl_xml = []
        self.__load()

    def __load(self):
        self.__gl_xml = []
        ll_dir = os.listdir("./")
        for lf_xml in ll_dir:
            if not lf_xml.endswith(".xml"): continue
            self.__gl_xml.append(lf_xml)

    def __create(self, iv_xml):

        lv_split    = str.split(iv_xml, '.')
        lv_path = lv_split[0] + '.json'

        try:

            ll_xml  = xml_handler.get_dict_from_xml(iv_xml)
            lv_out  = open(lv_path, 'w')
            json.dump(ll_xml, lv_out, sort_keys = True, indent=4, separators=(',', ': '))

            print messages.gen_json_cre % lv_path

        except Exception:
            pass
        except IOError:
            print(messages.error_json_cre)

    def generate(self):
        for lf_xml in self.__gl_xml:
            self.__create(lf_xml)
