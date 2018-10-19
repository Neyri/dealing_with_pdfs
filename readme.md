# Dealing with pdfs

This project allows you to :

* concatenate 2 pdf files
* extract pages from a pdf file



## Dependencies

To use these scripts, you will need to install PyPDF2

```bash
pip install PyPDF2
```





## Concatenating 2 pdf files

To concatenate 2 files, you just have to execute the script called concat_pdf.py and pass 

- the name of the 2 files you want to concatenate 
- the name of the output file

```bash
python concat_pdf.py path/file_name1.pdf path/file_name2.pdf /path/output_name.pdf
```



## Extracting pages from a pdf file

To extract pages from a pdf file, you just have to execute the script called extract_pages.py and pass:

- the name of the file you want to extract pages from
- the pages number to extract. The input 2;3;7-10 will extract pages 2, 3 et pages from 7 to 10 (included)
- the name of the output file

```bash
python extract_pages.py path/file_name.pdf pages_number /path/output_name.pdf
```



