import random

# List of places to visit
places = ["Philadelphia", "San Diego", "New York City", "Los Angeles", "Chicago", "Boston", "Seattle", "Miami", "Denver", "Las Vegas", "Dallas", "San Francisco", "Portland", "Atlanta", "Austin", "Houston", "Washington D.C.", "Phoenix", "Charlotte", "Detroit", "Minneapolis", "Tampa", "Orlando", "Sacramento", "Pittsburgh", "Cleveland", "Baltimore", "Indianapolis", "Milwaukee", "Nashville", "Columbus", "Kansas City", "St. Louis", "Raleigh", "Oklahoma City", "New Orleans", "Memphis", "Louisville", "Jacksonville", "Virginia Beach", "Buffalo", "Birmingham", "Fresno", "Cincinnati", "Tucson", "Mesa", "Arlington", "Long Beach", "Newark", "Chula Vista", "Tulsa", "Aurora", "Anaheim", "Riverside", "Santa Ana", "Corpus Christi", "Lexington", "St. Paul", "Henderson",
          "Stockton", "Saint Petersburg", "Columbus", "Lincoln", "Anchorage", "Toledo", "Greensboro", "Plano", "Newport News", "Hialeah", "Fort Wayne", "Jersey City", "Chandler", "Laredo", "Norfolk", "Durham", "Madison", "Lubbock", "Winston-Salem", "Garland", "Glendale", "Huntington Beach", "Reno", "Chesapeake", "Scottsdale", "North Las Vegas", "Baton Rouge", "Irving", "Fremont", "Gilbert", "Bakersfield", "Boise", "Richmond", "San Bernardino", "Spokane", "Des Moines", "Modesto", "Fayetteville", "Birmingham", "Tacoma", "Oxnard", "Fontana", "Amarillo", "Moreno Valley", "Rochester", "Oceanside", "Montgomery", "Aurora", "Akron", "Yonkers", "Augusta", "Glendale", "Huntington Beach", "Mobile", "Little Rock", "Grand Rapids", "Salt Lake City", "Tallahassee", "Huntsville"]
number_of_places = len(places)

# List of restaurants to eat at
restaurants = ["Panda Express", "Auntie Anne's", "Chipotle", "Subway", "Olive Garden", "Red Lobster", "TGI Friday's", "Chili's", "Outback Steakhouse", "Buffalo Wild Wings", "Longhorn Steakhouse", "Texas Roadhouse", "Ruby Tuesday", "Cracker Barrel", "Red Robin", "Quiznos", "Five Guys", "Wendy's", "Burger King",
               "McDonald's", "Taco Bell", "KFC", "Popeyes", "Chick-fil-A", "Arby's", "Dairy Queen", "Sonic", "Waffle House", "IHOP", "Golden Corral", "Hard Rock Cafe", "Nathan's Famous", "Boston Market", "White Castle", "A&W Restaurants", "Mrs. Fields", "Marie Callender's", "Denny's", "Cold Stone Creamery", "Applebee's Neighborhood Grill + Bar", "Panera Bread", "The Cheesecake Factory", "Cinnabon", "Pizza Hut", "Dunkin' Donuts", "Krispy Kreme", "Baskin-Robbins"]
number_of_restaurants = len(restaurants)

# List of modes of transportation
transportation = ["Bus", "Train", "Car", "Plane", "Boat", "Bicycle", "Motorcycle", "Scooter",
                  "Skateboard", "Segway", "Hoverboard", "Unicycle", "Rollerblades", "Skiis", "Snowboard", "Horseback"]
number_of_transportation = len(transportation)

# List of entertainment
entertainment = ["Watching TV", "Going to the movies", "Listening to music", "Dancing", "Playing sports", "Surfing the internet", "Playing video games", "Going to a concert", "Going to a play", "Going to a museum", "Going to a zoo",
                 "Going to an amusement park", "Going to a water park", "Going to a theme park", "Fishing", "Going to the beach", "Going to a magic show", "Going to a comedy club", "Going on a wine tour", "Attending a festival", "Going to a circus"]
number_of_entertainment = len(entertainment)

