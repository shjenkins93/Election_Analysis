counties = ["Arapahoe","Denver","Jefferson"]
counties [0]
print(counties[2])
print(counties[-1])
len(counties)
counties[1:]


counties

counties
counties.pop(3)

counties
counties = ["Arapahoe","Denver","Jefferson"]
counties.append("El Paso")
counties_tuple = ("Arapahoe","Denver","Jefferson")
len(counties_tuple)
counties_tuple[1:2]
counties_dict = {}
counties_dict["Arapahoe"] = 422829
counties_dict
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
counties_dict
len(counties_dict)
counties_dict.items()
counties_dict.values()
voting_data = []
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
voting_data
counties_a

for county in counties:
    print(county)
counties_tuple = ("Arapahoe","Denver","Jefferson")
counties
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in counties_dict.keys():
    print(county)

 for voters in counties_dict.values():
    print(voters)

for county in counties_dict:
    print(counties_dict.get(county))

for key, value in dictionary_name.items():
    print(key, value)
for county, voters in counties_dict.items():
    print(county, voters)

    voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

for county_dict in voting_data:
    print(county_dict['county'])

counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")

for county, voters in counties_dict.items():
print(f"{county} county has {voters} registered voters.")

candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
f"You received {candidate_votes} number of votes. "
f"The total number of votes in the election was {total_votes}. "
f"You received {candidate_votes / total_votes * 100}% of the total votes.")

print(message_to_candidate)