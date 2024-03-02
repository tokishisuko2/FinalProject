# Car Search and Racing Game

This Python program simulates a car search and racing game. Users can search for cars by brand and type, select cars to add to their garage, and then participate in races against randomly chosen cars from a CSV file. The program keeps track of the user's wallet balance and updates it based on the outcome of the races.

## Features

- **CarSearch Class**: Allows users to search for cars by brand and type, select up to 5 cars to add to their garage, and writes the selected cars to a text file.
  
- **CarGame Class**: Simulates races between user-selected cars and randomly chosen cars from a CSV file. Users can bet on races, and winnings or losses are updated in the wallet balance.
  
- **Text File Management**: The program initializes a text file (`selected_cars.txt`) to store the user's selected cars and wallet balance. It updates the file with the latest balance after each race.

## Usage

1. Clone the repository or download the source code files.

2. Ensure you have Python installed on your system.

3. Run the `main.py` file.

4. Follow the on-screen instructions to search for cars, select cars to add to your garage, and participate in races.

## Requirements

- Python 3.x
- CSV file containing car data (e.g., `cars.csv`)

## File Structure

- `main.py`: Main script to run the car search and racing game.
- `cars.csv`: CSV file containing car data (name, type, horsepower, etc.).
- `selected_cars.txt`: Text file to store the user's selected cars and wallet balance.
- `README.md`: Documentation file providing information about the program.

## Author

Toki

