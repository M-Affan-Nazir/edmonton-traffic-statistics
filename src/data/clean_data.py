def drop_columns(df, columns=[]):
    return df.drop(columns, axis=1)

def drop_all_null_rows(df):
    df_new = df.dropna(how="all")
    if len(df_new) != len(df):
        return df_new
        print("OK")
    return df

def drop_null_rows(df, columns):
    df_new = df.dropna(subset=columns)
    return df_new


def filter_dataframe(df, column, has_value):
    return df[df[column].str.lower().str.contains(has_value)]