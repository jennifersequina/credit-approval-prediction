import pandas as pd
import numpy as np


def validation(test_df: pd.DataFrame, test_labels: pd.Series, ml_model) -> float:
    # prepares y_test (series to df)
    new_y = test_labels.to_frame(name='real_value').reset_index().rename(columns={'index': 'ID'})

    # write predictions to y_test
    new_y['predictions'] = ml_model.predict(test_df)

    # check the percentage of matched predictions and real value
    new_y['valid'] = np.where(new_y['predictions'] == new_y['real_value'], 1, 0)
    count_valid = new_y['valid'].sum().astype(float)
    total_count = new_y['valid'].count().astype(float)
    result = np.round(count_valid / total_count, 2)
    return result
