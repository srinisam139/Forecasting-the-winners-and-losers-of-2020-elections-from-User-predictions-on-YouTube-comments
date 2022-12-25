NOTE: IF YOU ARE RUNNING GOOGLE COLAB OPEN FROM RIT EMAIL ID
There are totally 7 Jupyter Notebook to run.

- Unzip the Forecasting zip file.
- Open the Forecasting folder

STEP 1:
- Data Extraction file is used to extract the relevant data from 2 billions comments stored as json files.
- There are totally three datasets but we will be using only Forecasting_CNN.csv and Forecasting_MSNBC.csv 
- DO NOT RUN DATA_EXTRACTION.ipynb, THIS IS JUST TO SHOW DATASET IS EXTRACTED FROM THE WEB SCRAPED DATA.

STEP 2:
- Open Preprocessing.ipynb file in your local environment
- If you opened in Local Environment follow the steps below,
    1) Once the file is opened run all the cells.
    2) The preprocessed file will be stored in the Output folder as "preprocessing_CNN.csv".
    
                              (or)
                              
- use the following google colab link to open the file 
"https://drive.google.com/file/d/10WFbJYJ5-bGeeItmgGEFkin_Iy95jgP3/view?usp=sharing"
- If you opened in Google Colab Environment follow the steps below,
    1) Upload "Forecasting_CNN.csv" to the google colab environment, wait until it pops up on the left side.
    2) Run all the cells.
    3) Output file will be generated on the left column of the google colab as "preprocessing_CNN.csv"
    4) Download the "preprocessing_CNN.csv" file and store it in your local. 
    
STEP 3:
- Open Data_Exploratory.ipynb file in your locan environment
- If you opened in Local Environment follow the steps below,
    1) Once the file is opened run all the cells.
    2) All the graphs will be displayed below the respective cell.
    3) There is a preprocessing again involved here, so a file will be generated on the Output folder named "trimmed_pre_election_punctuation_CNN_20.csv"
    
                            (or)
                            
- use the following google colab link to open the file
  "https://drive.google.com/file/d/1W9RJQE98zoCjK00s1tG6YTbCpXmiiQsY/view?usp=sharing"
- If you opened in Google Colab Environment follow the steps below,
    1) Upload the stored "preprocessing_CNN.csv" from your local to the google colab environment, wait until it pops up on the left side.
    2) Run all the cells.
    3) All the graphs will be displayed below the respective cell.
    4) Output file will be generated on the left colum of the google colab as "trimmed_pre_election_punctuation_CNN_20.csv"
    5) Download the "trimmed_pre_election_punctuation_CNN_20.csv" file and store it in your local.
    
STEP 4:
- Open Topic_Modeling.ipynb file in your local environment.
-   WARNING: HIGH GPU REQUIRED TO RUN THIS STEP IF IT IS NOT RUNNING IN LOCAL, PLEASE USE THE GOOGLE COLAB LINK.
    1) Once the file is opened run all the cells.
    2) Following Output files will be generated "topic_model_2500", "topic_model_2500_dataframe.csv", "topic_model_2500_info.csv".
    3) Clustered Topics and Topic number '0' top 10 words will be generated. Here Topic Number '0' Points to TRUMP Cluster and '1' Points to Biden Cluster.

                            (or)

- use the following google colab link to open the file
"https://drive.google.com/file/d/1OuokC6PZPnSJd1puZzKFekcbS16GTfy-/view?usp=sharing"
- If you opened in Google Colab Environment follow the steps below,
    1) Upload the stored "trimmed_pre_election_punctuation_CNN_20.csv" from your local to the google colab environment, wait until it pops up on the left side.
    2) Run all the cells.
    3)Following Output files will be generated "topic_model_2500", "topic_model_2500_dataframe.csv", "topic_model_2500_info.csv" on the left column of the Google Colab.
    4) Clustered Topics and Topic number '0' top 10 words will be generated. Here Topic Number '0' Points to TRUMP Cluster and '1' Points to Biden Cluster.
    5) Download all the following files "topic_model_2500", "topic_model_2500_dataframe.csv", "topic_model_2500_info.csv" and store it in your local folder.
    
