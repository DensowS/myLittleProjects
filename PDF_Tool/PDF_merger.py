from PyPDF2 import PdfReader, PdfWriter
import os

class PDFMerger:
    def merge_pdfs(self, pdf_paths, output_path):
        pdf_writer = PdfWriter()

        for path in pdf_paths:
            pdf_reader = PdfReader(path)
            for page in range(len(pdf_reader.pages)):
                pdf_writer.add_page(pdf_reader.pages[page])

        with open(output_path, 'wb') as out_pdf:
            pdf_writer.write(out_pdf)
