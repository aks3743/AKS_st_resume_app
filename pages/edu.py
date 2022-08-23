"""Edu page shown when the user enters the application"""
import streamlit as st

def write():
    """Used to write the page in the app.py file"""
    st.title("Education :books:")
    st.markdown(
            """### Birla Institute of Technology
**Master of technology in Data Science and Engineering | Sept 2022** | [**BITS Pilani**](https://www.bits-pilani.ac.in/)\n
GPA 8.2/10.00  

**Courses ** \n
- Statistics in Business Analytics \n
- Big Data Analytics with Hadoop \n
- Business Decision Modelling \n
- Predictive Analytics \n
- Data Mining and Business Analytics \n
- Introduction to Project Management \n
- Advanced Business Analytics and Project Management \n
- Adaptive Business Intelligence \n
- Project Risk and Cost Management \n
- Project Leadership and Communication \n


### Distance Learning

**One Fourth Labs | Dec 2019** | [Credential](https://www.credential.net/15fc1cb5-62e7-4658-9f50-b9eddabb2330#gs.9hj7zi)\n
- PadhAI - Deep Learning course completion

**Coursera | April 2019** | [Credential](https://www.coursera.org/account/accomplishments/verify/ZHXMJW4DF2QP)\n
- Neural Networks and Deep Learning

**EY Analytics| Oct 2018** | [Credential](https://www.credly.com/badges/7bf283d6-fab5-418f-98d6-efef12ea6abc/linked_in_profile)\n
- EY Analytics - Data visualization - Bronze (2018)

**EY Analytics| Sept 2018** | [Credential](https://www.credly.com/badges/e8274280-71c5-487e-8210-85c182f22431/linked_in_profile)\n
- EY Analytics - Data integration - Bronze (2018)

### College of Engineering Trivandrum
**Bachelors of Technology in Mechanical Engineering | May 2017** | [**CET**](https://www.cet.ac.in/)\n
GPA 8.2/10.00 

**Courses **\n
- Essentials of management\n
- Engineering Economics and Management \n
- Object Oriented Programming \n
- Business Communications \n
- Operational Research

""",
            unsafe_allow_html=True,
        )
if __name__ == "__main__":
    main()
