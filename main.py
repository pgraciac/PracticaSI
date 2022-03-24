import numpy as np
import pandas as pd

if __name__ == '__main__':
    legal_df = pd.read_json('/Logs/legal.json', orient = 'records')
    print(legal_df)

