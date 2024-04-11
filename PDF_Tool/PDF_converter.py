from docx2pdf import convert
from PyPDF2 import PdfReader, PdfWriter
import tempfile
import os

class PDFConverter:
    def convert_and_merge_docx_to_pdf(self, docx_paths, output_pdf_path):
        temp_dir = tempfile.mkdtemp()
        pdf_paths = []
        for docx_path in docx_paths:
            pdf_path = os.path.join(temp_dir, os.path.basename(docx_path) + ".pdf")
            convert(docx_path, pdf_path)
            pdf_paths.append(pdf_path)
        
        pdf_writer = PdfWriter()
        for pdf_path in pdf_paths:
            pdf_reader = PdfReader(pdf_path)
            for page_num in range(len(pdf_reader.pages)):
                pdf_writer.add_page(pdf_reader.pages[page_num])

        with open(output_pdf_path, 'wb') as out_pdf:
            pdf_writer.write(out_pdf)
