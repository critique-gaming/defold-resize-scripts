#!/usr/bin/env python

import deftree
import os
import sys
import glob

def scale_vec(el, factor):
    el.set_attribute("x", el.get_attribute("x").value * factor)
    el.set_attribute("y", el.get_attribute("y").value * factor)

if __name__ == "__main__":
    project_dir = sys.argv[1]
    font_name = sys.argv[2]
    scale_factor = float(sys.argv[3])

    def resize_in_gui(filename):
        print("Parsing " + filename)

        tree = deftree.parse(filename)
        root = tree.get_root()

        for el in root.iter_elements("nodes"):
            attr_type = el.get_attribute("type")
            attr_font = el.get_attribute("font")
            if attr_type.value == "TYPE_TEXT" and attr_font != None and attr_font.value == font_name:
                scale_vec(el.get_element("scale"), scale_factor)
                scale_vec(el.get_element("size"), 1.0 / scale_factor)

        tree.write(filename)

    os.chdir(project_dir)
    for filename in glob.glob("**/*.gui", recursive=True):
        resize_in_gui(filename)