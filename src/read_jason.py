import json
with open("../data/dudes-data.json") as f:
    data = json.load(f)
print("---")
fat_fucks = data["fat-fucks"]

for name, weight_data_list in fat_fucks.items():
    print(f"The dude: {name}")
    total_weight = 0
    for weight_data in weight_data_list:
        total_weight += weight_data["weight"]
        weight = weight_data["weight"]
        print(f"Weight: {weight}")
    print(f"Total weight: {total_weight}")
    avg_weight = total_weight / len(weight_data_list)
    print(f"Average weight: {avg_weight}")

    print("---")
