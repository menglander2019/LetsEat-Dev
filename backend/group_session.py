from .db.db_management import retrievePositives, retrieveNegatives, retrieveRestrictions

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

    print("final positives list: " + str(positives))

    return positives

def generateGroupNegatives(hostID, groupIDs):
    # initially populates the list of negatives with the host's negativbes
    negatives = retrieveNegatives(hostID)

    # now goes through each members' negative preferences
    for groupID in groupIDs:
        memberNegatives = retrieveNegatives(groupID)
        print("member negatives: " + str(memberNegatives))
        for memberNegative in memberNegatives:
            # checks if the negative preference appears in the list and adds it if it isn't already present
            if memberNegative not in negatives:
                negatives.append(memberNegative)

    print("final group negatives: " + str(negatives))

    return negatives

def generateGroupRestrictions(hostID, groupIDs):
    # initially populates the list of restrictions with the host's restrictions
    restrictions = retrieveRestrictions(hostID)

    # now goes through each members' restrictions
    for groupID in groupIDs:
        memberRestrictions = retrieveRestrictions(groupID)
        print("member restrictions: " + str(memberRestrictions))
        for memberRestriction in memberRestrictions:
            # checks if the restriction is already present in the list of restrictions and adds it if it is not
            if memberRestriction not in restrictions:
                restrictions.append(memberRestriction)

    print("final group restrictions: " + str(restrictions))

    return restrictions
