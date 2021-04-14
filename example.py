#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""
__version__     =   "0.0.1"
__author__      =   "@didats"
__date__        =   "2021/04/14"
__description__ =   "PDF Form Filling Example file"
""" 

from formfilling import FormFilling

form = FormFilling()
data = """
field_name عندما يريد العالم أن ‪يتكلّم
field_email didats@gmail.com
"""
# Generate
# form.generate(_data_, _template_file_, _output_path_)
output = form.generate(data, "./template.pdf", "./")