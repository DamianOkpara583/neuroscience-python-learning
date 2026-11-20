print ("Welcome to the Neuroscience Research Lab!")

participant_id = "P001"
age = 24
sleep_hours = 7
print ( participant_id)

print ("PARTICIPANT REPORT")
print ("Participant:", participant_id)
print ("Age:", age)
print ("Sleep hours:", sleep_hours)

awake_hours = 24 - sleep_hours
print ("Awake hours:", awake_hours)

if sleep_hours < 6:
    print ("participant has insufficent sleep")
else:
    print ("participant has adequate sleep")

participant = ["P001", "P002"]
sleep_data = [7, 5]

print (sleep_data)

average_sleep = sum(sleep_data) / len(sleep_data)
print (average_sleep)


participant = ["P001", "P002", "P003", "P004", "P005"]

sleep_data = [7, 5, 8, 4, 6]

average_sleep = sum(sleep_data) / len(sleep_data)
print ("Average sleep:", average_sleep)

print (max(sleep_data))

highest_sleep = max(sleep_data)
position = sleep_data.index(highest_sleep)
print (position)

print ("Best sleeper:", participant[position])

for i in range(len(sleep_data)):

    if sleep_data [i] < 6:
        print (participant[i], "has insufficient sleep")


insufficent_sleep = 0

for hours in sleep_data:
    if hours < 6:
        insufficent_sleep = insufficent_sleep + 1


print (insufficent_sleep)


import matplotlib.pyplot as plt
plt.bar(participant, sleep_data)

plt.title("Sleep Duration of Research Participants")
plt.xlabel ("Participants")
plt.ylabel ("Hours of Sleep")


plt.savefig("sleep_research_chart.png")
plt.show()



