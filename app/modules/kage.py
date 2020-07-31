# -*- coding: utf-8 -*-

"""
Convert Markdown files to HTML5 files.
"""

__author__ = "k.mp"

# generic | built-in imports
import os
from glob import iglob


# library imports
from markdown import markdownFromFile
from settings import basedir

# contents directory containing markdown files
contents_dir = os.path.abspath(os.path.join(basedir, "app/contents"))

# files match string
file_lookup = os.path.join(contents_dir, "*.md")

# templates directory path
template_dir = os.path.abspath(os.path.join(basedir, "app/templates/generated"))

# TODO// Refactor Kage.parse() function
# TODO// Add functionality to check if file exists and flash message


class Kage(object):

    # constructor
    def __init__(self):
        # file path registry
        self.paths_registry = [path for path in iglob(file_lookup)]

    @classmethod
    def extract_filename(cls, path):
        """
        Get filename from an absolute or relative path name
        :param path: string Relative ot Absolute path name
        :return: string file name
        """
        head, tail = os.path.split(path)
        return tail

    @classmethod
    def extract_filename_name(cls, filename):
        """
        From a filename, split and ge the name without extension
        :param filename: name of file
        :return:
        """
        name, extension = os.path.splitext(filename)
        return name

    @property
    def paths(self):
        """
        Get the file path registry
        :return: file path dictionary
        """
        return self.paths_registry

    def parse(self):
        if len(self.paths) != 0:
            for path in self.paths:
                # input filename absolute path
                input_name = path
                # output filename path
                filename = Kage.extract_filename(path)
                name = Kage.extract_filename_name(filename)
                output_name = os.path.join(template_dir, f"{name}.html")
                # encoding
                encoding = "utf-8"
                markdownFromFile(
                    input=input_name,
                    output=output_name,
                    encoding=encoding
                )
            return True
        return False


if __name__ == "__main__":
    kage = Kage()
    kage.parse()
