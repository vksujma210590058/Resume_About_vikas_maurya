import time
import streamlit as st
st.title(":rainbow[♥Hi this side is Vikas Maurya♥]")
st.write(":red[Quotes♥♥♥ :]:rainbow[Be someone's sunshine when their skies are grey.]")
st.write(":red[This is for you♥♥♥: ]:rainbow[I heard you are focusing more on yourself,and worring a little less about everyone else.That's beautiful.]")

# st.title("Hi This Side is Vikas Maurya")
col1,col2,col3=st.columns([1,2,1])
# col1.markdown("hi here is Vikas Maurya")
# camera_photo=col2.file_uploader(label="upload")
# uploaded_photo=col2.camera_input("Take a photo")
# progress_bar=col2.progress(0)
# for perc_completed in range(100):
#     time.sleep(.05)
#     progress_bar.progress(perc_completed+1)
# col2.success("photo uploaded sucessfully")
# col3.metric(label="Temperature",value='12 °c',delta="+ 3°c")
# with st.expander("Click to read more"):
#     st.write("hello")
#     if uploaded_photo is None:
#         st.image(camera_photo)
#     else:
#         st.image(uploaded_photo)

col1.markdown(":rainbow[Data Analytics course from EBSC Technologies Pvt. Ltd (Edubridge)]")
col1.markdown(":rainbow[Bachlar in Social science and Political science with 65%]")
col1.markdown(":rainbow[12th topper in college with 81.2%]")
col1.markdown(":rainbow[10th topper with 88.67%]")
col1.markdown(":rainbow[5 * Star Sql learner on HackerRank]")
# uploaded_file = col2.file_uploader("IMG20231210160321.jpg", type=["jpg"])
col2.image('vikas_maurya.png', caption="Vikas Maurya",width=400)
# URL to be displayed
url1 = "https://www.linkedin.com/in/vikas-maurya-a0886728b"

# Display the URL using st.markdown
col3.markdown(f":red[Linkin Profile :] [{url1}]({url1})")
url2="https://github.com/vksujma210590058?tab=repositories"
col3.markdown(f":red[GitHub link:] {url2}")
# st.markdown(f"**Gmail:** {gmail_address}")
# st.markdown(f"**Mobile Number:** {mobile_number}")
gmail="vksujma210590058545@gmail.com"
modile=9005865087
col3.markdown(f":red[**Mobile No:**] {modile}")
col3.markdown(f":red[**Gmail Id:**] {gmail}")
st.title(":rainbow[Certificates]")
da='https://github.com/vksujma210590058/Data_anlytics_certificates'
# col1.markdown("Data analytics course from Edubridge ")
st.markdown(f":red[Data Analytics Ceritificates] : {da}")
# PDF file path (replace 'document.pdf' with the path to your PDF file)
# pdf_path_sql_basic = "sql_basic.pdf"
# PDF file path (replace 'document.pdf' with the path to your PDF file)
# pdf_path = pdf_path_sql_basic
# st.markdown('''
#     :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
#     :gray[pretty] :rainbow[colors].''')
st.image('math.png', caption="Aptitude Test Preparation for Job Seekers",width=800)
st.image('sql_basic.png', caption="Sql Basic Certificate from HackerRank",width=800)
st.image('sql_inter.png', caption="sql Intermidiate Certificate from HackerRank",width=800)
st.image('python_basic.png', caption="Python Basic  Certificate from HackerRank",width=800)
st.title(":rainbow[Project]")
netfix="https://ntfxnextdaysharepriceprediction-vikas.streamlit.app/"
net_rep="https://github.com/vksujma210590058/MACHINE-LEARNING-PROJECT-OF-THE-NETFLIX-SHARE-PRICE-PREDICTION"
st.markdown(":rainbow[♥♥♥NETFLIX_SHARE_PRICE_PREDICTION♥♥♥☻♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥]")
st.markdown(f""":red[Netflix share price prediction] collecting the data of the netflix from the internet
:red[clean data handle null_value and duplicates...]:pink[EDA for better understanding] :rainbow[Preprocessing lable_encoder train_test_split]:yellow[Train and Text the model optimise the error]
:red[deploy our model on Internet]
:red[Link of the Model]{netfix}
:yellow[gitgublink :{net_rep}]""",)

zomato="https://zomatodataanalysis-app.streamlit.app/"
zomato_rep="https://github.com/vksujma210590058/zomato_data_analysis"
st.markdown(":rainbow[♥♥♥ZOMATO DATA ANALYSIS♥♥♥☻♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥]")
st.markdown(f""":red[Zomato data analysis] collecting the data of the zomato from the internet
:red[clean data handle null_value and duplicates...]:pink[apply the groupby and understand the data] :rainbow[data visulization ]:yellow[finally deploy the dashboard on the internet]
:red[Website of the Model]{zomato}
:yellow[gitgublink :{zomato_rep}]""",)

zomato="https://zomatodataanalysis-app.streamlit.app/"
customer_churn="https://github.com/vksujma210590058/DATA-VISULIZATION"
st.markdown(":rainbow[♥♥♥TELECOM CUSTOMER_CHURN DATA ANALYSIS♥♥♥☻♥♥♥♥♥♥♥♥♥♥♥♥]")
st.markdown(f""":red[customer_churn data analysis] collecting the data of the customer_churn from the internet
:red[clean data handle null_value and duplicates...]:pink[apply the groupby and understand the data] :rainbow[data visulization ]:yellow[finally deploy the dashboard on the internet]
:red[Website of the Model]{customer_churn}
:yellow[gitgublink :{customer_churn}]""",)

simple_visualization_git="https://github.com/vksujma210590058/simple_way_to_visulization"
viz_web="https://simplewaytovisualization-simple-way-to-visualization-data.streamlit.app/"
st.markdown(":rainbow[♥♥♥Simple Way To Understand The Your Data ♥♥♥☻♥♥♥♥♥♥♥♥♥♥♥♥]")
st.markdown(f""":red[ data analysis] upload the from you system 
:red[data should be clean ]:pink[ then click on the button to see the graph 2d and 3d] :rainbow[data visulization ]:yellow[finally deploy the dashboard on the internet]
:red[Website of the Model]{viz_web}
:yellow[gitgublink :{simple_visualization_git}]""",)

