import csv  
import random
import names
from data_gen_constants import *

cuisine_groups_list = list(cuisine_groups)
restaurant_cuisines_list = list(cuisine_groups.values())

# generates a list of cuisines the user likes
def generate_positives():
    num_positives = int(random.random() * num_pot_positives) + 1
    positives = []
    i = 0
    while i < num_positives:
        cuisine = cuisine_groups_list[int(random.random() * (len(cuisine_groups_list)))]
        if cuisine not in positives:
            positives.append(cuisine)
            i += 1
    return positives

# generates a list of cuisines the user dislikes
def generate_negatives(positives):
    num_negatives = int(random.random() * num_pot_negatives) + 1
    negatives = []
    i = 0
    while i < num_negatives:
        cuisine = cuisine_groups_list[int(random.random() * (len(cuisine_groups_list)))]
        if cuisine not in positives:
            negatives.append(cuisine)
            i += 1
    return negatives

def generate_restriction():
    if random.random() < restriction_pct:
        return restrictions[int(random.random() * (len(restrictions)))]
    return -1

def generate_restaurant_cuisines():
    cuisines = []
    # generates a random number between 0 and 99 that will determine if the restaurant has 1, 2, or 3 cuisines associated with it
    num_cuisines = random.random() * 10
    if num_cuisines < 0.5:
        cuisines.append(cuisine_group[int(random.random() * len(cuisine_group))])
    # will generate two cuisines for a restaurant ~80% of the time
    elif num_cuisines < 9:
        cuisines.append(cuisine_group[int(random.random() * len(cuisine_group))])
        second_cuisine = cuisine_group[int(random.random() * len(cuisine_group))]
        # ensures that both cuisines are different
        while second_cuisine in cuisines:
            second_cuisine = cuisine_group[int(random.random() * len(cuisine_group))]
        cuisines.append(second_cuisine)
    # generates three cuisines ~5% of the time
    else:
        cuisines.append(cuisine_group[int(random.random() * len(cuisine_group))])
        second_cuisine = cuisine_group[int(random.random() * len(cuisine_group))]
        # ensures that both cuisines are different
        while second_cuisine in cuisines:
            second_cuisine = cuisine_group[int(random.random() * len(cuisine_group))]
        cuisines.append(second_cuisine)
        third_cuisine = cuisine_group[int(random.random() * len(cuisine_group))]
        # ensures that the third cuisine is different
        while third_cuisine in cuisines:
            third_cuisine = cuisine_group[int(random.random() * len(cuisine_group))]
        cuisines.append(third_cuisine)

    return cuisines

with open('./backend/data_generation/random_data.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write the data
    for i in range(num_rows):
        day = days[int(random.random() * len(days))]
        # picks a random cuisine from the list of options
        positive_cuisines = generate_positives()
        negative_cuisines = generate_negatives(positive_cuisines)

        restriction = generate_restriction()

        occasion = occasions[int(random.random() * len(occasions))]
        if restriction == -1:
            restriction = ''
        cuisine_group = restaurant_cuisines_list[int(random.random() * len(restaurant_cuisines_list))]

        # generates the cuisines for the random restaurant
        cuisines = generate_restaurant_cuisines()
        cuisine1 = cuisines[0]
        cuisine2 = ''
        cuisine3 = ''
        if len(cuisines) == 3:
            cuisine2 = cuisines[1]
            cuisine3 = cuisines[2]
        elif len(cuisines) == 2:
            cuisine2 = cuisines[1]
       
        # sets the occasion and number of people properly
        if occasion == 'Myself':
            num_people = 1
        elif occasion == 'Date':
            num_people = 2
        else:
            num_people = int(random.random() * num_pot_people) + 1
            # prevents occasions that are work/family/friends related from having only 1 person
            while num_people == 1:
                num_people = int(random.random() * num_pot_people) + 1

        meal = meals[int(random.random() * len(meals))]
        

        # gives a restauraunt a random umbrella cuisine
        rest_cuisines = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        rest_cuisines[int(random.random() * len(rest_cuisines))] = 1

        # gives the restaurant a single price range
        rest_price_ranges = [0, 0, 0, 0]
        rest_price_ranges[int(random.random() * 4)] = 1


        
        row = [
            names.get_full_name(), day, int(random.random() * 3) - 1, int(random.random() * 3) - 1, int(random.random() * 3) - 1, int(random.random() * 3) - 1,
            int(random.random() * 3) - 1, int(random.random() * 3) - 1, int(random.random() * 3) - 1, int(random.random() * 3) - 1, int(random.random() * 3) - 1, 
            int(random.random() * 3) - 1, int(random.random() * 3) - 1, int(random.random() * 3) - 1, int(random.random() * 3) - 1, int(random.random() * 3) - 1, 
            int(random.random() * 3) - 1, int(random.random() * 3) - 1, int(random.random() * 2), int(random.random() * 2), int(random.random() * 2), int(random.random() * 2), int(random.random() * 2), int(random.random() * 2), int(random.random() * 2), int(random.random() * 2), int(random.random() * 2), int(random.random() * 2), occasion, num_people, meal, int(random.random() * 2), int(random.random() * 2), 
            int(random.random() * 2), int(random.random() * 2), round(random.random() * 5, 1), rest_cuisines[0], rest_cuisines[1], rest_cuisines[2], rest_cuisines[3], rest_cuisines[4], rest_cuisines[5], 
            rest_cuisines[6], rest_cuisines[7], rest_cuisines[8], rest_cuisines[9], rest_cuisines[10], rest_cuisines[11], rest_cuisines[12], rest_cuisines[13], 
            rest_cuisines[14], rest_cuisines[15], int(random.random() * 2), int(random.random() * 2), rest_price_ranges[0], rest_price_ranges[1], rest_price_ranges[2], 
            rest_price_ranges[3], int(random.random() * 2), int(random.random() * 2), int(random.random() * 2),
        ]

        for j in range(scraped_column_ct):
            column_val = int(random.random() * 3) - 1
            row.append(column_val)
        # assigns that cuisine to the given row and writes it to the csv file
        writer.writerow(row)

