import streamlit as st
import pandas as pd

# Load CSV file with usernames and passwords
@st.cache_data
def load_user_data():
    return pd.read_csv("admin_data.csv")  # Ensure this CSV exists with columns 'Username' and 'Password'
st.set_page_config(page_title="Attendance Dashboard",page_icon="RSS.png",initial_sidebar_state="collapsed")
st.markdown("""
        <style>
        div.stHeading{
            text-align:center;
        }
        div.stFormSubmitButton > button {
            background-color: #075378;
            color: white;
            border-radius: 100px;
            height: 50px;
            width: 100%;
            font-size: 14px;
            margin: 5px;
        }
        #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.stAppViewBlockContainer.block-container > div > div > div > div:nth-child(2) > div > div > div > h1{
            color:whitesmoke;
            font-size:xx-large
        }
        #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.stAppViewBlockContainer.block-container > div > div > div > div.stForm{
            background-color:white;
        }
        div.stFormSubmitButton > button:hover {
            background-color: #4cbef6;
            color: white;
        }
        #root > div:nth-child(1) > div.withScreencast > div > div{
            background:  linear-gradient(145deg, #00a2f17d, #00a2f1, #1470b3);
        }
        
        #root > div > div.withScreencast > div > div > section > div.stMainBlockContainer.block-container > div > div > div > div.stForm > div > div > div > div > div > label > div > p{
            color:white;
        }
        .stAlert{
            background-color:white;
            border-radius:30px;
        }
        /*button*/
        #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.stAppViewBlockContainer.block-container > div > div > div > div:nth-child(6) > div > button{
            display: block;
            margin: 0 auto; /* Center the button */
            background-color: #27be27; /* Set background color to green */
            color: white; /* Set font color to white */
            border: none; /* Remove border */
            padding: 10px 20px; /* Add padding for better aesthetics */
            border-radius: 5px; /* Optional: rounded corners */
            font-size: 16px; /* Set font size */
            cursor: pointer; /* Change cursor to pointer on hover */
        }
        #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.stAppViewBlockContainer.block-container > div > div > div > div:nth-child(6) > div > button:hover {
            background-color: darkgreen; /* Darker green on hover */
        }
        /*admin panel heading*/
        #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.stAppViewBlockContainer.block-container > div > div > div > div:nth-child(3) > div > div > div > h3{
            color:white;
        }
        </style>
    """, unsafe_allow_html=True)
def main():
    st.title("❚█══ Robust Support & Solution ══█❚")
    st.subheader("𝑨𝒅𝒎𝒊𝒏 𝑷𝒂𝒏𝒆𝒍")

    # Load user data
    user_data = load_user_data()
    usernames = user_data["Username"].tolist()

    # Initialize session state variables
    if "authentication_status" not in st.session_state:
        st.session_state["authentication_status"] = False
        st.session_state["logged_in"] = False
        st.session_state["Username"] = None

    with st.form("login_form", clear_on_submit=True):
        if not st.session_state["authentication_status"]:
            selected_username = st.selectbox("👤 Username", usernames)
            password = st.text_input("🔑 Password", type="password")
            login_btn = st.form_submit_button("Login")

            if login_btn:
                user_row = user_data[user_data["Username"] == selected_username]
                if not user_row.empty and str(user_row.iloc[0]["Password"]) == password:
                    st.success(f"Welcome, {selected_username}!")
                    st.session_state["logged_in"] = True
                    st.session_state["Username"] = selected_username
                    st.session_state["authentication_status"] = True
                    # Redirect to another page if implemented
                    st.switch_page("pages/year_admin.py")
                else:
                    st.error("Invalid username or password.")
        else:
            st.success(f"Welcome back, {st.session_state['Username']}!")
            # Redirect to another page
            st.switch_page("pages/year_admin.py")

if __name__ == "__main__":
    main()
# Create a regular Streamlit button
if st.button("Employee Panel"):
    # Navigate to the 'admin.py' page
    st.switch_page("login.py")
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
