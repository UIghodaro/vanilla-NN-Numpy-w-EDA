# A Newbie Made Neural Network
 A Personal Project created with the aim of properly understanding the workings of NNs in practice, as well as to self-teach numpy, pandas, matplotlib and basic data analysis techniques.

# Dependencies
Numpy, Pandas, Kagglehub with Pandas adapter 

Specifically for EDA (Exploratory Data Analysis):
Kaggle: "pip install kaggle"
Jupyter Labs: "pip install jupyterlab"
Matplotlib: "pip install matplotlib"
Seaborn: "pip install seaborn"


# The Dataset
Using the Telco Customer Churn dataset found on Kaggle: https://www.kaggle.com/datasets/blastchar/telco-customer-churn/data

Goal: Classify which customers will churn and predict behaviour to retain customers
The dataset is downloaded

## Kaggle API Setup and dataset download

This project uses the Kaggle API to download the Telco Customer Churn dataset. To get started:

1. **Obtain your API token**  
   - Go to [Kaggle → My Account → API] (https://www.kaggle.com/), click “Create New API Token,” and download the `kaggle.json` file.

2. **Create necessary folders and place your token in the project**  
   - Create 2 directories `.kaggle` and `data/raw` in the root of the repo:  
     ```bash
     mkdir .kaggle
     mkdir data/raw
     ```  
   - Copy your downloaded `kaggle.json` into the folder `.kaggle`:  
     ```bash
     cp /path/to/kaggle.json .kaggle/kaggle.json
     ```  

3. **Download the dataset into data/raw by running the EDA Jupyter Notebook**  
   The 2nd cell in the file EDA.ipynb is used to download the dataset into the folder `data/raw`. The following is the expected code, in case troubleshooting is needed:  
   ```python
   import os
   workingdir = os.path.dirname(os.getcwd()) 
   os.environ["KAGGLE_CONFIG_DIR"] = os.path.join(workingdir,'.kaggle')
   ```


# Credits
Credits to 3Blue1Brown on youtube for intuition on Neural Networks and stochastic gradient descent via back propagation.
Credits to BLASTCHAR on Kaggle for the provided dataset
