from PyPDF2 import PdfReader, PdfWriter
import os

class PDFSplitter:
    def split_pdf(self, file_path, page_counts, output_folder):
        pdf_reader = PdfReader(file_path)
        total_pages = len(pdf_reader.pages)
        start_page = 0

        for i, num_pages in enumerate(page_counts):
            pdf_writer = PdfWriter()
            end_page = min(start_page + num_pages, total_pages)

            for page in range(start_page, end_page):
                pdf_writer.add_page(pdf_reader.pages[page])

            output_filename = os.path.join(output_folder, f'{os.path.splitext(os.path.basename(file_path))[0]}_teil_{i + 1}.pdf')
            with open(output_filename, 'wb') as out:
                pdf_writer.write(out)

            start_page += num_pages

        if start_page < total_pages:
            pdf_writer = PdfWriter()
            for page in range(start_page, total_pages):
                pdf_writer.add_page(pdf_reader.pages[page])

            output_filename = os.path.join(output_folder, f'{os.path.splitext(os.path.basename(file_path))[0]}_teil_{len(page_counts) + 1}.pdf')
            with open(output_filename, 'wb') as out:
                pdf_writer.write(out)
