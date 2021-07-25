def filterDY(data_frame):
    data_frame['Dividend Yield'] = data_frame['Dividend Yield'].str.rstrip('%')
    data_frame['Dividend Yield'] = data_frame['Dividend Yield'].str.replace(
        ',', '.', regex=False)
    data_frame['Dividend Yield'] = data_frame['Dividend Yield'].astype(
        float) / 100
    is_more_four_percent = data_frame['Dividend Yield'] >= 0.04
    data_frame.loc[is_more_four_percent]
    data_frame['Dividend Yield'] = data_frame['Dividend Yield'].astype(str)
    data_frame['Dividend Yield'] = data_frame['Dividend Yield'].str.replace(
        '.', ',', regex=False)
    return data_frame
