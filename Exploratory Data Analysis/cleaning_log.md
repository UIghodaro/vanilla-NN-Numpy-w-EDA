### Differences between raw data and lightly cleaned csvs
1. Datatype of Total Charges converted to float64
2. Rows with null/missing Total Charges values dropped; 11 rows removed
3. 1 outlier/erroneous row removed as a person was charged at abnormal rates 
4. CustomerID column dropped

### Differences between lightly cleaned and engineered csvs
1. 2 new columns added for classifications:
    - 'Tenure Bins' [from **x-1** to **x** months] -> '1 Month, 6 Months, 12 Months, 2 years, 4 years'
    - 'Monthly Charges Bins' [Quartiles] -> 'Low Monthly Charges, Mid Monthly Charges, High Monthly Charges'
    
