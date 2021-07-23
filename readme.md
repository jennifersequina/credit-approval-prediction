## Credit Card Approval Prediction

### Description:
This project is about predicting the status of credit card application based on the information provided by the client and the credit history available. Note that the datasets have no labels yet, so I need to do it myself by making parameters.
The type of this machine learning is classification which is about predicting label.

This package contains the 2 datasets and 4 python files:
1. application_record.csv
2. credit_record.csv
3. main.py
4. pre_processing.py
5. approval.py
6. manual_val.py

### Methodology:
This section explains the procedures done in completing this project.

1. Identifying which information will be helpful in predicting the credit card application based on the 2 datasets.
   - application_record.csv: I only to get the ID, income, type of income, employment status.
    - credit_record.csv: ID and the status of each loan would be useful (whether it was paid off the same month or it was overdue for couple of days)
    

2. Cleaning up the 2 datasets to make it useful in making the model.
    - pre_processing.py: in this python file, I created 2 functions to clean up each dataset.
    - pre_processing_app: I converted the important columns to binary, then drop the columns which is not relevant in making approval decision.
    - pre_processing_credit: I filtered out the 'X' status as this only indicate that there's no existing loan in the current month (0). Then converted the column 'STATUS' to binary. Here I decided to have status C as 1 (means they paid off loan the same month), others as 0 (means their loans went overdue). Then grouped by 'ID' to get the count per status. Finally, to assess the credit performance of each client, I calculated the number of '1' out of the total loans they had then created another binary label whether good or bad (1, 0). I put a threshold of 80% of paid off loans within the month to be considered as 'good'.
    

3. Creating parameters for the approval of application. 
   - approval.py: in this python file I created a function to assess whether the client will get approve or not based on below parameters:
        1. credit_rating = 1 and 2 (1 - good 80%), (2 - clients with no history, this is to give them chance to be assessed based on the next parameters)
       2. high_income = 1
       3. fixed_income = 1 
       4. employed = 1
    

4. Creating a labeled datasets based on the approval decision created above.
    - main.py: in this python file, firstly I merged the pre-processed datasets and fill the nan values in 'STATUS' with 2 as indicator the client has no credit history. Then I applied the approval_decision function to have it labeled whether 'Approved' (1) or 'Rejected' (0).
    Now that I have labeled data this can be used in building the machine learning model and training it.
      

5. Building a machine learning model suitable for the objective. As this is a classification, I chose to check the Decision Tree Classifier and Logistic Regression.
     - main.py: I split the datasets 80% for training and 20% for testing.
    - I used two models: DecisionTreeClassifier and LogisticRegression from sklearn library.
    - I fit the train datasets for both models then I checked the accuracy by using the score method against the test data. 
      
    Results:
    - 58% for LogisticRegression
    - 100% for DecisionTreeClassifier
    

6. Add-ons: Creating function for manual validation of the two models.
    - manual_val.py: I created a function to manually validate the model I am using. There has been a preparation of datasets, and I used predict method and check the percentage of matched predictions and real value.
    
    Results:
    - 58% for LogisticRegression
    - 100% for DecisionTreeClassifier
    
Note: I am getting 100% using the DecisionTreeClassifier as the model  is capturing the same parameters that I used in the approval_decision function.

### Usage:
This package can be used to the new application records to make a prediction whether the it will be approved or rejected. The parameters can be also adjusted in the approval.py, and the manual_val can be used to different machine learning model to check the accuracy.
    
    
    


