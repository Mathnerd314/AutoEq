import sys
from pathlib import Path
import json
import re
import numpy as np
from autoeq.frequency_response import FrequencyResponse

with open('pathfinder_320_response.json', 'r') as f:
    json_data = json.load(f)

header = json_data['header']
data = np.array(json_data['data'])
frequency = data[:, header.index('Frequency')]
target = data[:, header.index('Target')]
col_ix = None
for col_name in ['Average Response']:
    if col_name in header:
        col_ix = header.index(col_name)
        break
if col_ix is None:
    raise ValueError('Could not find any of the data columns in JSON')

fr = FrequencyResponse(name='fr', frequency=frequency, raw=data[:, col_ix], target=target)
fr.interpolate()
fr.center()
fr.write_csv("fr.csv")
