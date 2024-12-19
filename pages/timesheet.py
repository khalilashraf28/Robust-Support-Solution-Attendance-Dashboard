import streamlit as st
import pandas as pd
from time import sleep
import streamlit.components.v1 as components
import pandas as pd
from streamlit_navigation_bar import st_navbar
import plotly.graph_objects as go


# Redirect if not logged in
if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
    with st.spinner('You must log in first!'):
        st.cache_data.clear()
        sleep(2)
        st.switch_page("login.py")

st.set_page_config(page_title="RSS Timesheet", layout="wide",page_icon="RSS.png",initial_sidebar_state="collapsed")
page = st_navbar(["","Home", "Late Analysis", "Time Sheet", "Month", "Logout"])

components.html(
    """
    <style>
        @media screen and (max-width: 768px) {
            body {
                -webkit-user-select: none;
                -webkit-touch-callout: none;
            }
        }
    </style>
    <meta name="viewport" content="width=1024">
    """,
    height=0,
)
if page == 'Home':
    st.switch_page("pages/main.py")
elif page == 'Late Analysis':
    st.switch_page("pages/late.py")
elif page == 'Time Sheet':
    pass
elif page == 'Month':
    st.switch_page("pages/month.py")
elif page == 'Logout':
    with st.spinner('Loging out'):
        st.cache_data.clear()
        sleep(2)
        st.session_state.clear() 
        st.switch_page("login.py")

@st.cache_data
def load_and_process_data(file_path, sheet_name,name):
    df = pd.read_excel(file_path,sheet_name=sheet_name)
    filtered_df=df[df['Name']==name]
    filtered_df['Date'] = pd.to_datetime(filtered_df['Date'], errors='coerce') 
    filtered_df = filtered_df.sort_values(by='Date', ascending=True) 
    return filtered_df

