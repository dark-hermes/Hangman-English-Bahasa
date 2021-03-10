import pandas as pd
import string_formatter as strform
import json

# import data
data = pd.read_csv('indonesia_raw.csv')

# apply no_strip function
data = data[data["lema"].astype(str).apply(lambda word : strform.no_strip(word))]

# drop missing values, reset dataframe index, and convert whole data's data type to string
clean_data = data.dropna().reset_index(drop=True).astype(str)

# categorizing level of words and create json file each level
for level in range(1,4):
    # use function of each level from string_formatter to divide words to different levels
    exec(f"level_{level} = clean_data[clean_data.lema.apply(strform.level_{level})].reset_index(drop=True)")

    # 3 dictionary for word storage
    exec(f"level_{level}_dict = dict()")

    # store lema and nilai for each variable level
    exec(f'level_data = level_{level}.lema')
    for i in range(level_data.size):
        exec(f"level_{level}_dict[level_{level}.lema[{i}]] = [level_{level}.nilai[{i}]]")

    with open(f'indonesia_level{level}.json', 'w') as write_json:
        exec(f"json.dump(level_{level}_dict,write_json)")