#!/usr/bin/env python

import deftree
import os
import sys
import glob

def scale_vec(el, factor):
    if el != None:
        el.set_attribute("x", el.get_attribute("x").value * factor)
        el.set_attribute("y", el.get_attribute("y").value * factor)

def scale_vec4(el, factor):
    if el != None:
        el.set_attribute("x", el.get_attribute("x").value * factor)
        el.set_attribute("y", el.get_attribute("y").value * factor)
        el.set_attribute("z", el.get_attribute("z").value * factor)
        el.set_attribute("w", el.get_attribute("w").value * factor)

if __name__ == "__main__":
    project_dir = sys.argv[1]
    scale_factor = float(sys.argv[2])

    def resize_in_gui(filename):
        print("Parsing " + filename)

        tree = deftree.parse(filename)
        root = tree.get_root()

        for el in root.iter_elements("nodes"):
            scale_vec(el.get_element("size"), scale_factor);
            scale_vec(el.get_element("position"), scale_factor);
            scale_vec4(el.get_element("slice9"), scale_factor);

        tree.write(filename)

    os.chdir(project_dir)
    for filename in glob.glob("**/*.gui", recursive=True):
        resize_in_gui(filename)