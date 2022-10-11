import csv  
import random
import names
from data_gen_constants import *

cuisine_list = cuisines.split('\n')

# generates a list of cuisines the user likes
def generate_positives():
    num_positives = int(random.random() * num_pot_positives) + 1
    positives = []
    i = 0
    while i < num_positives:
        cuisine = cuisine_list[int(random.random() * (len(cuisine_list)))]
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
        cuisine = cuisine_list[int(random.random() * (len(cuisine_list)))]
        if cuisine not in positives:
            negatives.append(cuisine)
            i += 1
    return negatives

def generate_restriction():
    if random.random() < restriction_pct:
        return restrictions[int(random.random() * (len(restrictions)))]
    return -1

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
        restriction = generate_restriction()
        occasion = occasions[int(random.random() * len(occasions))]
        if restriction == -1:
            restriction = ''
        cuisine = cuisine_list[int(random.random() * (len(cuisine_list)))]
        num_people = int(random.random() * num_pot_people) + 1
        meal = meals[int(random.random() * len(meals))]
        price_range = price_ranges[int(random.random() * len(price_ranges))]
        
        row = [names.get_full_name(), day, positive_cuisines, negative_cuisines, restriction, occasion, num_people, meal, price_range, cuisine]

        for j in range(scraped_column_ct):
            column_val = int(random.random() * 3) - 1
            row.append(column_val)
        # assigns that cuisine to the given row and writes it to the csv file
        writer.writerow(row)

