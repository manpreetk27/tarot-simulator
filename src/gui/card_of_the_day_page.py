import streamlit as st
import random 
from datetime import date 
from src.models.deck import Deck
from src.spreads.card_of_the_day import load_daily_card, save_daily_card

def show_card_of_the_day_page(deck: Deck):
    st.markdown("<h1 style='color:#5B2C6F; text-align:center;'>🌞 Card of the Day</h1>", unsafe_allow_html=True)
    st.markdown("---")

    st.markdown("""
    Each day brings new energy and guidance.<br>
    Your **Card of the Day** reflects the theme or insight that may shape your path today.<br><br>
    This card can offer wisdom, encouragement, or a gentle nudge to pay attention to certain aspects of your life.<br><br>
    Remember, the cards are a tool to connect with your intuition and inner knowing.<br><br>
    <i>Focus your intention... and reveal your card.</i>
    """, unsafe_allow_html=True)

    daily = load_daily_card()

    if daily:
        card_name = daily["card"]["name"]
        meaning = daily["card"]["meaning"]
        orientation = "Reversed" if daily["card"]["is_reversed"] else "Upright"
        st.success(f"✨ Your Card of the Day ({orientation}) ✨")
        st.markdown(f"### {card_name}")
        st.write(meaning)
    else:
        if st.button("🔮 Reveal Today's Card"):
            deck = Deck()
            deck.shuffle()
            card = deck.draw_card()

            is_reversed = random.choice([True, False])
            card.set_orientation(is_reversed)
            meaning = card.get_meaning("general")

            daily_card = {
                "date": str(date.today()),
                "card": {
                    "name": card.name,
                    "is_reversed": is_reversed,
                    "meaning": meaning
                }
            }

            save_daily_card(daily_card)
            st.rerun()  # refresh to show saved card