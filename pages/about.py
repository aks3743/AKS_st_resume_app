"""About page shown when the user enters the application"""
import streamlit as st
import base64
LOGO_IMAGE = "pages\\aks1.jpg"
def write():
    """Used to write the about page in the app.py file"""
    st.title("Un Esprit Curieux - A curious mind!")
    st.markdown(
    f"""
    <div class="container">
        <img class="logo-img" src="data:image/png;base64,{base64.b64encode(open(LOGO_IMAGE, "rb").read()).decode()}" width="100" height="100">
        <p class="logo-text">Welcome to my page !!!</p>
    </div>
    """,
    unsafe_allow_html=True
)
    st.markdown(
            """## Who Am I?
"_I am a Random Forest in the World of Overfitting_"

A Data Scientist with 5 years of experience in solving Business Problems, 
a constant learner and a firm believer of experimentation over expertise. 
Always on the lookout for new technologies, I am passionate about designing Data driven solutions which are easy, economical and can be scaled.
 


*Abhijith K S* \n
**Data Science | Business Analytics | Project Management**

[**LinkedIn**](https://www.linkedin.com/in/abhijith-k-s-aks3743/) | [**Email**](mailto:aksstudy94@gmail.com)

## The Project
I came across **Streamlit** last week while looking for solution to host python apps on AWS EC2. 
The Framework  boasts of being the easiest and the fastest way of creating interactive apps, and after spending just a 
few hours creating this interactive resume, I can vouch for that. 

Check out my [**GitHub**]() for the implementation. Reach out to me for any project or a simple discussion on Streamlit.
Also check out their [**page**](https://www.streamlit.io/) for more more information and updates.
Also check out this amazing implementation of Streamlit by [**Marc Skov Madsen**](http://awesome-streamlit.org/) for streamlit inspiration.


""",
            unsafe_allow_html=True,
        )
if __name__ == "__main__":
    main()
