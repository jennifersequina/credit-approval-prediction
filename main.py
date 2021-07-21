import pandas as pd
from pre_processing import pre_processing_app
from pre_processing import pre_processing_credit
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from approval import approval_decision
from manual_val import validation


df1 = pd.read_csv('/data/application_record.csv')
df_app = pre_processing_app(df1)

df2 = pd.read_csv('/data/credit_record.csv')
df_credit = pre_processing_credit(df2)

# merging two files
merged_df = pd.merge(df_app, df_credit, on='ID', how='left')

# impute NaN in credit history
merged_df['credit_rating'] = merged_df['credit_rating'].fillna(2).astype(int)

# approval decision
labeled_df = approval_decision(merged_df)
labeled_df['application_status'].value_counts()

# split the dataset to train and test
X = labeled_df.drop('application_status', axis=1)
Y = labeled_df['application_status']

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)

# machine learning models
dt = DecisionTreeClassifier()
lr = LogisticRegression()

dt.fit(x_train, y_train)
lr.fit(x_train, y_train)

dt.score(x_test, y_test)
lr.score(x_test, y_test)

# accuracy checked using machine learning models:
    # 58% for LR, 100% DT

# check the accuracy using the manual validation function

dt_val = validation(x_test, y_test, dt)
print(dt_val)

lr_val = validation(x_test, y_test, lr)
print(lr_val)





