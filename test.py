#test file
from almapipy import AlmaCnxn
import json

alma = AlmaCnxn('l7xx121cad15d0704e40ace2df0389961c43', data_format='json')

book = "9911361073703767"
bib_record = alma.bibs.catalog.get(book)
#parsed = json.loads(bib_record)
print(json.dumps(bib_record,indent = 4))
