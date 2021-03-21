import pandas as pd

def crop_data_extraction():
    crop_rqmt = {}
    df = pd.read_csv('crops_rqmt.csv', index_col='SN')
    df = df[['Crops', 'Avg Temp', 'Rainfall']]
    for i,j,k in df.values:
        crop_rqmt[i] = (j, k)
    return (crop_rqmt)
