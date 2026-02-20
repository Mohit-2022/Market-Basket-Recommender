import streamlit as st
import pickle
import pandas as pd

# ------------------ Load Saved Rules ------------------
rules = pickle.load(open('association_rules.pkl','rb'))

# ------------------ Get All Available Products ------------------
all_products = set()

for i in range(len(rules)):
    for item in list(rules.iloc[i]['antecedents']):
        all_products.add(item)

product_list = sorted(list(all_products))

# ------------------ Recommendation Function ------------------
def recommend_products(product_name):

    filtered_rules = rules[
        rules['antecedents'].apply(lambda x: product_name in x)
    ]

    filtered_rules = filtered_rules.sort_values(
        by='lift', ascending=False
    )

    recommendations = []

    for i in range(len(filtered_rules)):
        consequent = list(filtered_rules.iloc[i]['consequents'])
        recommendations.extend(consequent)

    return list(set(recommendations))[:5]


# ------------------ Streamlit UI ------------------
st.title("🛒 Frequently Bought Together System")

product_input = st.selectbox(
    "Select Product",
    product_list
)

if st.button("Recommend"):

    result = recommend_products(product_input)

    if len(result) == 0:
        st.write("No recommendations found")
    else:
        st.write("Recommended Products:")
        for item in result:
            st.write(item)
