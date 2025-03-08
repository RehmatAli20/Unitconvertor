import streamlit as st
import pandas as pd
import os
from io import BytesIO

# Set up app
st.set_page_config(page_title="File Data Manager", layout="wide")

# Centered title
col1, col2, col3 = st.columns([2, 2, 1])
with col2:
    st.title("FileFlex")  
st.subheader("Upload, Edit, and Download Your Files Easily")  

# File uploader with multiple file support
c1, c2 = st.columns([1, 1])
with c1:
    upload_files = st.file_uploader(
        "Upload CSV or Excel:", 
        type=["csv", "xlsx"], 
        accept_multiple_files=True  
    )

if upload_files:
    for file in upload_files:  
        file_ext = os.path.splitext(file.name)[-1].lower()

        # Read file based on type
        if file_ext == ".csv":
            df = pd.read_csv(file)
        elif file_ext == ".xlsx":
            df = pd.read_excel(file)
        else:
            st.error(f"Unsupported file type: {file_ext}")
            continue

        # Display file info
        st.write(f"**File Name:** {file.name}")
        st.write(f"**File Size:** {file.getbuffer().nbytes / 1024:.2f} KB")  

        # Show preview of data
        st.write("YOU CAN CHANGE VALUES IN DATAFRAME ")
        edited_df = st.data_editor(df, key=f"editor_{file.name}")  # Allow editing

        # Data cleaning options
        st.subheader(f"Data Cleaning Options for {file.name}")

        if st.checkbox(f"Clean Data for {file.name}"):
            col1, col2 = st.columns(2)

            with col1:
                if st.button(f"Remove Duplicates from {file.name}"):
                    edited_df.drop_duplicates(inplace=True)
                    st.success("Duplicates Removed!")

            with col2:
                if st.button(f"Fill Missing Values for {file.name}"):
                    numeric_cols = edited_df.select_dtypes(include=['number']).columns.to_list()
                    edited_df[numeric_cols] = edited_df[numeric_cols].fillna(edited_df[numeric_cols].mean())
                    st.success("Missing values have been filled!")

        # Choose specific columns to keep
        st.subheader("Select columns to keep")
        columns = st.multiselect(f"Choose Columns for {file.name}", list(edited_df.columns), default=list(edited_df.columns))
        edited_df = edited_df[columns]

        # Visualizations
        st.subheader("Data Visualization")
        if st.checkbox(f"Show Visual Representation of {file.name}"):
            st.bar_chart(edited_df.select_dtypes(include=['number']).iloc[:, :2])

        # Convert and Download the edited file
        st.subheader("Convert & Download File")
        conversion_type = st.radio(f"Convert {file.name} to:", ["CSV", "Excel"], key=file.name)

        if st.button(f"Save & Download {file.name}"):
            buffer = BytesIO()
            if conversion_type == "CSV":
                edited_df.to_csv(buffer, index=False)
                file_name = file.name.replace(file_ext, ".csv")
                mime_type = "text/csv"
            elif conversion_type == "Excel":
                edited_df.to_excel(buffer, index=False)
                file_name = file.name.replace(file_ext, ".xlsx")
                mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

            buffer.seek(0)

            # Download button
            st.download_button(
                label=f"Download {file.name} as {conversion_type}",
                data=buffer,
                file_name=file_name,
                mime=mime_type,   
                
            )
            st.success("Awesome! 🎉 Your file is good to go.")  
            st.success("We appreciate you choosing our service. Have a great day! 😊") 