import sys
import PyPDF2


def get_pages_number(input_nb):
    pages_nb = []
    for i in range(len(input_nb)):
        if "-" in input_nb[i]:
            min, max = input_nb[i].split("-")
            min = int(min)
            max = int(max)
            pages_nb += [i for i in range(min, max + 1)]
        else:
            pages_nb.append(int(input_nb[i]))
    return pages_nb


def extract_pages(pages_nb, file_name):
    input_file = PyPDF2.PdfFileReader(file_name, strict=False)
    pages = []
    for page_nb in pages_nb:
        page = input_file.getPage(page_nb - 1)
        pages.append(page)
    return pages


def write_file(pages, output_name):
    new_file = PyPDF2.PdfFileWriter()
    for page in pages:
        new_file.addPage(page)
    with open(output_name, "wb") as output_file:
        new_file.write(output_file)


def main():
    # pages to extract format ex : 2;3;7-10
    if len(sys.argv) == 4:
        input_name = sys.argv[1]
        input_nb = sys.argv[2]
        output_name = sys.argv[3]
    else:
        input_name = input("Name of the file from which to extract pages: ")
        input_nb = input("Pages to extract (in format 2;3;7-10): ")
        output_name = input("Name of the new file to write: ")
    input_nb = input_nb.split(";")
    pages_nb = get_pages_number(input_nb)
    print("... Extracting pages : ", pages_nb)
    pages = extract_pages(pages_nb, input_name)
    write_file(pages, output_name)


if __name__ == "__main__":
    main()
