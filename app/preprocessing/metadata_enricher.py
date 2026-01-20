from datetime import datetime
def enrich(c,s): return {'text':c,'source':s,'timestamp':datetime.now().isoformat()}
