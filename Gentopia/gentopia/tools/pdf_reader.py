import PyPDF2


class PDFReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_pdf(self):
        text = ""
        with open(self.file_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfFileReader(file)
            for page_num in range(pdf_reader.numPages):
                page = pdf_reader.getPage(page_num)
                text += page.extractText()

        return text

    @classmethod
    def main(cls, file_path):
        pdf_reader = cls(file_path)
        text = pdf_reader.read_pdf()
        return text


if __name__ == "__main__":
    pdf_file_path = 'example.pdf'
    res = PDFReader.main(pdf_file_path)
    print(res)
