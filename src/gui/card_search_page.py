import streamlit as st
from src.utils.card_search import load_cards

def show_card_search_page():
    st.markdown("<h1 style='color:#5B2C6F; text-align:center;'>🔍 Tarot Card Search</h1>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("""
    Search for any tarot card to uncover its meaning and insights.<br><br>
    <i>Let curiosity be your guide — each card has a story to tell.</i>
    """, unsafe_allow_html=True)

    all_cards = load_cards()
    search_query = st.text_input("Enter the card name (e.g., 'The Fool' or '3 of Cups'):")

    if search_query:
        found_card = None
        for card in all_cards:
            if search_query.lower() in card["name"].lower():
                found_card = card
                break

        if found_card:
            st.markdown(f"### 🌟 {found_card['name']}")
            st.markdown(f"**Arcana:** {found_card.get('arcana', 'Unknown')}")
            general = found_card.get("general")
            if general:
                st.markdown(f"**Meaning (Upright):** {general.get('upright', 'No meaning available.')}")
                st.markdown(f"**Meaning (Reversed):** {general.get('reversed', 'No meaning available.')}")
            else:
                st.warning("No general meaning available for this card.")
        else:
            st.warning("No matching card found. Try refining your search.")