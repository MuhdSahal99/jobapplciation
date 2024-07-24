import streamlit as st
from pages import candidate_page, employer_page

def main():
    st.sidebar.title("ATS")
    page = st.sidebar.radio("Select Page", ["Candidate", "Employer"])

    if page == "Candidate":
        candidate_page.show()
    elif page == "Employer":
        employer_page.show()

if __name__ == "__main__":
    main()