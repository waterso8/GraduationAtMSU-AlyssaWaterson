
# coding: utf-8

# In[ ]:

from scipy.stats import spearmanr, pearsonr
def calculate_pvalues(df,method = spearmanr):
    """
    Assumes df with only numeric entries clean of null entries. 
    Calls df in to perform spearmanr method from scipy.stats.
    Transposes the columns to provide p values for each column.
    """
    dfcols = pd.DataFrame(columns=df.columns)
    pvalues = dfcols.transpose().join(dfcols, how='outer')
    for r in df.columns:
        for c in df.columns:
            pvalues[r][c] = round(method(df[r], df[c])[1], 4)
    return pvalues

