import streamlit as st
import pickle

rules = pickle.load(open('association_rules.pkl','rb'))

def recommend_products(product_name):

    recommendations = []

    for i in range(len(rules)):
        
        antecedent = list(rules.iloc[i]['antecedents'])
        consequent = list(rules.iloc[i]['consequents'])

        if product_name in antecedent:
            recommendations.extend(consequent)

    return list(set(recommendations))[:5]


st.title("🛒 Frequently Bought Together System")

product_input = st.text_input("Enter Product Name")

if st.button("Recommend"):

    result = recommend_products(product_input)

    if len(result) == 0:
        st.write("No recommendations found")
    else:
        st.write("Recommended Products:")
        for item in result:
            st.write(item)