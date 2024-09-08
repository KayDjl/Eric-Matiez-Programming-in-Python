import json

pipa = [1,3,2,4,5,5,6]
filename = '../text_file/pip.json'
with open(filename, 'w') as f:
    json.dump(pipa, f)
    
