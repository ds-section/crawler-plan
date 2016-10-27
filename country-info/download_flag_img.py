import requests
import pandas as pd
import numpy as np

# to read country_code as object type, set dtype = np.object type
df = pd.read_csv('flag_link.csv', sep=',', dtype=np.object)

# set country_code and flag_link to 2 list
code_list = df['country_code'].tolist()
flag_link_list = df['country_flag_link'].tolist()

for i in range(0, len(flag_link_list)):

    code = code_list[i]
    file_path = 'flag-image/' + code + '.png'
    url = flag_link_list[i]
    r = requests.get(url)

    print('country_code:' , code, ', status: ', r.status_code)

    if r.status_code == 200:

        with open(file_path, 'wb') as f:
            f.write(r.content)