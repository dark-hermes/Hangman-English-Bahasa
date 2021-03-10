import json
import pandas as pd
import string_formatter as strform

with open("english_raw.json", 'r') as read_json:
    data = json.load(read_json)

level_1, level_2, level_3  = {}, {}, {}
for word in data:
    
    if strform.level_1(word):
        level_1[word] = data[word]

    elif strform.level_2(word):
        level_2[word] = data[word]
    
    elif strform.level_3(word):
        level_3[word] = data[word]

for level in range(1,4):
    with open(f"english_level{level}.json", 'w') as write_json:
        exec(f"json.dump(level_{level}, write_json)")