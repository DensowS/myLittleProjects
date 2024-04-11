import tkinter as tk
from tkinter import filedialog, messagebox
from PDF_split import PDFSplitter
from PDF_converter import PDFConverter
from PDF_merger import PDFMerger
import os

class PDFToolsApp:
    def __init__(self, root):
        self.root = root
        self.splitter = PDFSplitter()
        self.converter = PDFConverter()
        self.merger = PDFMerger()
        self.file_paths = []
        self.setup_main_menu()

    def setup_main_menu(self):
        self.root.title("PDF Werkzeuge")
        self.root.geometry("640x480")
        tk.Button(self.root, text="PDF Konverter", command=self.open_converter).pack(pady=10)
        tk.Button(self.root, text="PDF Teilen", command=self.open_splitter).pack(pady=10)
        tk.Button(self.root, text="PDF Zusammenführen", command=self.open_merger).pack(pady=10)

    # CONVERTER
    def open_converter(self):
        converter_window = tk.Toplevel(self.root)
        converter_window.title("PDF Konverter")
        converter_window.geometry("400x300")
        self.file_paths_var = tk.StringVar(converter_window)
        entry = tk.Entry(converter_window, textvariable=self.file_paths_var, width=50)
        entry.pack(pady=10)
        tk.Button(converter_window, text="Dateien auswählen", command=self.choose_files).pack()
        tk.Button(converter_window, text="Zu PDF konvertieren", command=self.convert_to_pdf).pack(pady=20)

    def choose_files(self):
        file_paths = filedialog.askopenfilenames(filetypes=[("Word documents", "*.docx")])
        if file_paths:
            self.file_paths = file_paths
            self.file_paths_var.set("; ".join(file_paths))

    def convert_to_pdf(self):
        if self.file_paths:
            output_pdf_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
            if output_pdf_path:
                self.converter.convert_and_merge_docx_to_pdf(self.file_paths, output_pdf_path)
                messagebox.showinfo("Erfolg", "Dateien wurden erfolgreich zu PDF konvertiert und zusammengeführt.")
        else:
            messagebox.showerror("Fehler", "Bitte wählen Sie zuerst DOCX Dateien aus.")

    # SPLITTER
    def open_splitter(self):
        splitter_window = tk.Toplevel(self.root)
        splitter_window.title("PDF Teilen")
        splitter_window.geometry("400x300")
        self.pdf_path_var = tk.StringVar(splitter_window)
        tk.Entry(splitter_window, textvariable=self.pdf_path_var, width=50).pack(pady=10)
        tk.Button(splitter_window, text="PDF auswählen", command=self.choose_pdf).pack()
        self.page_numbers_var = tk.StringVar(splitter_window)
        tk.Entry(splitter_window, textvariable=self.page_numbers_var, width=50).pack(pady=10)
        tk.Label(splitter_window, text="Seitenzahlen (durch Komma getrennt, z.B. 1,3,5)").pack()
        tk.Button(splitter_window, text="PDF teilen", command=self.split_pdf).pack(pady=20)

    def choose_pdf(self):
        pdf_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if pdf_path:
            self.pdf_path_var.set(pdf_path)

    def split_pdf(self):
        pdf_path = self.pdf_path_var.get()
        page_numbers_str = self.page_numbers_var.get()
        page_numbers = [int(n) for n in page_numbers_str.split(',') if n.isdigit()]
        if pdf_path and page_numbers:
            output_folder = filedialog.askdirectory()
            if output_folder:
                self.splitter.split_pdf(pdf_path, page_numbers, output_folder)
                messagebox.showinfo("Erfolg", "PDF wurde erfolgreich geteilt.")
        else:
            messagebox.showerror("Fehler", "Bitte geben Sie den Pfad und die Seitenzahlen korrekt ein.")

    # MERGER
    def open_merger(self):
        merger_window = tk.Toplevel(self.root)
        merger_window.title("PDF Zusammenführen")
        merger_window.geometry("500x400")

        self.pdf_listbox = tk.Listbox(merger_window, width=50, height=15)
        self.pdf_listbox.pack(pady=10)

        tk.Button(merger_window, text="PDF hinzufügen", command=self.add_pdf).pack()
        tk.Button(merger_window, text="Ausgewähltes PDF entfernen", command=self.remove_selected_pdf).pack()
        tk.Button(merger_window, text="PDFs zusammenführen", command=self.merge_pdfs).pack(pady=20)

        self.pdf_listbox.bind('<Button-1>', self.start_move)
        self.pdf_listbox.bind('<ButtonRelease-1>', self.stop_move)
        self.pdf_listbox.bind('<B1-Motion>', self.do_move)
        
    def merge_pdfs(self):
        pdf_paths = [self.pdf_listbox.get(idx) for idx in range(self.pdf_listbox.size())]
        if pdf_paths:
            output_pdf_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
            if output_pdf_path:
                self.merger.merge_pdfs(pdf_paths, output_pdf_path)
                messagebox.showinfo("Erfolg", "PDFs wurden erfolgreich zusammengeführt.")
        else:
            messagebox.showerror("Fehler", "Bitte fügen Sie zuerst PDF-Dateien hinzu.")

    def add_pdf(self):
        pdf_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if pdf_path:
            self.pdf_listbox.insert(tk.END, pdf_path)

    def remove_selected_pdf(self):
        try:
            selected_index = self.pdf_listbox.curselection()[0]
            self.pdf_listbox.delete(selected_index)
        except IndexError:
            pass 

    def start_move(self, event):
        self._drag_start_index = self.pdf_listbox.nearest(event.y)

    def stop_move(self, event):
        self._drag_stop_index = self.pdf_listbox.nearest(event.y)
        if self._drag_start_index != self._drag_stop_index:
            moving_item = self.pdf_listbox.get(self._drag_start_index)
            self.pdf_listbox.delete(self._drag_start_index)
            self.pdf_listbox.insert(self._drag_stop_index, moving_item)

    def do_move(self, event):
        pass


if __name__ == "__main__":
    root = tk.Tk()
    app = PDFToolsApp(root)
    root.mainloop()
