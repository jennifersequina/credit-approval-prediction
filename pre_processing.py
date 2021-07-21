import pandas as pd
import numpy as np

def pre_processing_app(df: pd.DataFrame) -> pd.DataFrame:
    df = df[['ID', 'FLAG_OWN_CAR', 'FLAG_OWN_REALTY', 'AMT_INCOME_TOTAL', 'NAME_INCOME_TYPE', 'DAYS_EMPLOYED']]
    df['high_income'] = np.where(df['AMT_INCOME_TOTAL'] < 100000, 0, 1) #select
    df['fixed_income'] = np.where(df['NAME_INCOME_TYPE'] == 'Working', 1, 0) #if 2 values - 1 column, if more than 2,separete
    df['employed'] = np.where(df['DAYS_EMPLOYED'] < 0, 1, 0)
    df['car_owner'] = np.where(df['FLAG_OWN_CAR'] == 'Y', 1, 0)
    df['realty_owner'] = np.where(df['FLAG_OWN_REALTY'] == 'Y', 1, 0)

    df.drop(['FLAG_OWN_CAR', 'FLAG_OWN_REALTY', 'AMT_INCOME_TOTAL', 'NAME_INCOME_TYPE', 'DAYS_EMPLOYED'],
            axis=1,
            inplace=True,
            errors='ignore')
    return df

# just for checking:
# df_app = pd.read_csv('~/Desktop/Projects/Credit Card Approval Prediction/application_record.csv')
# df_app2 = pre_processing_app(df_app)
# print(df_app2.head())

def pre_processing_credit(df: pd.DataFrame) -> pd.DataFrame:
    df = df.loc[(df.STATUS != "X")]
    df['status_c'] = np.where(df['STATUS'] == 'C', 1, 0)
    df = df.groupby('ID').agg(count_loans=('status_c', 'count'),
                              count_c=('status_c', 'sum'))
    df['status_c_rate'] = round(df['count_c']/df['count_loans'], 2)
    df['credit_rating'] = np.where(df['status_c_rate'] >= 0.80, 1, 0).astype(int)
    df.reset_index(inplace=True)
    df.drop(['count_loans', 'count_c', 'status_c_rate'], axis=1, inplace=True, errors='ignore')
    return df

# just for checking:
# df = pd.read_csv('~/Desktop/Projects/Credit Card Approval Prediction/credit_record.csv')
# df2 = pre_processing_credit(df)
# print(df2.head())



