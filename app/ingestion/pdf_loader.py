from PyPDF2 import PdfReader

def load_pdf(path): r=PdfReader(path); return ' '.join(p.extract_text() for p in r.pages)
