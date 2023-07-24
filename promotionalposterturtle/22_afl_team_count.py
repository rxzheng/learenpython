list = dict({"Brisbane Lions" : "Queensland", "Gold Coast Suns" : "Queensland", "Sydney Swans" : "Sydney", "Greater Western Sydney Giants" : "Sydney", "Adelaide Crows" : "South Australia", "Port Adelaide Power" : "South Austalia", "West Coast Eagles" : "Western Australia", "Fremantle Dockers" : "Western Austalia"})
count = 0
print(list)
for i in list:
    if "Sydney" in str(i):
        count += 1
print("There are " + str(count) + " teams in the AFL that are not based in Victoria")

