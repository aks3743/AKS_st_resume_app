### Main page for streamlit resume
import streamlit as st
import pages.about
import pages.skills
import pages.projects
import pages.edu
# import pages.recommendations

import resources.ast as ast

PAGES = {
    "About": pages.about,
    "Education" : pages.edu,
    "Skills": pages.skills,
    "Projects": pages.projects,
    # "Recommendations": pages.recommendations
}

def main():
    """Main function of App"""
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))

    page = PAGES[selection]
    # st.snow()
    with st.spinner(f"Loading {selection} ..."):
        ast.write_page(page)

    st.sidebar.title("Hire Me")
#     st.sidebar.info(
#         """
#         If you are looking to hire a Data Scientist, 
#         [email me](mailto:aksstudy94@gmail.com) or reach out 
#         to me on [Linkedin](https://www.linkedin.com/in/abhijith-k-s-aks3743/)
# """)
    # st.sidebar.title("Additional Info")
    st.sidebar.info(
        "This an interactive streamlit app completely created with Python's latest library **streamlit** "
        "Do reach out to me on [LinkedIn](https://www.linkedin.com/in/abhijith-k-s-aks3743/) or "
        "at [Mail me](mailto:aksstudy94@gmail.com) to know more. "
        "Also check the [source code](https://github.com/aks3743/AKS_st_resume_app) here. "  

)

if __name__ == "__main__":
    main()
