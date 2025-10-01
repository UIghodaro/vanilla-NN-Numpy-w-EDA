# Vanilla Neural Network with Exploral Data Analysis on Finance Dataset
 A Personal Project created with the aim of properly understanding the workings of NNs in practice, as well as to self-teach numpy, pandas, matplotlib and basic data analysis techniques.\
 **Disclaimer:** *Due to this project being done from a learner's perspective, the Exploral Data Analysis notebook may read as one of someone making findings in how pandas and matplotplib works alongside data findings - rather than a succinct, workplace ready data analysis.*\
Of course, the notebook is still cleaned for concisety.

## What is included
This project aims to emulate a data analysis to ML pipeline that may be seen in the workplace.
- ``ExploratoryDataAnalysis\EDA.ipynb`` -> Data Analysis/Exploration notebook, cleaning_log.md describing what it changed
   - Running the entire notebook generates 3 CSVs in ``data`` [see Setup if ``data`` is not a folder] which is needed before executing Machine learning files
- ``Machine-Learning\Models.py`` -> Initialises Logistic Regression, Random Forest and a Pytorch FF NN as classes for readability
- ``Machine-Learning\Train.py`` -> Trains ML models from ``Models.py`` on data

# Setup
## 1 - Requirements


## 2 - Kaggle API Setup and dataset download
Using the Telco Customer Churn dataset found on Kaggle:\ https://www.kaggle.com/datasets/blastchar/telco-customer-churn/data\
Goal: Classify which customers will churn and predict behaviour to retain customers

This project uses the Kaggle API to download the dataset. To get started:

1. **Obtain your API token**  
   - Go to [Kaggle → Settings → Account → API] (https://www.kaggle.com/), click 'Create New Token' to download the `kaggle.json` file.

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
