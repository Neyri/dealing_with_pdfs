import sys
import PyPDF2

if __name__ == '__main__':
    if len(sys.argv) == 4:
        output_name = sys.argv[-1]
        file_names = sys.argv[1:-1]
    else:
        file_name1 = input("Name of the first file to concatenate: ")
        file_name2 = input("Name of the second file to concatenate: ")
        output_name = input("Name of the new file to write: ")
        file_names = [file_name1, file_name2]
    new_file = PyPDF2.PdfFileMerger(strict=False)
    for file_name in file_names:
        if len(file_name) < 4 or file_name[-4:] != ".pdf":
            raise Exception(
                "You need to give the name of pdf files : " + file_name)
        new_file.append(file_name)
    output_file = open(output_name, 'wb')
    new_file.write(output_file)
