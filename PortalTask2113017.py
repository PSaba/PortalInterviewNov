
def check_same(checking):
    #checks if 2 events clash
    listClash = []
    for date in checking:
        #checks every date
        for i in range(len(checking[date])):
            for j in range(i, len(checking[date])):
                #first starts before start and ends after start
                #first starts before end and ends after end
                if checking[date][i][1] < checking[date][j][1] and checking[date][i][2] > checking[date][j][1]:
                    listClash.append(checking[date][i][0])
                    listClash.append(checking[date][j][0])
                elif checking[date][j][1] < checking[date][i][1] and checking[date][j][2] > checking[date][i][1]:
                    listClash.append(checking[date][i][0])
                    listClash.append(checking[date][j][0])
                elif checking[date][i][1] < checking[date][j][2] and checking[date][i][2] > checking[date][j][2]:
                    listClash.append(checking[date][i][0])
                    listClash.append(checking[date][j][0])
                elif checking[date][j][1] < checking[date][i][2] and checking[date][j][2] > checking[date][i][2]:
                    listClash.append(checking[date][i][0])
                    listClash.append(checking[date][j][0])
                elif checking[date][j][1] == checking[date][i][2] and checking[date][j][2] == checking[date][i][2]:
                    if checking[date][j][0] != checking[date][i][0]:
                        listClash.append(checking[date][i][0])
                        listClash.append(checking[date][j][0])                        
    return listClash;
    


#initial events
dictEvents = dict({})
dictEvents["02232017"] = [["Interview at The Portal", 15.0, 16.5]]
dictEvents["02242017"] = [["Dinner with John", 17.0, 17.5], ["Conference", 11, 17.5]]
dictEvents["02252017"] = [["Lunch with Cindy", 12.0, 13.0]]

#more events added
dictEvents["02262017"] = [["Lunch with Harry", 11.0, 13.0]]
dictEvents["02262017"].append(["Lunch with Zoe", 12.0, 14.0])
dictEvents["02232017"].append(["Magic Mountain", 18.0, 16.0])
dictEvents["02232018"] = [["Magic Mountain Pt.2", 18.0, 16.0]]

print(check_same(dictEvents))

#I chose dictionary with key as date, since events can only clash if they occur on the same day
# value is array with name, start time, and end time as they need to be kept in certain order
#that way same day items are together
#I went through each date, going through all the events in the date and comparing the times
#if any of the start and end times clashed, that is, one events doesn't end before the start of the other event or starts in the middle of the event, then add to list
#if both events checked is the same event, not added
#if more time, would have sorted according to starting time and checked if ending time is before other event's starting time
