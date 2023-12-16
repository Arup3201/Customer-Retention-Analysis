# Customer Retention Analysis

## Dataset

Name: **Bank Customer Churn Prediction**

Link: [Bank Customer Churn Dataset | Kaggle](https://www.kaggle.com/datasets/gauravtopre/bank-customer-churn-dataset)

## About the dataset

This dataset is for ABC Multistate bank with following columns:

1. `customer_id`: Account Number
2. `credit_score`: Credit Score
3. `country`: Country of Residence
4. `gender`: Sex
5. `age`: Age
6. `tenure`: From how many years he/she is having bank acc in ABC Bank
7. `balance`: Account Balance
8. `products_number`: Number of Product from bank
9. `credit_card`: Is this customer have credit card ?
10. `active_member`: Is he/she is active Member of bank ?

## Business Objectives

1. **Churn Prediction**:
   
   - **Columns Used**: `customer_id`, `credit_score`, `age`, `tenure`, `balance`, `products_number`, `credit_card`, `active_member`
   - **Approach**: Utilize machine learning algorithms like logistic regression, decision trees, or neural networks to predict which customers are likely to churn based on their credit score, age, tenure, balance, number of products, credit card status, and active membership.

2. **Customer Segmentation**:
   
   - **Columns Used**: `credit_score`, `age`, `tenure`, `balance`, `products_number`, `credit_card`, `active_member`
   - **Approach**: Use clustering algorithms (e.g., K-means clustering) to group customers based on their characteristics such as age, tenure, balance, number of products, credit card status, and active membership. This can help in understanding different customer segments and tailoring retention strategies accordingly.

3. **Feature Importance Analysis**:
   
   - **Columns Used**: All columns except `customer_id` and `country`
   - **Approach**: Employ techniques like feature importance from decision trees or permutation importance to identify which features have the most impact on customer churn. This analysis can guide the bank to focus on specific aspects when designing retention programs.

4. **Customer Lifetime Value (CLV) Prediction**:
   
   - **Columns Used**: `age`, `tenure`, `balance`, `products_number`, `credit_card`, `active_member`
   - **Approach**: Use regression techniques to predict the lifetime value of customers based on their age, tenure, balance, number of products, credit card status, and active membership. This information can assist the bank in prioritizing efforts and resources towards high-value customers.

5. **Identifying Key Drivers of Churn**:
   
   - **Columns Used**: All columns except `customer_id` and `country`
   - **Approach**: Conduct statistical analysis (e.g., correlation analysis) and data visualization to understand the relationships between different variables and churn. Identify patterns and correlations to pinpoint the key factors contributing to customer churn.

6. **Retention Strategy Optimization**:
   
   - **Columns Used**: All columns except `customer_id` and `country`
   - **Approach**: Utilize A/B testing and experimental design methodologies to test different retention strategies. Analyze the data to determine which strategies are most effective in retaining customers. This could involve testing different incentives, communication channels, or engagement approaches.

## Reference

1. [BankChurn EDA and Prediction Using Lazy Classifier | Kaggle](https://www.kaggle.com/code/prathameshgadekar/bankchurn-eda-and-prediction-using-lazy-classifier)

2. [Churn - EDA, Balancing and Machine Learning | Kaggle](https://www.kaggle.com/code/raphaelmarconato/churn-eda-balancing-and-machine-learning)

3. [Medium blog on customer retention analysis using PowerBI](https://medium.com/@Feranmi_Amole/customer-retention-analysis-with-power-bi-d9dd00077a36)

4. [Customer retention using SQL](https://medium.com/cube-dev/customer-retention-analysis-93af9daee46b)

5. [Customer retention Kaggle](https://www.kaggle.com/datasets/uttamp/store-data)
