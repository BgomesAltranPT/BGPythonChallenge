# -*- coding: utf-8 -*-

import funcs as func
import messages as message
import os


class Menu:

    __gl_option = [func.generate_xml, func.generate_json, message.menu_exit]
    __gl_menu   = [message.menu_start, message.menu_op_xml, message.menu_op_json, message.menu_op_quit]

    def __init__(self):
        self.gv_exit = False

    def execute(self):
        while not self.gv_exit:
            self.__show_menu()
            lv_op = self.__get_select_option()
            self.clear()   # probably not working

            if not self.__is_valid(lv_op):
                print(message.menu_op_err)
                continue

            self.__execute_function(int(lv_op))

    def clear(self):
        os.system('cls')

    def __show_menu(self):
        for line in Menu.__gl_menu:
            print(line)

    def __get_select_option(self):
        return input(message.menu_sel)

    def __execute_function(self, iv_val):

        if Menu.__gl_option[iv_val - 1] == message.menu_exit:
            self.gv_exit = True
            return

        Menu.__gl_option[iv_val - 1]()

    def __is_valid(self, iv_value):

        try:
            int(iv_value)
            if int(iv_value) > len(Menu.__gl_option): return
            if int(iv_value) < 1: return
        except ValueError:
            return False

        return True
