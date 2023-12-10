# Reading File Data
classRosterFile = open("ClassRoster.csv", "r")
availabilityFile = open("Availability.csv", "r")
outputFile = open("SplitRoster.csv", "w")

classRosterData = classRosterFile.read()
availabilityData = availabilityFile.read()

# Spliting names into Data
stepOneClassRoster = classRosterData.split('\n')
stepOneAvailability = availabilityData.split('\n')

classRosterDictionary = {}
classesWithAvailablity = {}
splitRoster = {}

students = list()
availableSpots = list()
periods = []
rooms = []

# This loop makes lists with periods and students in each period
# [Period X, Period Y]
# [Student in Period X, Student in Period Y]
for i in stepOneClassRoster:
    students.append(i.split(','))

# Makes a list of all classrooms
for i in stepOneAvailability:
    availableSpots.append(i.split(','))

# This adds a list to each period. The list will contain all the students in that period.
# The periods list contains however many periods there are.
for i in range(len(students[0])):
    classRosterDictionary[students[0][i]] = list()
    periods.append(students[0][i])

# This loop adds a list to each classroom. The list will soon contain other lists containing how many students will be
# placed in that classroom depending on what period it is.
for i in range(len(availableSpots[0])):
    classesWithAvailablity[availableSpots[0][i]] = list()
    splitRoster[availableSpots[0][i]] = list()
    rooms.append(availableSpots[0][i])

students.pop(0)
availableSpots.pop(0)

# This nested loop adds the students to the correct periods.
for i in students:
    for j in range(len(i)):
        classRosterDictionary[periods[j]].append(i[j])

# This nested loop determines how many available spots a classroom has for each period.
for i in availableSpots:
    for j in range(len(i)):
        if (len(i[j])) == 0:
            continue
        classesWithAvailablity[rooms[j]].append(i[j])

# If there are 7 periods, 7 lists will be nested inside of the classroom list.
for i in splitRoster:
    for j in range(len(classesWithAvailablity[i])):
        splitRoster[i].append(list())

# This loop divides students into the other classrooms depending on how many spots they have available.
for i in classesWithAvailablity: # class name
    for j in range(len(classesWithAvailablity[i])): # references periods
        for k in range(int(classesWithAvailablity[i][j])):
            if len(classRosterDictionary[periods[j]]) > 0:
                splitRoster[i][j].append(classRosterDictionary[periods[j]][0])
                classRosterDictionary[periods[j]].pop(0)

# This loop writes the classroom names as headers in the output file.
outputFile.write(', ')
for key in splitRoster.keys():
    outputFile.write(key + ', ')

outputFile.write('\n')

# Iterate through classes with availability

periodNumber = 0
tempString = ''
for periodName in classRosterDictionary:
    outputFile.write(periodName + ',')
    for i in splitRoster:
        for j in range(len(splitRoster[i][periodNumber])):
            outputFile.write(splitRoster[i][periodNumber][j] + '; ')

        outputFile.write(',')

    periodNumber += 1
    outputFile.write('\n')