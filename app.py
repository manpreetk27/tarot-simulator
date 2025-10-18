import streamlit as st
from src.gui.main_dashboard import show_dashboard
from src.gui.past_present_future_readings import show_reading_page
from src.gui.about import show_about_page
from src.gui.journal_reflection import show_journal_reflection_page
from src.gui.custom_spread import show_custom_spread_page
from src.gui.journal_insights import show_insights_page
from src.gui.card_of_the_day_page import show_card_of_the_day_page
from src.models.deck import Deck 
from src.gui.card_search_page import show_card_search_page

deck = Deck()

# Initialize session state for page
if "page" not in st.session_state:
    st.session_state.page = "Dashboard"

st.sidebar.title(" Tarot Reading Simulator")
page = st.sidebar.radio(
    "Navigate",
    ["Dashboard", "Past, Present, Future Reading", "The History", "Reflection Journal", "Custom Spread", "Journal Insights", "Card of the Day", "Tarot Card Search"],
    index=["Dashboard", "Past, Present, Future Reading", "The History", "Reflection Journal", "Custom Spread", "Journal Insights", "Card of the Day", "Tarot Card Search"].index(st.session_state.page)
)

# Update session state when sidebar changes
st.session_state.page = page

# Page routing
if st.session_state.page == "Dashboard":
    show_dashboard()
elif st.session_state.page == "Past, Present, Future Reading":
    show_reading_page()
elif st.session_state.page == "The History":
    show_about_page()
elif st.session_state.page == "Reflection Journal":
    show_journal_reflection_page()
elif st.session_state.page == "Custom Spread":
    show_custom_spread_page()
elif st.session_state.page == "Journal Insights":
    show_insights_page()
elif st.session_state.page == "Card of the Day":
    show_card_of_the_day_page(deck)
elif st.session_state.page == "Tarot Card Search":
    show_card_search_page()