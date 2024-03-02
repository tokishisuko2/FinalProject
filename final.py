import csv
import random

class CarSearch:
    def __init__(self, filename):
        self.filename = filename
        self.selected_cars = []
        self.wallet = 10000

    def clear_text_file(self):
        try:
            with open("selected_cars.txt", mode='w') as file:
                file.write("Balance: $10000\n")
            print("selected_cars.txt has been cleared and initialized with balance.")
        except Exception as e:
            print(f"Error occurred while clearing the text file: {e}")

    def extract_cars_by_name(self, car_name):
        try:
            with open(self.filename, mode='r') as file:
                reader = csv.DictReader(file)
                self.cars = [row for row in reader if car_name.lower() in row['Name'].lower()]
        except FileNotFoundError:
            print("File was not found.")

    def search_by_type(self, car_type):
        return [car for car in self.cars if car["Type"].lower() == car_type.lower()]

    def search_cars(self):
        while len(self.selected_cars) < 5:
            car_name = input("Which brand do you want to search? (Enter 'done' when finished): ")
            if car_name.lower() == 'done':
                break

            self.extract_cars_by_name(car_name)

            if not self.cars:
                print("No cars found with the given name.")
                continue

            car_type = input("What type of car do you want to search? ")
            selected_brand_cars = self.search_by_type(car_type)

            if not selected_brand_cars:
                print("No cars found with the given type.")
                continue

            print("Available cars for selection:")
            for idx, car in enumerate(selected_brand_cars, 1):
                print(f"{idx}. {car['Name']}, {car['Type']}, HP: {car['Horsepower(HP)']}")
            print()

            while len(self.selected_cars) < 5:
                car_choice = input("Which car do you want to choose? (Enter number or 'done' to finish): ")
                if car_choice.lower() == 'done':
                    break
                try:
                    car_index = int(car_choice) - 1
                    if 0 <= car_index < len(selected_brand_cars):
                        chosen_car = selected_brand_cars[car_index]
                        if chosen_car in self.selected_cars:
                            reselect = input("This car is already selected. Do you want to choose again? (yes/no): ")
                            if reselect.lower() != 'yes':
                                continue
                        self.selected_cars.append(chosen_car)
                        print(f"Added {chosen_car['Name']} to your garage. HP: {chosen_car['Horsepower(HP)']}")
                        self.write_car_to_text_file(chosen_car)
                    else:
                        print("Please choose a valid number.")
                except ValueError:
                    print("Please enter a valid number or 'done'.")
            print()

        print("Your selected cars:")
        for idx, car in enumerate(self.selected_cars, 1):
            print(f"{idx}. {car['Name']}, HP: {car['Horsepower(HP)']}")
        print()

    def write_car_to_text_file(self, car):
        try:
            with open("selected_cars.txt", mode='a') as file:
                file.write(f"{car['Name']}, {car['Type']}, HP: {car['Horsepower(HP)']}\n")
        except Exception as e:
            print(f"Error occurred while writing to the text file: {e}")

    def update_balance_in_text_file(self):
        try:
            with open("selected_cars.txt", mode='r') as file:
                lines = file.readlines()
            
            # Step 2: Update the balance line
            lines[0] = f"Balance: ${self.wallet}\n"
            with open("selected_cars.txt", mode='w') as file:
                file.writelines(lines)
                print(f"Balance updated in the selected_cars.txt file: ${self.wallet}")
        except Exception as e:
            print(f"Error occurred while updating balance in the text file: {e}")

class CarGame:
    def __init__(self, filename):
        self.filename = filename
        self.wallet = 10000

    def games(self, selected_cars):
        if not selected_cars:
            print("You haven't selected any cars yet.")
            return

        race_choice = input("Which car do you want to race with? (Enter number): ")
        try:
            race_index = int(race_choice) - 1
            if 0 <= race_index < len(selected_cars):
                car1 = selected_cars[race_index]
                print(f"You chose to race with {car1['Name']}.")
                bet_amount = float(input(f"Your wallet balance is ${self.wallet}. How much do you want to bet? "))

                if bet_amount > self.wallet or bet_amount <= 0:
                    print("Invalid bet amount. Please try again with a valid amount within your wallet balance.")
                    return

                with open(self.filename, mode='r') as file:
                    reader = csv.DictReader(file)
                    all_cars = list(reader)
                    if not all_cars:
                        print("No cars found in the CSV file.")
                        return

                    random_car = random.choice(all_cars)
                    print(f"Randomly chosen car from the CSV file: {random_car['Name']}, HP: {random_car['Horsepower(HP)']}")

                    if int(car1['Horsepower(HP)']) >= int(random_car['Horsepower(HP)']):
                        print(f"You won the race against {random_car['Name']}.")
                        self.wallet += bet_amount * 2
                        print(f"You won ${bet_amount * 2}! Your new wallet balance is ${self.wallet}.")
                    else:
                        print(f"You lost the race against {random_car['Name']}.")
                        self.wallet -= bet_amount
                        print(f"You lost ${bet_amount}. Your new wallet balance is ${self.wallet}.")
                    self.update_balance_in_text_file()
            else:
                print("Invalid selection. Please choose a valid number.")
        except ValueError:
            print("Please enter a valid number.")
        print()

    def update_balance_in_text_file(self):
        try:
            with open("selected_cars.txt", mode='r') as file:
                lines = file.readlines()
            lines[0] = f"Balance: ${self.wallet}\n"
            with open("selected_cars.txt", mode='w') as file:
                file.writelines(lines)
                print(f"Balance updated in the selected_cars.txt file: ${self.wallet}")
        except Exception as e:
            print(f"Error occurred while updating balance in the text file: {e}")


car_search = CarSearch('cars.csv')
car_search.clear_text_file()  # Initialize the text file with balance
car_search.search_cars()

car_game = CarGame('cars.csv')
car_game.games(car_search.selected_cars)