STEP 5:
- Open Sentiment_Analyzer.ipynb file in your local environment.
    1) Once the file is opened run all the cells.
    2) Output file named "combined_sentiment.csv" will be generated and stored in the Ouput folder.
    3) A random sample of 100 comments is human annotated to check the accuracy (73%). The file named "sentiment_target" is stored in the Data Folder
    
                            (or)
             
- use the following google colab link to open the file
"https://drive.google.com/file/d/11k_9gVXKgw7yi42FGDzAS5Q7Kw6icKV6/view?usp=sharing"
- If you opened in Google Colab Environment follow the steps below,
    1) Upload the stored "topic_model_2500_dataframe.csv" from your local to the google colab environment, wait until it pops up on the left side.
    2) Run all the cells.
    3) Following Ouput file "combined_sentiment.csv" will be generated on the left side of the google colab environment.
    4) Downlaod the "combined_sentiment.csv" file and store in your local folder.
    5) A random sample of 100 comments is human annotated to check the accuracy (73%). The file named "sentiment_target" is stored in the Data Folder
    
STEP 6:
- Open Unsupervised_Learning.ipynb file in your local environment.
    WARNING: HIGH GPU REQUIRED TO RUN THIS STEP IF IT IS NOT RUNNING IN LOCAL, PLEASE USE THE GOOGLE COLAB LINK.
    1) Once the file is opened run all the cells.
    2) A output file named "labeled_votes.csv" will be generated and stored in the Output folder.
    3) Winner of the 2020 Presidential election will be shown in the plotly graph in form of barchart.
        i)First Bar chart indicates the 15 days timeline of votes before November 3rd 2020 between Trump and Biden.
        ii) Second Barc chart indicates the overall in the span of 15 days before the presidential election.
    4) A random sample of 100 comments is labeled in the following path "Data/unsupervised_sample_labeled.csv" to check the accuracy score.
                         (or)
                         
- use the following google colab link to open the file
"https://drive.google.com/file/d/12iKiXJtMr2l8XLl7IG_Zg3lIXBkemJNQ/view?usp=sharing"
- If you opened in Google Colab Environment follow the steps below,
    1) Upload the stored "trimmed_pre_election_punctuation_CNN_20" from your local to the google colab environment, wait until it pops up on the left side.
    2) Run all the cells
    3) A output file named "labeled_votes.csv" will be generated on the left side on the google colab.
    4) Winner of the 2020 Presidential election will be shown in the plotly graph in form of barchart.
        i)First Bar chart indicates the 15 days timeline of votes before November 3rd 2020 between Trump and Biden.
        ii) Second Barc chart indicates the overall in the span of 15 days before the presidential election.
    5) A random sample of 100 comments is labeled in the following path "Data/unsupervised_sample_labeled.csv" to check the accuracy score.
    6) Make sure to download the "labeled_votes.csv" file.
    
    
STEP 7:

WARNING: USE ONLY GOOGLE COLAB TO RUN THE FOLLOWING CODE
"https://drive.google.com/file/d/1rVLbKAn9-zxRTaogGCPX_vamuPTidFN0/view?usp=sharing"
- If you opened in Google Colab Environment follow the steps below,
    1) Upload the following files to the google colab environment Preprocessing.py, Data_Exploratory.py, labeled_votes.csv and Forecasting_MSNBC.csv files and wait until it pops up on the left side or click refresh.
    2) Run only tht first cell.
    WARNING: AFTER INSTALLING TENSORLFOW_TEXT restart the environment
    WARNING: ONCE RESTARTED THE ENVIRONEMNT PLEASE DONT RUN THE FIRST CELL AGAIN AND RUN THE REMAINING CELL
    3) Run all the cells
    4) Following OUTPUT files will be generated on the left column validation_predicted_df.csv, preprocess_test_Forecasting_MSNBC.csv and testing_predicted_df.csv 
    4) The testing_predicted_df.csv is the predicted test output file for MSNBC corpus. The random sample of 100 comments is in the following path "Data/labeled_test_data.csv".