# #total number of items in each list
# print(f'There are {number_of_places} places to visit.')
# print(f'There are {number_of_restaurants} restaurants to eat at.')
# print(f'There are {number_of_transportation} modes of transportation.')
# print(f'There are {number_of_entertainment} forms of entertainment.')

# Randomly select a place to visit
random_place = random.randint(0, number_of_places - 1)

# Randomly select a restaurant to eat at
random_restaurant = random.randint(0, number_of_restaurants - 1)

# Randomly select a mode of transportation
random_transportation = random.randint(0, number_of_transportation - 1)

# Randomly select a form of entertainment
random_entertainment = random.randint(0, number_of_entertainment - 1)

# Print the randomly selected items for the user
print(f'You should visit {places[random_place]}.\nYou should eat at {restaurants[random_restaurant]}.\nYou should travel by {transportation[random_transportation]}.\nYou should enjoy {entertainment[random_entertainment]}.\nDo you like these choices?\n(Y)es or (N)o')

# Ask the user if they like the choices
user_input = input()

# If the user likes the choices, print a message
if user_input == 'Y' or user_input == 'y':
    print(
        f'Good choice! Your day trip to {places[random_place]} is going to be great!')

# If the user does not like the choices, ask which choice they do not like
elif user_input == 'N' or user_input == 'n':
    print('Which choice do you not like?\n(P)lace, (R)estaurant, (T)ransportation, or (E)ntertainment')
    user_input = input()

    # If the user does not like the place, randomly select a new place
    if user_input == 'P' or user_input == 'p':
        random_place = random.randint(0, number_of_places - 1)
        print(f'You should visit {places[random_place]}.\nYou should eat at {restaurants[random_restaurant]}.\nYou should travel by {transportation[random_transportation]}.\nYou should enjoy {entertainment[random_entertainment]}.\nDo you like these choices?\n(Y)es or (N)o')
        user_input = input()
        if user_input == 'Y' or user_input == 'y':
            print(
                f'Good choice! Your day trip to {places[random_place]} is going to be great!')
        elif user_input == 'N' or user_input == 'n':
            print('You should stay home.')
    # If the user does not like the restaurant, randomly select a new restaurant
    elif user_input == 'R' or user_input == 'r':
        random_restaurant = random.randint(0, number_of_restaurants - 1)
        print(f'You should visit {places[random_place]}.\nYou should eat at {restaurants[random_restaurant]}.\nYou should travel by {transportation[random_transportation]}.\nYou should enjoy {entertainment[random_entertainment]}.\nDo you like these choices?\n(Y)es or (N)o')
        user_input = input()
        if user_input == 'Y' or user_input == 'y':
            print(
                f'Good choice! Your day trip to {places[random_place]} is going to be great!')
        elif user_input == 'N' or user_input == 'n':
            print('You should stay home.')
    # If the user does not like the mode of transportation, randomly select a new mode of transportation
    elif user_input == 'T' or user_input == 't':
        random_transportation = random.randint(0, number_of_transportation - 1)
        print(f'You should visit {places[random_place]}.\nYou should eat at {restaurants[random_restaurant]}.\nYou should travel by {transportation[random_transportation]}.\nYou should enjoy {entertainment[random_entertainment]}.\nDo you like these choices?\n(Y)es or (N)o')
        user_input = input()
        if user_input == 'Y' or user_input == 'y':
            print(
                f'Good choice! Your day trip to {places[random_place]} is going to be great!')
        elif user_input == 'N' or user_input == 'n':
            print('You should stay home.')
    # If the user does not like the form of entertainment, randomly select a new form of entertainment
    elif user_input == 'E' or user_input == 'e':
        random_entertainment = random.randint(0, number_of_entertainment - 1)
        print(f'You should visit {places[random_place]}.\nYou should eat at {restaurants[random_restaurant]}.\nYou should travel by {transportation[random_transportation]}.\nYou should enjoy {entertainment[random_entertainment]}.\nDo you like these choices?\n(Y)es or (N)o')
        user_input = input()
        if user_input == 'Y' or user_input == 'y':
            print(
                f'Good choice! Your day trip to {places[random_place]} is going to be great!')
        elif user_input == 'N' or user_input == 'n':
            print('You should stay home.')