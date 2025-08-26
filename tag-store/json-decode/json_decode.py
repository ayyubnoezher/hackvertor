import json

def _to_text(x):
    try:
        return x.decode('utf-8')
    except:
        return str(x)

s = _to_text(input)           
obj = json.loads(s)           
output = json.dumps(         
    obj, 
    indent=2, 
    ensure_ascii=False
)
