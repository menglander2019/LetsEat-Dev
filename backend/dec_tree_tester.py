def test_dec_tree():
    features = []
    day = input("What's the current day? ")
    positives = input("What cuisines do you prefer? ")
    negatives = input("What cuisines do you dislike? ")
    restrictions = input("Any dietary restrictions? ")
    occasion = input("What is the occasion?")
    if occasion == "solo":
        num_people = 1
    elif occasion == "date":
        num_people = 2
    else:
        num_people = int(input("How many people will be going? "))
    meal = input("What meal will it be for? ")
    price_range = input("What is your price range? ")

    return [day, positives, negatives, restrictions, occasion, num_people, meal, price_range]


