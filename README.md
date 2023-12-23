# Reducing Customer Churn of ABC Bank

Telco company stakeholder have reached out to me for the solution of their recent surge in customer churn. This alarming trend is significantly impacting their long-standing relationship with their clients.

To solve this problem, they need a data scientist who can help them understand the underlying cause of this sudden increase in customer defection.

In this project, I will perform data analysis using Python and libraries to solve this problem. Objective of this project is to learn more about data analysis practically and also to understand the flow of a real-life project in a company.

Steps:

1. [Business Problem](#business-problem)
2. [Business Understanding](#business-understanding)
3. [Data Understanding](#data-understanding)
4. [Data Preparation](#data-preparation)
5. [Modeling](#modeling)
6. [Evaluation](#evaluation)
7. [Deployment](#deployment)
8. [Reference](#reference)

## Business Problem

Telco company want me to find out the cause of the customer defection. Mainly they want me to see the relation between this customer churn with other factors like customer dissatisfaction, competitive pressure and customer preferences.

The problem in hand incorporates 5 things to do:

1. **Customer Behavior Patterns:** Analyze recent customer interactions, transactions, and service usage to identify any discernible patterns or anomalies that might be indicative of disengagement or dissatisfaction.

2. **Service Satisfaction Metrics:** Evaluate the effectiveness of our current customer service strategies and identify areas for improvement. Are there specific services or touchpoints that consistently result in customer dissatisfaction?

3. **Competitive Benchmarking:** Conduct a comparative analysis with other leading companies in the same market to identify any superior practices or features that may be attracting our customers away.

4. **Predictive Modeling:** Develop predictive models to forecast potential churn candidates based on historical data. This will enable us to proactively address concerns and tailor retention strategies.

5. **Customer Feedback Analysis:** Scrutinize customer feedback channels, such as surveys and complaints, to pinpoint recurring issues and sentiments that may be contributing to the churn.

The ultimate goal is not just to understand the cause of the customer churn but also to implement effective measures that will help retain the valued clients.

## Business Understanding

- **Customer Profiling**: Analyzing customer behaviour patterns such as their interactions, transactions and service usage to understand each group of customers and find out the properties of those groups. From this, we can also find out which group has properties of dissatisfaction or disengagement which essentially means to find the groups that has more chances of churn.

- **Regression Analysis of Customer Satisfaction**: Using regression to predict or estimate the churn rate of customers towards customer service strategies. Analyzing the difference between satisfied and dissatisfied customers using the regression prediction. Then, looking at the features that differentiate the 2 groups and thinking of strategies to improve on those features.

- **Comparative Analysis with Leading Companies**: FUTURE WORK...

- **Class Probablity Estimation**: Predicting the probablities of the customer churning from ABC bank using classification technique. It helps forecasting potential churn candidates based on historical data. It will help us in understanding the customers who are going to churn, ans then focus next services on only those who have better chances of turning back. It will also help in understanding the candidates who have highest churn rate and their problems.

- **Analysis of Churn Reasons**: Using NLP to examine the sentiment of the churn reasons and researching the words that are used when the sentiment is negative can help in finding out what customers are dissatisfied about and also whatever we find positive from the positive sentiment, whether we can include that to improve customer experiences.

## Data Understanding

- For **Customer Profiling**, I will use unsupervised learning algorithms to understand the groups of clusters that have similarities to each other. The dataset contains features like [NAME OF ALL FEATURES THAT I AM USING] to apply clustering.

- For **Regression analysis**, I am using supervised learning which means I am using the labels of satisfaction measure that have values from 1-5. In this case, classification can also be an answer but for now I will go with regression.

- For **Comparative Analysis**, FUTURE WORK...

- For **Class Probablity Estimation**, I am using the churn column of dataset to apply supervised algorithm to classify between churn or not churn.

- For **Sentiment Analysis**, I am using the churn reason from customers to apply NLP to find out the words or most common reasons for the customers to churn.

## Data Preparation

Dataset: `/data/teleco-customer-churn/telco_customer_churn.xlsx`.



## Modeling

## Evaluation

## Deployment

## Reference

1. [BankChurn EDA and Prediction Using Lazy Classifier | Kaggle](https://www.kaggle.com/code/prathameshgadekar/bankchurn-eda-and-prediction-using-lazy-classifier)

2. [Churn - EDA, Balancing and Machine Learning | Kaggle](https://www.kaggle.com/code/raphaelmarconato/churn-eda-balancing-and-machine-learning)

3. [Customer retention Kaggle](https://www.kaggle.com/datasets/uttamp/store-data)
