from pathlib import Path

def load_notes(path='data/raw'):
    texts=[]
    for f in Path(path).glob('*.txt'): texts.append(f.read_text())
    return texts
