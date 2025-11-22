import streamlit as st
from src.utils.persistence import load_readings
from datetime import datetime # for date formatting
import os  # for file operations
import json # for exporting readings

READINGS_FILE = "src/data/readings.json" # Path to readings file

def show_journal_reflection_page():
    """Displays the Reflection Journal page in the Streamlit app."""
    st.markdown("<h1 style='color:#5B2C6F; text-align:center;'>🪞 Your Reflection Journal</h1>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("""
    This is your sacred space to reflect on your tarot readings.<br><br>
    Browse your saved readings below or write fresh reflections inspired by your recent experiences.<br><br>
    <i>Every entry is a step toward deeper self-awareness and intuition.</i>
    """, unsafe_allow_html=True)


    # Clear Readings Button
    if st.button("🗑️ Clear All Readings"):
        if os.path.exists(READINGS_FILE): # check if file exists
            with open(READINGS_FILE, "w", encoding="utf-8") as f: # open file in write mode
                f.write("[]") # clear contents
            st.success("All readings have been cleared!")
        else:
            st.info("No readings to clear.")

    # Export Readings Button
    readings = load_readings() # load readings
    if readings:
        st.download_button(
            label="⬇️ Export Readings (JSON)",
            data=json.dumps(readings, indent=2, ensure_ascii=False), # convert readings to JSON string
            file_name="my_tarot_readings.json", # suggested file name
            mime="application/json" # MIME type
        )

    readings = load_readings() # Load saved readings
    if not readings:
        st.info("You haven't saved any readings yet. Perform a reading to start your journal!")
        return
    if readings:
        st.markdown("### 🧿 Your Saved Readings")
        for r in reversed(readings):
            # Format date as "17 Oct 2025"
            date_str = r["timestamp"].split(" ")[0] # get date part
            formatted_date = datetime.strptime(date_str, "%Y-%m-%d").strftime("%d %b %Y") # format date
            expander_title = f"🔆 {r['reading_type']} | {formatted_date}" # create expander title
            with st.expander(expander_title): # create expander for each reading
                st.write("**Cards Drawn:**") # display cards
                for c in r["cards"]: # iterate through cards
                    orientation = "Reversed" if c["is_reversed"] else "Upright" # get orientation
                    st.write(f"- **{c['name']}** ({orientation})") # display card name and orientation
                    st.write(f"  _Meaning:_ {c.get('meaning', 'No meaning available.')}") # display meaning
                if r["reflection"]: # if reflection exists
                    st.write(f"**Reflection:** {r['reflection']}") # display reflection
                else:
                    st.write("_No reflection added._") # no reflection message
        st.markdown("---")
