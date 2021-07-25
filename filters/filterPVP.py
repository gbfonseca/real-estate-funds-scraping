def filterPVP(data_frame):
    data_frame['P/VP'] = data_frame['P/VP'].astype(str)
    data_frame['P/VP'] = data_frame['P/VP'].str.replace(',', '.', regex=False)
    data_frame['P/VP'] = data_frame['P/VP'].astype(float) / 100
    filtered_data_frame = data_frame['P/VP'] <= 2
    data_frame.loc[filtered_data_frame]
    data_frame['P/VP'] = data_frame['P/VP'].astype(str)
    data_frame['P/VP'] = data_frame['P/VP'].str.replace('.', ',', regex=False)
    return data_frame
