import fitz
import os


class ConvertFile:

    # default constructor
    def __init__(self, file_name, type_file, file_start=0, file_end=0):
        self.file_name = file_name
        self.type_file = type_file
        self.file_start = file_start
        self.file_end = file_end

    # a method for printing data members
    def print_args(self):
        print(self.file_name, self.type_file, self.file_start, self.file_end)

    def open_file(self):
        if not self.file_name:
            doc = get_filename()
        try:
            doc = fitz.open(self.file_name)
        except RuntimeError:
            print(
                f'\nError ind pdfCropMargins: The program could nor read \n{doc}')
            ex.cleanup_and_exit(1)
        return doc

    def convert_pdf(self):
        doc = self.open_file()
        print(type(doc))
        cont = 0
        page_start = self.file_start
        page_end = self.file_end
        matriz = fitz.Matrix(10, 10)
        if(page_start != 0 and page_end):
            page_start -= 1
        for p in range(page_start, page_end):
            p = doc.loadPage(p)
            pix = p.getPixmap(matrix=matriz)
            pix.writePNG(str(self.file_name)+'-page-%i' % p.number)


if __name__ == '__main__':
    pdf = 'como_programar_cpp.pdf'

    obg = ConvertFile(pdf, 'jpg', 1, 16)
    obg.convert_pdf()
