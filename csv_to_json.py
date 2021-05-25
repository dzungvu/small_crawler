import csv
import json

# csv_path = 'hot.csv'
# json_path = 'json\\hot.json'

csv_path = 'nexflix_anime.csv'
json_path = 'json\\netflix_anime.json'

data = []

with open(csv_path) as csv_file:
    csv_reader = csv.DictReader(csv_file)
    group_item_data = {}
    current_group = ''
    for rows in csv_reader:
        group_item = {}
        group_name = rows['group']
        if current_group != group_name:
            if (len(group_item_data) > 0):
                group_item['group_name'] = current_group
                group_item['items'] = group_item_data[current_group]
                data.append(group_item)

            group_item_data = {}
            current_group = group_name
        try:
            group_item_data[current_group]
        except KeyError:
            group_item_data[current_group] = []

        group_item_data[current_group].append(rows)


with open(json_path, "w") as json_file:
    json_file.write(json.dumps(data, indent=4))
    json_file.close()