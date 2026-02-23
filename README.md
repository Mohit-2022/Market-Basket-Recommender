**1. Frequently Bought Together Recommendation System**

This project builds an end-to-end Market Basket Analysis based recommendation engine using the Instacart dataset to identify product combinations that are frequently purchased together. 
The system leverages Association Rule Mining techniques to generate real-time product recommendations for cross-selling opportunities in retail environments.

**2.  Problem Statement**

Retailers often aim to increase revenue by recommending complementary products to customers during purchase. However, identifying meaningful product relationships from millions 
of transactions manually is not feasible.

The objective of this project is to:

  a) Identify frequently co-purchased product combinations
  
  b) Generate actionable association rules between products
  
  c) Recommend complementary products in real-time
  
  d) Deploy a user-friendly recommendation system using Streamlit

**3.  Approach**

The recommendation engine is built using Association Rule Mining, specifically:

  a) Apriori Algorithm
  
  b) Support

  c) Confidence
  
  d) Lift

These metrics help quantify relationships between products based on historical transaction data.

**4. Dataset**

The Instacart Online Grocery Shopping Dataset was used, containing over:

  a) 3 million orders
  
  b) 200,000+ users
  
  c) 49,000+ products

Each order represents a customer’s basket containing multiple purchased items.

**5. Methodology**

  a) Data Preprocessing

    Merged product and order datasets
    
    Filtered top frequently purchased products to reduce dimensionality
    
    Sampled transaction data for memory optimization

    Converted transactions into a one-hot encoded basket matrix

  b) Frequent Itemset Mining

    The Apriori algorithm was applied to identify frequently purchased product combinations using:
    
**   Minimum Support Threshold = 0.01**
    
    This step reduced the total product combinations to only meaningful frequent itemsets.

  c) Association Rule Generation

    Association rules were generated using:
    
    Confidence ≥ 0.2
    
    Lift ≥ 1.2

    Lift was used to identify statistically significant relationships between products beyond random chance.
    
    Example Rule:
    
    Organic Raspberries → Organic Strawberries
    Lift = 2.79

    Indicates that customers purchasing Organic Raspberries are 179% more likely to purchase Organic Strawberries compared to random shoppers.

  d) Recommendation Engine

    A recommendation function was built to:
    
    Accept product input
    
    Identify matching association rules
    
    Rank recommendations based on Lift
    
    Return Top 5 complementary products , but unfortunately only 1 complementary products is refelcting considering association rule

  e) Model Deployment

    The generated association rules were serialized using Pickle and deployed using Streamlit Cloud to enable real-time recommendations via an 
    interactive web application.

    🔗 [Click Here to Use Live App](https://instacartfbtrecommender-dn4rqpmjb65xa99rhd2522.streamlit.app/)

**6. Project Structure**

    association_rules.pkl   → Saved association rules  
    app.py                  → Streamlit application  
    requirements.txt        → Dependencies  
    README.md               → Project documentation
 
**7. Tech Stack**

    Python
    
    Pandas
    
    MLxtend
    
    Streamlit
    
    Pickle
 
 **8. Business Impact**
 
    This system can help retailers:
    
      a) Increase Average Order Value (AOV)
      
      b) Improve product bundling strategies
      
      c) Enhance cross-selling opportunities
      
      d) Optimize promotional campaigns












