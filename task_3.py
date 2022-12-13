import pandas as pd

hike_data = pd.read_csv('../data/hike_long.csv')
clean_hike_trails = hike_data

clean_hike_trails[['gain', 'highpoint', 'rating']] = clean_hike_trails[['gain', 'highpoint', 'rating']] \
    .apply(pd.to_numeric)

def getTripVal(length):
    if length.find('roundtrip') != -1:
        return 'roundtrip'
    elif length.find('trails') != -1:
        return 'trails'
    elif length.find('one-way') != -1:
        return 'one-way'
    else:
        return None

clean_hike_trails['trip'] = clean_hike_trails['length'].apply(getTripVal)
clean_hike_trails['length_total'] = pd.to_numeric(clean_hike_trails['length'].str.split(' ').str[0])
clean_hike_trails['length_total'] = clean_hike_trails.apply(lambda x: x['length_total'] * 2 
    if x['trip'] == 'one-way' 
    else x['length_total'], axis=1)
    
clean_hike_trails["location_general"] = clean_hike_trails["location"].str.split(" -- ").str[0]

clean_hike_trails["row_id"] = clean_hike_trails.index


print('1. How many routes have rating more than 4.9')
print(len(clean_hike_trails[clean_hike_trails['rating'] > 4.9]))

print('2. How many routes are “Good for kids” (hint: you can use (unnest function)?')
print(len(clean_hike_trails[clean_hike_trails["features"].str.contains("Good for kids")]))

print('3. Which unique features can routes have?')
print(clean_hike_trails.drop_duplicates("features")["features"].tolist())

print('4. What is the most common rating of a route?')
print(clean_hike_trails["rating"].value_counts().head(1))

print("5. Your own question and answer: how many routes have 'Mount Rainier Area' location?")
print(len(clean_hike_trails[clean_hike_trails["location_general"] == 'Mount Rainier Area']))
