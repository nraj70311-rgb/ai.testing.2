import streamlit as st
from pages.analytics import show_analytics
from pages.history import show_history
from app.database.db_init import init_db
from app.auth.session_manager import initialize_session, logout

from pages.login import show_login
from pages.register import show_register
from pages.dashboard import show_dashboard
from pages.analyzer import show_analyzer

# Page Configuration

st.set_page_config(
page_title="AI Website Testing Platform",
layout="wide"
)

# Initialize Database

init_db()

# Initialize Session

initialize_session()

# -----------------------------

# NOT LOGGED IN

# -----------------------------

if not st.session_state.logged_in:


    tab1, tab2 = st.tabs(
        ["Login", "Register"]
    )

    with tab1:
        show_login()

        with tab2:
            show_register()


# -----------------------------

# LOGGED IN

# -----------------------------

else:


    st.sidebar.success(f"Logged in as: {st.session_state.user_email}")

    menu = st.sidebar.radio(
    "Navigation",
    [
    "Dashboard",
    "Website Analyzer",
    "Scan History",
    "Analytics"
    ]
    )


    if st.sidebar.button("Logout"):
        logout()

    if menu == "Dashboard":
        show_dashboard()

    elif menu == "Website Analyzer":
        show_analyzer()
    elif menu == "Scan History":
            show_history()
    elif menu == "Analytics":
        show_analytics()


