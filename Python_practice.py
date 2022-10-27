counties = ["Arapahoe","Denver","Jefferson"]
counties [0]
print(counties[2])
print(counties[-1])
len(counties)
counties[1:]
counties.append("El Paso")
counties.insert(2, "El Paso")
counties
counties.remove("El Paso")
counties
counties.pop(3)
counties[2] = "El Paso"
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
voting_data.append({"county":"El Paso", "registered_voters": 461149})
