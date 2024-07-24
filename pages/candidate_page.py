import streamlit as st
from job_matcher import JobMatcher
import os

def show():
    st.title("Candidate Job Matcher")
    
    # File uploader for resume
    uploaded_file = st.file_uploader("Upload your resume (PDF or DOCX)", type=["pdf", "docx"])
    
    if uploaded_file is not None:
        try:
            # Check if the CSV file exists
            csv_path = "data/job_listings.csv"
            if not os.path.exists(csv_path):
                st.error(f"Error: The file {csv_path} does not exist.")
                return

            # Initialize JobMatcher
            job_matcher = JobMatcher(csv_path)
            
            # Process the resume and get recommendations
            recommendations = job_matcher.process_resume(uploaded_file)
            
            # Display recommendations
            st.subheader("Top Job Recommendations:")
            for i, (job_title, similarity, description) in enumerate(recommendations, 1):
                st.write(f"{i}. {job_title}")
                st.write(f"   **Similarity: {similarity * 100:.2f}%**")
                st.write(f"   Description: {description}")
                st.write("---")
        
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
