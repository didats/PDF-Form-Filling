#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""
__version__     =   "0.0.1"
__author__      =   "@didats"
__date__        =   "2021/04/14"
__description__ =   "PDF Form Filling Generator"
""" 

from pdfrw import PdfReader, PdfWriter, PageMerge, PdfDict, PdfObject, objects
import string
import random

class FormFilling:
    
    ANNOT_KEY = '/Annots'
    ANNOT_FIELD_KEY = '/T'
    ANNOT_VAL_KEY='/V'
    ANNOT_RECT_KEY = '/Rect'
    SUBTYPE_KEY = '/Subtype'
    WIDGET_SUBTYPE_KEY='/Widget'

    def write_fillable_pdf(self, input_pdf_path,output_pdf_path,data_dict):
        template_pdf=PdfReader(input_pdf_path)
        
        for index, _ in enumerate(template_pdf.pages):
            annotations = template_pdf.pages[index][self.ANNOT_KEY]
            if hasattr(annotations, "__len__"):
                for annotation in annotations:
                    if annotation[self.SUBTYPE_KEY]==self.WIDGET_SUBTYPE_KEY:
                        
                        if self.ANNOT_FIELD_KEY in annotation: 
                            key = annotation[self.ANNOT_FIELD_KEY][1:-1]
                            
                            if key in data_dict.keys():
                                value = data_dict[key]
                                if annotation["/FT"] == "/Tx":
                                    if value != "-":
                                        annotation.update(
                                            PdfDict(V='{}'.format(value.upper()))
                                        )
                                elif annotation["/FT"] == "/Btn" and value == "Yes":
                                    annotation.update(
                                        PdfDict(V=objects.pdfname.BasePdfName('/Yes'))
                                    )
                    annotation.update(PdfDict(Ff=1))

        template_pdf.Root.AcroForm.update(PdfDict(NeedAppearances=PdfObject('true')))
        PdfWriter().write(output_pdf_path,template_pdf)

    def toArray(self, data):
        items = {}
        alldata = data.splitlines()
        
        for item in alldata:
            itemData = item.split(" ")
            
            strData = ""
            for value in itemData:
                strData = strData + " " + value
            
            items[itemData[0]] = strData.replace(itemData[0], "").strip()
            
        return items

    def createFileName(self):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(10))

    def generate(self, fieldData, PDFTemplate, outputPath):
        
        filename = self.createFileName()
        data = self.toArray(fieldData)

        template = PDFTemplate
        output = outputPath + "/" + filename + ".pdf"
        
        self.write_fillable_pdf(template, output, data)
        
        return output
        


