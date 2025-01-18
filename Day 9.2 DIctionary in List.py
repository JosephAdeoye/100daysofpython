travels_log = [
    {
        "Country": "France",
        "visits": 12, 
        "cities_visited": ["Paris", "Lille", "Dijon"]
    },
    {
        "Country": "Germany",
        "visits": 5,
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"] 
    }
]

# TODO - Write the function that will allow new countries to be added to the travel_log.

def add_new_country(Country, visits, cities_visited):
    new_country = {
        "Country": Country,
        "visits": visits,
        "cities_visited": cities_visited
    }
    travels_log.append(new_country)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
add_new_country("South Africa", 1, ["Cape Town", "Durban"])
print(travels_log)

