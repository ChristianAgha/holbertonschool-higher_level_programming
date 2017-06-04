#!/usr/bin/python3
"""Student class module"""


class Student:
    """initialization"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None or attrs == '':
            return self.__dict__
        else:
            atrb_list = {}
            for atrb in attrs:
                if atrb in self.__dict__:
                    atrb_list.update({atrb: self.__dict__[atrb]})
            return atrb_list

    def reload_from_json(self, json):
        for k in json:
            if k in self.__dict__:
                self.__dict__[k] = json[k]
