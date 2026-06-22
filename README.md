# **🏎️ Python F1 Race Simulator**

A lightweight, object-oriented command-line application that simulates a Formula 1 Grand Prix. The simulation calculates dynamic, randomized lap times based on driver skill vectors, concluding with a final leaderboard and a victory audio sequence.

Developed by Samridhi Gupta as a portfolio project showcasing Python OOP paradigms.  
GITHUB: https://github.com/Samridhi-g-dev

## **Key Features**

* **Object-Oriented Architecture:** Strictly adheres to encapsulation principles by decoupling the driver data layer from the race orchestration engine.  
* **Dynamic Lap Calculations:** Simulates realistic lap-time variances using Python's `random.uniform` to represent human consistency and track conditions.  
* **Dynamic Event-Driven Audio:** Integrates `pygame` to conditionally load and play unique victory audio tracks on the condition of which driver wins the race.  
* **Decoupled Configuration:** Highly scalable architecture. Adding more drivers or changing victory audio clips requires zero modification to the core game loop.

## **System Architecture & OOP Concepts**

By designing and building this project, I mastered several fundamental software engineering paradigms:

### **1\. Encapsulation**

Rather than managing loose lists or dictionaries, driver statistics (`name`, `team`, `_skill`, `audio_file`) and behaviors (`calc_lap_time()`) are bound together within a single `Driver` class. Internal state variables (like skill) are marked as protected to prevent accidental external modification.

### **2\. State Management**

The `Race` class coordinates multiple iterations over collections of custom objects. It updates and maintains the active state (`total_time`) of each driver object across nested loops without destroying reference integrity.

### **3\. Decoupling and Polymorphism**

The `Race` class does not hardcode who is racing or what audio files exist. It interacts solely with the abstract interface of the objects passed to it. This allows for infinite scalability (e.g., adding 50 more drivers) without altering a single line of the `Race` logic.

## **Installation & Setup**

Follow these steps to run the simulation locally on your machine.

### **Prerequisites**

Ensure you have Python 3.8 or higher installed.

### **1\. Clone the Repository**

git clone \[https://github.com/Samridhi-g-dev/python-F1-race-simulator\](https://github.com/Samridhi-g-dev/f1-race-simulator.git)  
cd python-F1-race-simulator

### **2\. Set Up a Virtual Environment**

\# Windows  
python \-m venv venv  
venv\\Scripts\\activate

\# macOS/Linux  
python3 \-m venv venv  
source venv/bin/activate

### **3\. Install Dependencies**

This project utilizes `pygame` for stable, cross-platform audio streaming:

pip install pygame

### **4\. Project Structure**

Ensure your files are organized as follows:

f1-race-simulator/  
│  
├── carlos.mp3  
├── george.mp3  
├── leclerc.mp3  
├── DUDUDUDU MAXX VERSTA--\_audio\_file.mp3  
│  
├── main.py             \# Main execution script  
└── README.md

### **5\. Run the Application**

python main.py

## **Sample Console Execution**

\------------------------------  
   🏆 FINAL LEADERBOARD 🏆     
\------------------------------  
1\. Max Verstappen \- Total Time: 5252.2 seconds  
2\. George Russell \- Total Time: 5314.61 seconds  
3\. Charles Leclerc \- Total Time: 5459.82 seconds  
4\. Carlos Sainz \- Total Time: 5558.2 seconds  
\------------------------------

🏆 WINNER: Max Verstappen from Red Bull\! 🏆  
\[System\] Initializing audio subsystem...  
\[System\] Playing winner's audio: DUDUDUDU MAXX VERSTA--\_audio\_file.mp3

## **Note on Audio Assets**

The simulation engine is designed to be fully professional and decoupled, but it is currently loaded with a comical/meme sound pack of 4 audios (one per Driver) to demonstrate how easily custom audio assets can be dynamically mapped to individual objects.

## **Extending and Customizing**

To modify the drivers or the sounds that trigger when they win, locate the instantiations at the bottom of `main.py` and modify the parameters:

\# To add a new driver:  
new\_driver \= Driver(  
    name="Your Name",  
    team="Your Custom Team",  
    skill=10,   
    audio\_file="your\_custom\_victory.mp3"  
)

## **License**

This project is open-source and licensed under the MIT License.