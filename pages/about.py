"""About page shown when the user enters the application"""
from ast import Pass
import streamlit as st
import base64
LOGO_IMAGE = "pages\\aks1.jpg"
def write():
    """Used to write the about page in the app.py file"""
    st.title("Hope for the best and Prepare for the worst...")
    try :
        st.markdown(
    f"""
    <div class="container">
        <img class="logo-img" src="data:image/png;base64,{base64.b64encode(open(LOGO_IMAGE, "rb").read()).decode()}" width="100" height="100">
        <p class="logo-text">Welcome to my page !!!</p>
    </div>
    """,
    unsafe_allow_html=True
)
    except OSError as OS:
        pass
    # st.image(LOGO_IMAGE,width=100)
    st.markdown(
            """## Who Am I?
"_I am a Bag of words who want to become Transformers_"

Skilled data scientist manager with 4+ years of experience in the Data Science 
domain who creates valuable insights from data and transforms them to action. 
Have hands-on experience in Data Analysis with expertise in Python, SQL, Tableu and 
Cloud technologies. Experience in developing Machine learning/Deep learning models 
and deploying them in production environments. Experience in managing, leading and 
developing data science solutions from scratch using AI/ML techniques. Experience 
in problem solving, ETL, EDA and data visualization. Experience in using state of 
the art NLP techniques in information retrieval and feature extraction from 
images/computer vision using DL techniques. Ability to write clean code,strong 
understanding of object oriented programming and excellent presentation skills.


### Abhijith KS \n
**Data Science | Business Analytics | Project Management**

[**LinkedIn**](https://linkedin.com/comm/mynetwork/discovery-see-all?usecase=PEOPLE_FOLLOWS&followMember=abhijith-k-s-aks3743) | [**Email**](mailto:aksstudy94@gmail.com)



""",
            unsafe_allow_html=True,
        )
    
    
    # try :
    #     file_path='pages/Abhijith_KS_CV_18_08_compressed.pdf'
    #     with open(file_path,"rb") as f:
    #         base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    #     pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="800" height="800" type="application/pdf"></iframe>'
    #     st.markdown(
    #         '''
    #         ### My resume
    #     ''')
    #     st.markdown(pdf_display, unsafe_allow_html=True)
    # except OSError as e:
    #     Pass
    st.markdown(
        '''
        #### The Project
I came across **Streamlit** while looking for solution to host python apps on web. 
The Framework  boasts of being the easiest and the fastest way of creating interactive apps, and after spending just a 
few hours creating this interactive resume, I can vouch for that. 

Check out my [**GitHub**](https://github.com/aks3743/) for the implementation. Reach out to me for any project or a simple discussion on Streamlit.
Also check out their [**page**](https://www.streamlit.io/) for more more information and updates.
Also check out this amazing implementation of Streamlit by [**Marc Skov Madsen**](http://awesome-streamlit.org/) for streamlit inspiration.

        '''
    )
if __name__ == "__main__":
    main()
