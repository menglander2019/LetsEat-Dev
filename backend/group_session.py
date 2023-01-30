from .db.db_management import retrievePositives, retrieveNegatives

def generateGroupPreferences(hostID, groupIDs):
    # initializes the list of positive cuisine preferences with the host's preferences
    positives = retrievePositives(hostID)
    print("host positives: "+ str(positives))

    # iterates through every guest in the host's session and adds their preferences to the final list
    for groupID in groupIDs:
        memberPositives = retrievePositives(groupID)
        for memberPositive in memberPositives:
            # makes sure that the preference is not already in the list so that repeats are avoided
            if memberPositives not in positives:
                positives.append(memberPositive)

    # now that all the positive preferences are consolidated, the negatives of each user need to be considered
    print("prebuilt positives list: " + str(positives))

    # goes through the list of negative preferences the host has and removes any appearances of those negatives
    hostNegatives = retrieveNegatives(hostID)
    print("host negatives: " + str(hostNegatives))
    for hostNegative in hostNegatives:
        if hostNegative in positives:
            print("from the host, removing: " + str(hostNegative))
            positives.remove(hostNegative)

    # now goes through each members' negative preferences
    for groupID in groupIDs:
        memberNegatives = retrieveNegatives(groupID)
        print("member negatives: " + str(memberNegatives))
        for memberNegative in memberNegatives:
            # checks if the negative preference appears in the list and removes it
            if memberNegative in positives:
                print("removing from a member: " + str(memberNegative))
                positives.remove(memberNegative)

    return positives

    
