# -*- coding: utf-8 -*-

"""{Description}"""

__author__ = "k.mp"

# generic | built-in imports
import os
from glob import iglob

# library imports
from bs4 import BeautifulSoup
from settings import basedir

# templates directory path
template_dir = os.path.abspath(os.path.join(basedir, "app/templates/generated"))

# files match string
file_lookup = os.path.join(template_dir, "*.html")


class Soup(object):

    # constructor
    def __init__(self):
        self.file = os.path.join(template_dir, "text.html")
        with open(self.file) as file:
            self.doc = BeautifulSoup(file, "html.parser")

    @classmethod
    def append_jinja_start(cls):
        for file in iglob(file_lookup, recursive=True):
            if not Soup.search(file, "{% extends 'base.html' %}"):
                with open(file, "r+") as f:
                    lines = f.readlines()
                    f.seek(0)
                    f.write("{% extends 'base.html' %}\n")
                    f.write("{% block content %}\n")
                    f.write("<div>\n")
                    for line in lines:
                        f.write(line)
                f.close()

    @classmethod
    def append_jinja_end(cls):
        for file in iglob(file_lookup, recursive=True):
            if not Soup.search(file, "{% endblock %}"):
                with open(file, "a+") as f:
                    f.write("\n</div>")
                    f.write("\n{% endblock %}")
                f.close()

    @classmethod
    def search(cls, filename, search_str):
        file = open(filename, "r")
        read = file.readlines()
        file.close()
        for line in read:
            words = line.split("\n")
            if words[0] == search_str:
                return True
        return False


if __name__ == "__main__":
    Soup.append_jinja_start()
    Soup.append_jinja_end()
