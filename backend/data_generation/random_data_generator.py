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

with open('random_data.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write the data
    for i in range(num_rows):
        day = days[int(random.random() * len(days))]
        # picks a random cuisine from the list of options
        positive_cuisines = generate_positives()
        negative_cuisines = generate_negatives(positive_cuisines)

        positive1 = positive_cuisines[0]
        positive2 = ''
        positive3 = ''
        positive4 = ''
        positive5 = ''
        if len(positive_cuisines) > 1:
            positive2 = positive_cuisines[1]
        if len(positive_cuisines) > 2:
            positive3 = positive_cuisines[2]
        if len(positive_cuisines) > 3:
            positive4 = positive_cuisines[3]
        if len(positive_cuisines) > 4:
            positive5 = positive_cuisines[4]
        
        negative1 = negative_cuisines[0]
        negative2 = ''
        negative3 = ''
        negative4 = ''
        negative5 = ''
        if len(negative_cuisines) > 1:
            negative2 = negative_cuisines[1]
        if len(negative_cuisines) > 2:
            negative3 = negative_cuisines[2]
        if len(negative_cuisines) > 3:
            negative4 = negative_cuisines[3]
        if len(negative_cuisines) > 4:
            negative5 = negative_cuisines[4]


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
        if occasion == 'solo':
            num_people = 1
        elif occasion == 'date':
            num_people = 2
        else:
            num_people = int(random.random() * num_pot_people) + 1
            # prevents occasions that are work/family/friends related from having only 1 person
            while num_people == 1:
                num_people = int(random.random() * num_pot_people) + 1

        meal = meals[int(random.random() * len(meals))]
        
        price_range = price_ranges[int(random.random() * len(price_ranges))]
        
        row = [names.get_full_name(), day, positive1, positive2, positive3, positive4, positive5, negative1, negative2, negative3, negative4, negative5, restriction, occasion, num_people, meal, price_range, cuisine1, cuisine2, cuisine3]

        for j in range(scraped_column_ct):
            column_val = int(random.random() * 3) - 1
            row.append(column_val)
        # assigns that cuisine to the given row and writes it to the csv file
        writer.writerow(row)

