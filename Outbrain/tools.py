from sklearn import preprocessing

def normilize(df, exclude=[]):
    for col in df.columns:
        if not('_id' in col) and not(col in exclude):
            df[col] = preprocessing.StandardScaler().fit(df[[col]]).transform(df[[col]])
    return df        
        
def normilize_cols(df, cols):
    for col in cols:
        df[col] = preprocessing.StandardScaler().fit(df[[col]]).transform(df[[col]])
            
            
            

    