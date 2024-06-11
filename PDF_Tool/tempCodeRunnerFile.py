        pdf_writer = PdfWriter()
        for pdf_path in pdf_paths:
            pdf_reader = PdfReader(pdf_path)
            for page_num in range(len(pdf_reader.pages)):
                pdf_writer.add_page(pdf_reader.pages[page_num])

        with open(output_pdf_path, 'wb') as out_pdf:
            pdf_writer.write(out_pdf)