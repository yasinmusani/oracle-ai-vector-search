# app_ui.py

import streamlit as st
import requests

st.set_page_config(page_title="Product Search", page_icon="🔍")

st.title("🔍 Vector-Based Product Search")

# Input field
query = st.text_input("Enter a product search term", placeholder="e.g., Watch, Headphones, Laptop")

# Submit button
if st.button("Search"):
    if not query:
        st.warning("⚠️ Please enter a search term.")
    else:
        try:
            # Call your Flask API endpoint
            api_url = "http://localhost:5000/search"  # Change if running elsewhere
            response = requests.post(api_url, json={"query": query})
            
            if response.status_code == 200:
                data = response.json()
                results = data.get("results", [])

                if results:
                    st.success(f"✅ Found {len(results)} results:")
                    for idx, (name, desc, distance) in enumerate(results, 1):
                        st.markdown(f"### {idx}. {name}")
                        st.write(desc)
                        st.code(f"Similarity Score: {distance:.4f}")
                        st.markdown("---")
                else:
                    st.info("🔎 No results found.")
            else:
                st.error(f"❌ API Error: {response.status_code}")
        except Exception as e:
            st.error(f"❗ Error connecting to the API: {e}")

