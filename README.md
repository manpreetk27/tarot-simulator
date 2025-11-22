# 🔮 Tarot Simulator

A modern tarot reading simulator built with Python and Streamlit. Draw cards, get meaningful interpretations, and keep a journal of your readings.

---
<img width="1000" height="600" src="https://github.com/manpreetk27/tarot-simulator/blob/9d9ef36cdd733747d8eacb7c1a52cce091241b89/assets/screen.png" />

## 🌙 Features

- **Card of the Day:** Draw a single card for daily guidance
- **Past, Present, Future Spread:** A classic three-card spread
- **Custom Spreads:** Create your own spreads with any number of cards
- **Reading Types:** General, Love, and Career readings
- **Journal:** Save and track all your readings with reflections
- **Insights:** See your most frequently drawn cards and reading statistics
- **Export:** Download your readings as JSON

## ⚡️ Installation

1. Clone the repository:
```bash
git clone https://github.com/manpreetk27/tarot-simulator.git
cd TarotSimulator
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Mac/Linux
# or
venv\Scripts\activate  # On Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## 🪐 Running the App

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## 🏷️ Project Structure

```
src/
├── models/           # Card and Deck classes
├── spreads/          # Reading spread logic
├── gui/              # Streamlit pages
├── utils/            # Helper functions
└── data/             # JSON card data
```

## 📁 Card Data

The app includes comprehensive tarot interpretations for:
- 22 Major Arcana cards
- 56 Minor Arcana cards (Wands, Cups, Swords, Pentacles)

Each card has meanings for:
- General readings
- Love readings
- Career readings
- Both upright and reversed orientations

## 🪄 Usage

1. **Card of the Day:** Click "Reveal Today's Card" for daily guidance
2. **Standard Reading:** Choose "Past, Present, Future" for a classic spread
3. **Custom Spread:** Create a personalized spread with custom positions
4. **Save Reflection:** Add your thoughts to each reading
5. **View Journal:** See all your saved readings with insights

## 💿 Tech Stack

- **Python 3.13**
- **Streamlit** - Web app framework
- **JSON** - Card data storage

## 📎 Future Enhancements

- Additional spread types (Celtic Cross, Wheel of the Year, etc.)
- Card interpretations in multiple languages
- User accounts and cloud storage
- AI-powered reading suggestions

## License

This project is open source.

---
