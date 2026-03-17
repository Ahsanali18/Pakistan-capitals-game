# 🇵🇰 Pakistan Capitals Guessing Game

An interactive Python game built using **Turtle Graphics** and **Pandas**, where users try to guess the capitals of Pakistan and see them appear on the map in real-time.

---

## 🎮 Project Overview

This project is inspired by map-based quiz games. The user is shown a map of Pakistan and is asked to guess the names of provincial and administrative capitals. Each correct guess is displayed on the map at its correct position.

The game continues until:

* All capitals are guessed, or
* The user chooses to exit

---

## 🚀 Features

* 🗺️ Interactive map using Turtle Graphics
* 📍 Real-time display of correct answers on the map
* 📊 Data handling using Pandas
* ❌ Tracks incorrect and missing guesses
* 💾 Option to export missed capitals for learning

---

## 🧠 Capitals Included

* Islamabad
* Lahore
* Karachi
* Peshawar
* Quetta
* Gilgit
* Muzaffarabad

---

## 🛠️ Technologies Used

* Python 🐍
* Turtle Graphics 🎨
* Pandas 📊

---

## 📂 Project Structure

```
Sporcle Pakistan Capital Finding Game/
│
├── main.py                    # Main game logic
├── pakistan_capitals.csv      # Capitals with x, y coordinates
├── cities_to_learn.csv        # Missed cities for user's learning
├── map.gif                    # Map image used in the game (collected from sprocle.com)
└── coordinates_collection.py  # Used to collect the cities locations from the map

```

---

## ▶️ How to Run

1. Clone this repository:

```
git clone https://github.com/ahsanali18/Pakistan-capitals-game.git
```

2. Navigate to the project folder:

```
cd Pakistan-capitals-game
```

3. Run the game:

```
python main.py
```

---

## 🎯 How to Play

* A prompt will ask you to enter a capital name
* If correct → it appears on the map
* If incorrect → try again
* Type **"Exit"** to quit and see missed capitals

---

## 💡 Future Improvements

* Add score tracking system
* Add timer mode ⏱️
* Include all major cities instead of only capitals
* GUI enhancement using Tkinter or PyQt

---

## 🤝 Contribution

Feel free to fork this repository and improve the project. Contributions are always welcome!

---

## 📜 License

This project is open-source and free to use for educational purposes.

---

## ⭐ Acknowledgment

Inspired by interactive geography quiz games and Python learning projects.
