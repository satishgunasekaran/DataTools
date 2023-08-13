import streamlit as st
import pandas as pd
from io import BytesIO

st.set_page_config(page_title="Data Merger", page_icon="📈")

# Upload two files
file1 = st.file_uploader("Upload file 1", type=["csv", "xlsx"])
file2 = st.file_uploader("Upload file 2", type=["csv", "xlsx"])

# Select join type
join_type = st.selectbox("Select join type", ["left", "right", "inner", "outer"])

# Enter common column name
common_column = st.text_input("Enter common column name")

# Merge and display result
if st.button("Merge"):
    if file1 is not None and file2 is not None:
        df1 = pd.read_csv(file1) if file1.name.endswith('.csv') else pd.read_excel(file1)
        df2 = pd.read_csv(file2) if file2.name.endswith('.csv') else pd.read_excel(file2)
        
        df = pd.merge(df1, df2, how=join_type, on=common_column)
        st.dataframe(df)

        # Download button
        output = BytesIO()
        df.to_csv(output, index=False)
        output.seek(0)
        st.download_button("Download Merged Data", data=output, file_name='merged_data.csv', mime='text/csv')

    else:
        st.write("Please upload two files to merge.")
