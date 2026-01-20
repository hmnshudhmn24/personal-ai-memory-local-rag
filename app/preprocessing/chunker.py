def chunk(t,size=300,overlap=50):
    out=[]; i=0
    while i<len(t): out.append(t[i:i+size]); i+=size-overlap
    return out
