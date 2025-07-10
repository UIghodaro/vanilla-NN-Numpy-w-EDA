#Main Neural Network file. This is where all the magic will happen!

# Import Numpy
import numpy as np

# Other imports entirely for dataset integration and handling 
import pandas as pd
import kagglehub
from kagglehub import KaggleDatasetAdapter
import pickle

# Set the path to the telco-customer-churn dataset downloaded
file_path = ""

#Loads the dataset into a python object under the pandas framework for manipulation
df = kagglehub.load_dataset(
  KaggleDatasetAdapter.PANDAS,
  "blastchar/telco-customer-churn",
  file_path,
  # Provide any additional arguments like 
  # sql_query or pandas_kwargs. 
  # Documatation: https://github.com/Kaggle/kagglehub/blob/main/README.md#kaggledatasetadapterpandas
)