Name = st.session_state["Username"]   
# filtered_df = load_and_process_data(st.session_state['filename'], st.session_state['file'],Name)
# filtered_df = load_and_process_data(st.session_state['timesheet_filename'], st.session_state['timesheet_name'],Name)
# Check if the file or sheet name is available
try:
        # Attempt to load the data using the provided file and sheet names
    filtered_df = load_and_process_data(st.session_state['timesheet_filename'],st.session_state['timesheet_name'], Name)


    
    st.image('Robust-Logo-400x84.png', width=300) 
    st.title(f"Time Sheet")
    st.markdown("""
        <style>
        /*logo*/
            #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.stAppViewBlockContainer.block-container > div > div > div > div:nth-child(6) > div > div > div > img{
                background-color: white;
                border-radius: 100px;
                padding: 15px;
                align-item:center;
                margin-right:30px;
            }
            #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.stAppViewBlockContainer.block-container > div > div > div > div:nth-child(6) > div > div{
                display: flex;
                justify-content: center;
                align-items: center;
                text-align: center;
                margin-top:-50px;
            }
            /*body*/
            #root > div:nth-child(1) > div.withScreencast > div > div{
                background: linear-gradient(145deg, #00a2f17d, #00a2f1, #1470b3);
            }
            /*Title*/
            #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.stAppViewBlockContainer.block-container > div > div > div > div:nth-child(7) > div > div > div > h1{
            text-align: center;
            color:white;
            }
            /*Expanders*/
            #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.stAppViewBlockContainer.block-container > div > div > div > div:nth-child(10) > details,
            #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.stAppViewBlockContainer.block-container > div > div > div > div:nth-child(9) > details,
            #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.stAppViewBlockContainer.block-container > div > div > div > div:nth-child(11) > details{
                background-color:white;
            }
            /*Multiselect*/
            #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.stAppViewBlockContainer.block-container > div > div > div > div:nth-child(10){
                background-color:white;
                padding:10px;
                border-radius:10px;
            }
        </style>
    """, unsafe_allow_html=True)

    if not filtered_df[filtered_df['Name'] == Name].empty:
        try:
            with st.expander("", expanded=True):
                with st.container():
                    # Custom CSS for gradient cards and hover effect
                    st.markdown("""
                        <style>
                        .gradient-card {
                            border-radius: 10px;
                            padding: 20px;
                            text-align: center;
                            color: white;
                            margin: 10px;
                            font-family: Arial, sans-serif;
                            font-size: 16px;
                        }
                        .gradient-card h3 {
                            margin: 0;
                            font-size: 20px;
                        }
                        .gradient-card h2 {
                            margin: 0;
                            font-size: 28px;
                        }
                        .gradient-card:hover {
                            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
                            transform: scale(1.02);
                            transition: 0.3s;
                        }
                        </style>
                    """, unsafe_allow_html=True)

                    # Dashboard Columns
                    col1, col2 = st.columns(2)

                    # Card 1 - Department
                    with col1:
                        st.markdown(
                            f"""
                            <div class='gradient-card' style='background: linear-gradient(135deg, #00A5C2, #007899);'>
                                <h3>Department</h3>
                                <h2>{filtered_df['Department'].iloc[0]}</h2>
                            </div>
                            """, unsafe_allow_html=True
                        )
                        
                    # Card 2 - Name
                    with col2:
                        st.markdown(
                            f"""
                            <div class='gradient-card' style='background: linear-gradient(135deg, #FF4B78, #D9325E);'>
                                <h3>Name</h3>
                                <h2>{filtered_df['Name'].iloc[0]}</h2>
                            </div>
                            """, unsafe_allow_html=True
                        )
                    st.markdown(
                    f"""
                    <div class='gradient-card' style='background: linear-gradient(135deg, #FFB733, #FF8C00);'>
                        <h3>Total Days</h3>
                        <h2>{filtered_df.shape[0]}</h2>
                    </div>
                    """, unsafe_allow_html=True
                    )
            with st.expander("Filters", expanded=True):
                with st.container():
                    col1 , col2 = st.columns(2)
                    with col1:
                        # Styling for the Status multiselect div
                        status_options = filtered_df['Status'].unique()
                        selected_status = st.multiselect(
                            'Select Status',
                            options=status_options,
                        )
                        # Filtering the DataFrame based on the selected status
                        if selected_status:
                            filtered_df = filtered_df[filtered_df['Status'].isin(selected_status)]
                        else:
                            filtered_df = filtered_df
                            
                        
                            
                    with col2:  
                        # Styling for the Status multiselect div
                        # Define the correct order of the days
                        days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

                        # Sort the unique values of the 'Day' column based on this order
                        status_options = sorted(filtered_df['Day'].unique(), key=lambda x: days_order.index(x))
                        selected_status = st.multiselect(
                            'Select Day',
                            options=status_options,
                        )
                        # Filtering the DataFrame based on the selected status
                        if selected_status:
                            filtered_df = filtered_df[filtered_df['Day'].isin(selected_status)]
                        else:
                            filtered_df = filtered_df  
                    
                    # Add a slider for the Date range
                    date_min = filtered_df['Date'].min().date()  # Convert to datetime.date
                    date_max = filtered_df['Date'].max().date()  # Convert to datetime.date

                    # Create a slider to select a date range
                    selected_date = st.slider(
                        "Select a date range",
                        min_value=date_min,
                        max_value=date_max,
                        value=(date_min, date_max)
                    )

                    # Filter the DataFrame based on the selected date range
                    filtered_df = filtered_df[(filtered_df['Date'].dt.date >= selected_date[0]) & (filtered_df['Date'].dt.date <= selected_date[1])]

        except KeyError as e:
            st.warning(f"KeyError: Missing column in the dataframe or Employee was not hired - {e} Contact to Development Team")
        except IndexError as e:
            st.warning(f"You are not in the Index - {e} Contact to Development Team")
        except Exception as e:
            st.warning(f"You are not in the list: {e} Contact to Development Team")
            
        if filtered_df is not None:
            try:
                with st.expander("", expanded=True):
                    with st.container():
                        st.dataframe(
                            filtered_df.reset_index(drop=True),
                            height=300,
                            use_container_width=True
                        )
            except Exception as e:
                st.error(f"An error occurred: {e} Contact the Development Team")

    else:
        # HTML for the alert
        alert_html = f"""
        <div style="padding: 10px; background-color: #f8d7da; border: 1px solid #f5c2c7; color: #842029; border-radius: 5px; margin-bottom: 20px;">
            <strong>Alert:</strong> You are not listed on the attendance sheet of {st.session_state['Month']}.
        </div>
        """
        # {st.session_state['Month']}
        # Render the alert in the Streamlit app
        st.markdown(alert_html, unsafe_allow_html=True)      
except Exception as e:
    with st.spinner('Sheet was not introduced or Sheet is not Available'):
        st.cache_data.clear()
        sleep(3)
        st.switch_page("pages/month.py")
st.markdown(
"""
<style>
.query-box {
    /*background: linear-gradient(145deg, #d0227eb0, #6c3483);*/
    background-color:white;
    color: black;
    border-radius: 10px;
    padding: 20px;
    margin: auto;
    width: 80%; /* Adjust the width as needed */
    text-align: center;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}
.query-box h2 {
    margin: 0;
    font-size: 24px;
    color: black;
}
.query-box p {
    margin: 5px 0;
    font-size: 18px;
    color: black;
}

</style>
""",
unsafe_allow_html=True
)

st.markdown(
    """
    <div class="query-box">
        <h2>Send your queries to</h2>
        <p><a href="mailto:mustafas@xclusivetradinginc.com" style="color: black; text-decoration: none;">mustafas@xclusivetradinginc.com</a></p>
        <p>Ph: +923473090660</p>
    </div>
    """,
    unsafe_allow_html=True
)   

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
