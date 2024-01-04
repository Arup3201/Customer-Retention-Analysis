# Reducing Customer Churn of Telco

Telco company stakeholder have reached out to me for the solution of their recent surge in customer churn. This alarming trend is significantly impacting their long-standing relationship with their clients.

To solve this problem, they need a data scientist who can help them understand the underlying cause of this sudden increase in customer defection.

In this project, I will perform data analysis using Python and libraries to solve this problem. Objective of this project is to learn more about data analysis practically and also to understand the flow of a real-life project in a company.

## Problems and Goal

Telco communication is finding difficulty to keep customers for a long time and recently they are facing the rapidly growing problem of customer churn. They want a model that can help them understand which customers are likely to churn and which customers are loyal. Also this will help them focus more on the loyal customers and improve on the possible churn customers. Throughout this process, they also want to learn which factors are more detrimental for customer churn and effectively they want to work on those factors. Not only that, they also want an analysis of the whole customer churn and want to know insights that can improve their customer retention.

So, the goal of this project is to deliver the analysis related to customer churn and some suggestions to improve, model that can predict customer churn, importance of features that highly contribute to the customer churn.

## Establishing data sources

Data source: `./data/telco-customer-churn/telco_customer_churn.xlsx`

Dataset Link: [Telco customer churn: IBM dataset | Kaggle](https://www.kaggle.com/datasets/yeanzc/telco-customer-churn-ibm-dataset)

## Data Preparation, Expoloration, and Preprocessing
**About the dataset:**

- Dataset contains 7043 entries and 33 features.

- Features of the dataset are-
    - `Customer ID`: ID of customers each are unique
    - `Count`: Frequency of the customer in the table
    - `Country`: Country of the customer
    - `State`: State where customer lives
    - `City`: City where customer resides(1129 unique city names)
    - `Zip Code`: Zip code of the place
    - `Lat Long`: Latitude and Longitude of the place
    - `Latitude`: Latitude of the place
    - `Longitude`: Longitude of the place
    - `Gender`: Gender of the customer (Male or Female)
    - `SeniorCitizen`: Indicates whether the client is an older person (0, 1).
    - `Partner`: Indicates whether or not the client is partnered (Yes, No).
    - `Dependents`: Indicates whether the client is supported by others (Yes, No).
    - `Tenure Months`: The length of time a customer has been a customer of the business (multiple different number values)).
    - `Phone Service`: If the client has a phone service, it is indicated by the words “Yes” or “No”.
    - `Multiple Line`: Whether the customer has more than one line (no phone service, no service, yes service).
    - `Internet Service`: Whether the client has a subscription to the company’s Internet service (DSL, Fiber optic, or No).
    - `Online Security`: Indicates if the client has access to online security (Internet service available, No, Yes).
    - `Online Backup`: Indicates whether or not the client has an online backup (Internet service unavailable, No, Yes).
    - `Device Protection`: Indicates whether the client has device protection (Internet service not available, Not Available, Yes).
    - `Tech Support`: Whether the customer has access to tech help (no internet service, no, yes).
    - `Streaming TV`: Whether the customer has access (no internet service, no, yes).
    - `Streaming Movies`: Streaming movies: Indicates whether or not the client offers or has access streaming movies(no internet service, no, yes).
    - `Contract`: The type of existing contract for the customer (Month-to-Month, One-Year, Two-Year)
    - `Paperless Billing`: Whether the client uses paperless billing (Yes, No)
    - `PaymentMethod`: The chosen payment method by the consumer (credit card, bank transfer, electronic check, paper check)
    - `Monthly Charges`: The monthly charge made to the consumer (various numeric quantities)
    - `Total Charges`: (many different numeric values): The total amount charged to the consumer
    - `Churn Label`: Whether the customer decided to leave the service or not ('yes' or 'no').
    - `Churn Value`: 0 or 1 depending on the churn value as 'no' or 'yes'.
    - `CLTV`: Customer Lifetime Value if they stayed in the company as a customer.
    - `Churn Reason`: Churn Reason: Reason for the customer to choose to leave.


## Modeling and testing



## Deployment and Monitoring



## Reference

1. [BankChurn EDA and Prediction Using Lazy Classifier | Kaggle](https://www.kaggle.com/code/prathameshgadekar/bankchurn-eda-and-prediction-using-lazy-classifier)

2. [How to implement customer churn | neptune.ai](https://neptune.ai/blog/how-to-implement-customer-churn-prediction)