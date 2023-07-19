from py_pdf_parser.loaders import load_file
from pathlib import Path
from pypdf import PdfReader

def extract_image(filename):
    # extract text from figures and tables py_pdf_parser
    '''
    document = load_file(Path(__file__).resolve().parent/ filename)
    table_captions = document.elements.filter_by_regex("Table*")
    tables = [document.elements.above(table_caption)[-1].text() for table_caption in table_captions]
    print(tables)    

    figure_captions = document.elements.filter_by_regex("Figure*")
    figures = [document.elements.above(figure_caption)[-1].text() for figure_caption in figure_captions]
    print(figures)
    '''

    # extract images using pypdf
    reader = PdfReader(Path(__file__).resolve().parent/ filename)
    count = 0
    for page in reader.pages:
        for image_file_object in page.images:
            with open(str(count) + image_file_object.name, "wb") as fp:
                fp.write(image_file_object.data)
                count += 1

    #return tables, figures

if __name__ == "__main__":
    extract_image("openai27052023.pdf")