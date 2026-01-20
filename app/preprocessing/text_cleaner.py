import re
def clean(t): return ' '.join(re.sub(r'[^a-zA-Z0-9 ]',' ',t).split())
