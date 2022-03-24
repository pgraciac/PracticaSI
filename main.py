import numpy as np
import pandas as pd

if __name__ == '__main__':
    legal_df = pd.read_json('/Logs/legal.json')
    legal_df.head()
    users_df = pd.read_json('/Logs/users.json')
    users_df.head()
