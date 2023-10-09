from PyPDF2 import PdfMerger

pdfs = ["Document1.pdf", "Document2.pdf","Document3.pdf"]

merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("merged.pdf")
merger.close()

