import streamlit as st
from time import sleep
import streamlit.components.v1 as components

st.set_page_config(page_title="Select Year", page_icon="RSS.png", layout="wide")

if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
    with st.spinner('You must log in first!'):
        sleep(2)
        st.switch_page("pages/admin.py")

username = st.session_state["Username"]
mycode = f"<script>alert('Welcome, {username}!');</script>"
components.html(mycode, height=0, width=0)
# Custom CSS for alignment, button size, and background color
st.markdown("""
    <style>
        .centered {
            text-align: center;
        }
        .stButton>button {
            background-color: #075378;
            color: white;
            font-size: 20px;
            padding: 15px 40px;
            border-radius: 10px;
            width: 100%;
        }
        .stButton>button:hover{
            background-color: white;
            color:black;
        }
        #root > div:nth-child(1) > div.withScreencast > div > div{
            background: linear-gradient(145deg, #00a2f17d, #00a2f1, #1470b3);
        }
        #root > div:nth-child(1) > div.withScreencast > div > div > section > div.stMainBlockContainer.block-container> div > div > div > div > div > button > div > p{
            font-size:32px;
        }
        /*logo*/
        #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.stAppViewBlockContainer.block-container > div > div > div > div:nth-child(3) > div > div > div > img{
            background-color: white;
            border-radius: 100px;
            padding: 15px;
            align-item:center;
            margin-right:30px;
        }
        #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.stAppViewBlockContainer.block-container > div > div > div > div:nth-child(3) > div > div{
            display: flex;
            justify-content: center;
            align-items: center;
            text-align: center;
        }
        /*attendance-portal*/
        #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.stAppViewBlockContainer.block-container > div > div > div > div:nth-child(4) > div > div > div > div > h1,
        #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.stAppViewBlockContainer.block-container > div > div > div > div:nth-child(5) > div > div > div > div > h3{
            color:white;
        }
        /*st.error*/
        .stAlert{
            background-color:white;
            border-radius:10px;
            text-align:center;
        }
        
    </style>
""", unsafe_allow_html=True)

# Display the logo (optional)
st.image('Robust-Logo-400x84.png', width=300)

# Page header
st.markdown("<div class='centered'><h1>Attendance Portal</h1></div>", unsafe_allow_html=True)

# Subtitle
st.markdown("<div class='centered'><h3>Select the Year Below:</h3></div>", unsafe_allow_html=True)

# Add functionality with Streamlit's native button
if st.button("2025"):
    # st.session_state['filename'] = "Attendance '24.xlsx"
    # st.switch_page("pages/month_admin.py")
    st.error('Wait till new Year')
    
if st.button("2024"):
    st.session_state['filename'] = "Attendance '24.xlsx"
    st.session_state['timesheet_filename'] = "Timesheet.xlsx"
    st.switch_page("pages/month_admin.py")
    

st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background-color: white;
        color: black;
        text-align: center;
        padding: 10px 0;
        font-size: 16px;
        box-shadow: 0 -2px 5px rgba(0, 0, 0, 0.2);
    }
    .footer .small-text {
        font-size: 14px;
        color: black;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="footer">
        Robust Support & Solution. All rights reserved.<br>
        <span class="small-text">Developed with ❤️ by Development Team</span>
    </div>
    """,
    unsafe_allow_html=True
)
