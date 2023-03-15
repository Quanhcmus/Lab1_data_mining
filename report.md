

# Preprocessing and data mining

## Install WEKA (0.5 points)

### Requirement 1:
  - 20120554 ![Image 1](Images/20120554.png)
  - 20120563 ![Image 2](Images/20120554.png)

### Requirement 2:
  - **Current Relation**: abcd
  - **Attributes**: abcd
  - **Selected Attributes**: abcd
  - **Preprocess**: abcd
  - **More**: abcd 

## Getting Acquainted with WEKA (4.5 points)

### Exploring Breast Cancer data set
  - Load the data file **breast cancer.arf** ![cancer dataset](Images/load-breast-cancer-dataset.png)
  - **How many instances does this data set have?**
  There are 286 instances in this dataset
  ![Breast cancer 1](Images/Breast_cancer_1.png)
  - **How many attributes does this data set have?**
  There are 10 attributes in this dataset
  ![Breast cancer 2](Images/Breast_cancer_1.png)
  - **Which attribute is used for the label? Can it be changed? How?**
  *Class* is attributes used for the label, we can change by following these step:
     + Click *edit* button
        ![Breast cancer 2.1](Images/Breast_cancer_21.png)
     + Choose the label *class*
        ![Breast cancer 2.2](Images/Breast_cancer_22.png)
     + Select the cell which you want change
        ![Breast cancer 2.3](Images/Breast_cancer_23.png)
  - **What is the meaning of each attribute?**
     + **Age**: Patient's age include (10-19, 20-29, 30-39, 40-49, 50-59, 60-69, 70-79, 80-89, 90-99.)
     + **Menopause**: when your periods stop due to lower hormone levels. (lt40, ge40, premeno.)
     + **Tumor-size**: often measured in centimeters (cm) or inches. (0-4, 5-9, 10-14, 15-19, 20-24, 25-29, 30-34, 35-39, 40-44, 45-49, 50-54, 55-59.)
     + **Inv-nodes**: the number (range 0 - 39) of axillary lymph nodes that contain metastatic breast cancer visible on histological examination. (02,3-5, 6-8, 9-11, 12-14, 15-17, 18-20, 21-23, 24-26, 27-29, 30-32, 33-35, 36-39.)
     + **Node-caps**: if the cancer does metastasise to a. lymph node, although outside the original site of. the tumor it may remain “contained” by the cap- sule of the lymph node. (yes, no.)
     + **Deg-malig**:  the degree of malignancy of the tumor, which is also known as the tumor grade. (1, 2, 3.)
     + **Breast**: the breast location where the tumor was found. (left, right.)
     + **Breast.quad**: the quadrant of the breast where the tumor was found. (left-up, left-low, right-up, right-low, central.)
     + **Irradiat**: whether or not the patient received radiation therapy as part of their treatment for breast cancer. (yes, no.)
     + **Class**: indicates whether or not a patient experienced a recurrence of breast cancer after their initial treatment. (yes, no.)
  - **Let’s investigate the missing value status in each attribute and describe in general ways to solve the problem of missing values.**
     + **Node-caps**: 8 missing values
        ![Breast cancer 4.1](Images/Breast_cancer_41.png)
     + **Breast.quad**: 1 missing values
        ![Breast cancer 4.2](Images/Breast_cancer_42.png)
     + we can handle missing values by replaced with the property's mean
  - **Let’s propose solutions to the problem of missing values in the specific attribute.**
     + In **Node-caps** attributes we can replace with the most likely value infer from a Bayesian formula, decision tree or EM algorithm
     + In **Breast.quad** attributes we can replace with the property's mean
  - **Let’s explain the meaning of the chart in the WEKA Explorer. Setting the title for it and describing its legend.**
     + ![Breast cancer chart](Images/Breast_cancer_chart.png)
     + We can setting title chart is stacked bar chart
     + Red represents the patients recurrence-events
     + Blue represents the patients no-recurrence-events