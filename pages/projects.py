"""Projects page shown when the user enters the application"""
import streamlit as st

def write():
    """Used to write the page in the app.py file"""
    st.title("Projects - :male-construction-worker: ")
    st.markdown(
            """<div style="text-align: justify;>
### Decision Scientist, :blue[Mu Sigma Inc.]| June 2019 - July 2022

**:red[Launch Support & Analytics]** | **:blue[SQL, python, Tableau]**

 Managed a team of fifteen analysts who assisted the Strategy team in determining the pertinent indicators that needed to be monitored during the introduction of a new drug into various markets
 Compiled all ﬁeld strategy, ﬁnancial strategy, promotional strategy, and customer strategy data into a single dashboard(Tableau) and enabled the leadership team in staying on top of all launch operations on each front. The analysis for the BE data was processed in python which needed knowledge of databases, pandas, numpy etc. The ADS created was pushed into AWS S3 buckets through boto3 library.
 The team also created a dashboard(Tableau) that is presentation ready, which helped them in tracking the pre prep for future launches (Launch readiness). This dashboard helped the launch strategy team in tracking each steps of launch process which previously was done using excel tracker, leading to many errors and time wastage

**:red[Network Analytics]** | **:blue[SQL, python, Tableau, Excel]**

 Led a three-member team who helped the launch team in ﬁnding the most eﬀective healthcare providers to contact in order to enroll patients in a new study
 Techniques like hcp profiling, distance calculations were involved in this activity
 This assisted the customer in reducing efforts in terms of both money and time, and it helped them choose the best course of action

**:red[Next Purchase Date Prediction]** | **:blue[SQL, python, Tableau, Excel]**

Retail Sales UK-based Fortune 500 Retail Company.Led a seven-member team for the Strategic Insights and Analytics group to leverage statis-
tical analyses and regression modelling using python to predict a consumer's Next Purchase
Date, Churn Probability and other characteristics. The insights helped in formulating suitable
marketing strategies for enhanced engagement leading to reduction in churn rate by 12'%' and
monetary impact of 0.6M in 2 months

**:red[Customer Insights Portal Analytics]** | **:blue[SQL, python, Tableau, Excel]**

 Developed a sentiment analyzer for medical insights obtained, comparing the performance of libraries BERT, BIOBERT, and SciBERT. This aided the Customer Engagement Team in finding and categorizing pertinent material that required rapid attention, which previously required a great deal of human engagement.For this CRM project, I worked on sentiment analysis to categorize HCP insights as good, negative, or neutral. To construct this, I utilized BERT for embedding and added a classification layer to the end of the pretrained model. However, there were challenges such as class imbalance, data shortages, and so on throughout implementation. But using this, we were able to attain over 60\% accuracy and accurately identify the majority of the insightful findings.
 Used text mining and text clustering techniques to group the insights collected to particular categories using TF-IDF technique
 Created curated reports using text mining and NLP techniques to support major US Medical congresses such as ASCO, ASH etc. These were numbers pulled out after processing text data to finding most trending terms, topics etc. This helped the leadership team in following the flow of a concept or topic over time to find out which is the most relevant topic of discussion. We used python to do the data processing and displayed the information in the form of Tableau dashboards.
 Created notebooks for automated reports on impact of COVID-19 in different therapeutics areas, which involved trending topics identification, information retrieval from raw text etc.

**:red[Patient enrollment prediction - NRDG Studies]** | **:blue[R, python, SQL, Tableau, Excel]** \n

 Performed patient enrolment prediction for NRDG Studies
 Used multiple regression techniques such as linear regression, polynomial regression etc to derive the best prediction values
 Helped the client in making decisions on studies that will be delayed in the future and derive business strategies based on the predictions. The above information helped the leadership team in identifying studies that were having a risk of getting delayed and also properly understanding why are they getting delayed


### Associate Analyst, :blue[EY LLP] | May 2018 - May 2019
**Audit and Accounting** \n **:blue[R, python, SQL, Tableau, Excel]** \n
 Started career as Data Analyst. Had the opportunity to look into and perform ETL on different variety of data
 Worked on image processing and recognition activities from scanned pdf documents
 Worked on Audit data of fortune-500 companies

### Academic Projects [(GitHub)](https://github.com/aks3743/)

### Mtech thesis Birla Institute of Technology Pilani\n
May 2022 - Aug 2022 **(python, Tableau, Excel)**

 We sought to make a product that could convert photographs to sounds while working on the image to audio generator. Here, I decoded the image using a CNN model (VGG16, Resnet50, etc.), tokenized and embedded the captions using glove embedding, and then integrated the two models to convert the image to text and the text to audio using the Google API.
 There were many NLP related assignments that I have worked on during my Masters in data science and engineering like image caption generator , restaurant recommender, stack overflow question quality classification etc.


            
</div>
""",
            unsafe_allow_html=True,
        )
if __name__ == "__main__":
    main()
