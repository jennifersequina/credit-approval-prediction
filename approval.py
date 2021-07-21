import pandas as pd
import numpy as np

# label the dataset if approved or not based on below parameters
        # credit_rating = 1 (good - 80%), 2 (no History)
        # high_income = 1
        # fixed_income = 1
        # employed = 1

def approval_decision(df: pd.DataFrame) -> pd.DataFrame:
    df['application_status'] = '0'
    conditions = [
        (df['credit_rating'] > 0) & (df['high_income'] == 1) & (df['fixed_income'] == 1) & (df['employed'] == 1)
    ]
    choices = [
        '1'
    ]
    df['application_status'] = np.select(conditions, choices)
    return df
