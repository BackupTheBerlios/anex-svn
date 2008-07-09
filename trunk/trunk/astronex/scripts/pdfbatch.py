# -*- coding: utf-8 -*-
from scripts import Script
       
class PdfBatch(Script):
    def run(self,*arg,**kw):
        from .. surfaces.pdfsurface import DrawPdf
        DrawPdf.simple_batch()

pdfbatch = PdfBatch
