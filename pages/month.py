import streamlit as st
from time import sleep

# Redirect if not logged in
if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
    with st.spinner('You must log in first!'):
        sleep(2)
    st.switch_page("login.py")
else:
    st.set_page_config(page_title="Select Month", layout="wide",page_icon="RSS.png",initial_sidebar_state="collapsed")
    username = st.session_state["Username"]
    # Display the logo (optional)
    st.image('Robust-Logo-400x84.png', width=300)
    st.title("Time Period Selection")

    button_style = """
        <style>
        div.stHeading{
            text-align:center;
        }
        div.stButton > button {
            background-color: #075378;
            color: white;
            border-radius: 100px;
            height: 50px;
            width: 100%;
            font-size: 14px;
            margin: 5px;
            cursor: pointer;
        }
        div.stButton > button:hover {
            background-color: white;
            color: black;
            border: 2px solid #4CAF50; /* Adds border */
            box-shadow: 0 0 10px 2px rgb(150, 148, 148, 0.8); /* Glowing border effect */
        }
        #root > div:nth-child(1) > div.withScreencast > div > div{
            background: linear-gradient(145deg, #00a2f17d, #00a2f1, #1470b3);
        }
        .stAlert{
            background-color:white;
            border-radius:30px;

        }
        /*logo*/
        #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.stAppViewBlockContainer.block-container > div > div > div > div:nth-child(1) > div > div > div > img{
            background-color: white;
            border-radius: 100px;
            padding: 15px;
            align-item:center;
            margin-right:30px;
        }
        #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.stAppViewBlockContainer.block-container > div > div > div > div:nth-child(1) > div > div{
            display: flex;
            justify-content: center;
            align-items: center;
            text-align: center;
        }
        
        #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.stAppViewBlockContainer.block-container.st-emotion-cache-1jicfl2.ea3mdgi5 > div > div > div > div:nth-child(2) > div > div > div > h1{
            color:white;
        }
        </style>
    """
    st.markdown(button_style, unsafe_allow_html=True)

    # st.success(f"Username {username}")
    col1, col2, col3,col4 = st.columns(4)
    with col1:
        if st.button("JANUARY"):
            st.session_state['file'] = "January Attendance"
            st.session_state['timesheet_name'] = "January timesheet" 
            st.session_state['Month'] = "January"
            st.switch_page("pages/main.py")
    with col2: 
        if st.button("FEBRUARY"):
            st.session_state['file'] = "February Attendance" 
            st.session_state['timesheet_name'] = "February timesheet" 
            st.session_state['Month'] = "February"
            st.switch_page("pages/main.py")
    with col3:
        if st.button("MARCH"):
            st.session_state['file'] = "March Attendance" 
            st.session_state['timesheet_name'] = "March timesheet" 
            st.session_state['Month'] = "March"
            st.switch_page("pages/main.py")
    with col4:
        if st.button("APRIL"):
            st.session_state['file'] = "April Attendance" 
            st.session_state['timesheet_name'] = "April timesheet" 
            st.session_state['Month'] = "April"
            st.switch_page("pages/main.py")
            
    col1, col2, col3,col4 = st.columns(4)
    with col1:
        if st.button("MAY"):
            st.session_state['file'] = "May Attandence" 
            st.session_state['timesheet_name'] = "May timesheet" 
            st.session_state['Month'] = "May"
            st.switch_page("pages/main.py")
    with col2: 
        if st.button("JUNE"):
            st.session_state['file'] = "June Attandence"
            st.session_state['timesheet_name'] = "June timesheet"  
            st.session_state['Month'] = "June"
            st.switch_page("pages/main.py")
    with col3:
        if st.button("JULY"):
            st.session_state['file'] = "July Attendence"
            st.session_state['timesheet_name'] = "July timesheet" 
            st.session_state['Month'] = "July" 
            st.switch_page("pages/main.py")
    with col4:
        if st.button("AUGUST"):
            st.session_state['file'] = "August Attendence"
            st.session_state['timesheet_name'] = "August timesheet" 
            st.session_state['Month'] = "August" 
            st.switch_page("pages/main.py")
    col1, col2, col3,col4 = st.columns(4)
    with col1:
        if st.button("SEPTEMBER"):
            st.session_state['file'] = "September Attendence"
            st.session_state['timesheet_name'] = "September Timesheet"  
            st.session_state['Month'] = "September"
            st.switch_page("pages/main.py")
    with col2: 
        if st.button("OCTOBER"):
            st.session_state['file'] = "October Attendence" 
            st.session_state['timesheet_name'] = "October Timesheet" 
            st.session_state['Month'] = "October"
            st.switch_page("pages/main.py")
    with col3:
        if st.button("NOVEMBER"):
            st.session_state['file'] = "November Attendence"
            st.session_state['timesheet_name'] = "November Timesheet"  
            st.session_state['Month'] = "November"
            st.switch_page("pages/main.py")
    with col4:
        if st.button("DECEMBER"):
            st.session_state['file'] = "December Attendence"
            st.session_state['timesheet_name'] = "December Timesheet"  
            st.session_state['Month'] = "December"
            st.switch_page("pages/main.py")
    
    # with col1:
    #     if st.button("JANUARY"):
    #         st.session_state['file'] = "January Attendance"
    #         st.session_state['timesheet_name'] = "January timesheet" 
    #         st.session_state['Month'] = "January"
    #         st.switch_page("pages/main.py")
    #     if st.button("MAY"):
    #         st.session_state['file'] = "May Attandence" 
    #         st.session_state['timesheet_name'] = "May timesheet" 
    #         st.session_state['Month'] = "May"
    #         st.switch_page("pages/main.py")
    #     if st.button("SEPTEMBER"):
    #         st.session_state['file'] = "September Attendence"
    #         st.session_state['timesheet_name'] = "September Timesheet"  
    #         st.session_state['Month'] = "September"
    #         st.switch_page("pages/main.py")
    # with col2:
    #     if st.button("FEBRUARY"):
    #         st.session_state['file'] = "February Attendance" 
    #         st.session_state['timesheet_name'] = "February timesheet" 
    #         st.session_state['Month'] = "February"
    #         st.switch_page("pages/main.py")
    #     if st.button("JUNE"):
    #         st.session_state['file'] = "June Attandence"
    #         st.session_state['timesheet_name'] = "June timesheet"  
    #         st.session_state['Month'] = "June"
    #         st.switch_page("pages/main.py")
    #     if st.button("OCTOBER"):
    #         st.session_state['file'] = "October Attendence" 
    #         st.session_state['timesheet_name'] = "October Timesheet" 
    #         st.session_state['Month'] = "October"
    #         st.switch_page("pages/main.py")
    # with col3:
    #     if st.button("MARCH"):
    #         st.session_state['file'] = "March Attendance" 
    #         st.session_state['timesheet_name'] = "March timesheet" 
    #         st.session_state['Month'] = "March"
    #         st.switch_page("pages/main.py")
    #     if st.button("JULY"):
    #         st.session_state['file'] = "July Attendence"
    #         st.session_state['timesheet_name'] = "July timesheet" 
    #         st.session_state['Month'] = "July" 
    #         st.switch_page("pages/main.py")
    #     if st.button("NOVEMBER"):
    #         st.session_state['file'] = "November Attendence"
    #         st.session_state['timesheet_name'] = "November Timesheet"  
    #         st.session_state['Month'] = "November"
    #         st.switch_page("pages/main.py")

    # with col4:
    #     if st.button("APRIL"):
    #         st.session_state['file'] = "April Attendance" 
    #         st.session_state['timesheet_name'] = "April timesheet" 
    #         st.session_state['Month'] = "April"
    #         st.switch_page("pages/main.py")
    #     if st.button("AUGUST"):
    #         st.session_state['file'] = "August Attendence"
    #         st.session_state['timesheet_name'] = "August timesheet" 
    #         st.session_state['Month'] = "August" 
    #         st.switch_page("pages/main.py")
    #     if st.button("DECEMBER"):
    #         st.session_state['file'] = "December Attendence"
    #         st.session_state['timesheet_name'] = "December Timesheet"  
    #         st.session_state['Month'] = "December"
    #         st.switch_page("pages/main.py")
            
            
            
            
    # disable = 'Week 51\n2nd-15th Dec is currently not available.'
    try:
        if disable:
            st.error(disable)
    except Exception as e:
        print('disable not available')

    if st.button("← Years"):
        st.switch_page("pages/year.py")



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