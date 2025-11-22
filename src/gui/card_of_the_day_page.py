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

    daily = load_daily_card() # load saved card

    if daily:
        card_name = daily["card"]["name"] # get card name
        meaning = daily["card"]["meaning"] # get card meaning
        orientation = "Reversed" if daily["card"]["is_reversed"] else "Upright" # get orientation
        st.success(f"✨ Your Card of the Day ({orientation}) ✨") # show orientation
        st.markdown(f"### {card_name}") # show card name
        st.write(meaning) # show card meaning
    else:
        if st.button("🔮 Reveal Today's Card"):
            deck = Deck() # create new deck
            deck.shuffle() # shuffle deck
            card = deck.draw_card() # draw a card

            is_reversed = random.choice([True, False]) # randomly decide orientation
            card.set_orientation(is_reversed) # set card orientation
            meaning = card.get_meaning("general") # get card meaning

            daily_card = { 
                "date": str(date.today()),
                "card": {
                    "name": card.name,
                    "is_reversed": is_reversed,
                    "meaning": meaning
                }
            }

            save_daily_card(daily_card) # save drawn card
            st.rerun()  # refresh to show saved card