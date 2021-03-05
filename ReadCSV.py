
# coding: utf-8

# In[ ]:


def ReadCSV(csv):
    import pandas as pd
    import numpy as np 
    from sklearn import preprocessing
    import matplotlib.pyplot as plt 
    get_ipython().magic('matplotlib inline')
    import seaborn as sns #can i just say i REALLY hate how people import seaborn as sns. just import it as sbn COME ON
    from scipy.stats import spearmanr, pearsonr
    sns.set(style="white") #white background style for seaborn plots
    sns.set(style="whitegrid", color_codes=True)
    """
    Imports all future libraries
    Reads in CSV file according to Pandas library
    spits out file
    
    """
    file = pd.read_csv(csv)
    return file

