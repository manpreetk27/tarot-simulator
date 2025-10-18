import streamlit as st
from src.utils.persistence import load_readings
from datetime import datetime

def show_journal_reflection_page():
    st.markdown("<h1 style='color:#5B2C6F; text-align:center;'>🪞 Your Reflection Journal</h1>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("""
    This is your sacred space to reflect on your tarot readings.<br><br>
    Browse your saved readings below or write fresh reflections inspired by your recent experiences.<br><br>
    <i>Every entry is a step toward deeper self-awareness and intuition.</i>
    """, unsafe_allow_html=True)

    readings = load_readings()
    if not readings:
        st.info("You haven't saved any readings yet. Perform a reading to start your journal!")
        return
    if readings:
        st.markdown("### 🧿 Your Saved Readings")
        for r in reversed(readings):
            # Format date as "17 Oct 2025"
            date_str = r["timestamp"].split(" ")[0]
            formatted_date = datetime.strptime(date_str, "%Y-%m-%d").strftime("%d %b %Y")
            expander_title = f"🔆 {r['reading_type']} | {formatted_date}"
            with st.expander(expander_title):
                st.write("**Cards Drawn:**")
                for c in r["cards"]:
                    orientation = "Reversed" if c["is_reversed"] else "Upright"
                    st.write(f"- **{c['name']}** ({orientation})")
                    st.write(f"  _Meaning:_ {c.get('meaning', 'No meaning available.')}")
                if r["reflection"]:
                    st.write(f"**Reflection:** {r['reflection']}")
                else:
                    st.write("_No reflection added._")
        st.markdown("---")
