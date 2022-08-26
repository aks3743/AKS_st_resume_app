"""Skills page shown when the user enters the application"""
import streamlit as st

def write():
    """Used to write the page in the app.py file"""
    st.title("Skills :hammer_and_wrench:")
    st.markdown(
            """## Languages
- R
- Python
- SQL 

## Platforms and Libraries
- **MS Office** - Excel, Powerpoint, Project, Word
- **Python** - Pandas, Numpy, Skicit Learn,Scipy, NLTK, Tensorflow,Pytorch,Transformers, Keras, Streamlit, Dash, Plotly, Matplotlib, Seaborn, etc.
- **R** - Shiny, Dplyr
- **SQL** - MS SQL, PostgreSQL,HIVE
- Tableau
- PowerBI


## Analytical Skills
- Statistical Data Analysis
- Data Wrangling
- Hypothesis Testing
- Machine Learning
- Natural Language Processing
- Deeplearning
           

_I am a Bag of words who want to become Transformers_



""",
            unsafe_allow_html=True,
        )
if __name__ == "__main__":
    main()
