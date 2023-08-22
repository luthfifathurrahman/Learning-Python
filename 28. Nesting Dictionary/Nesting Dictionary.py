# Nesting a list in a dictionary
travel_log = {
    "Indonesia" : {"cities_visited" : ["Semarang", "Bandung"], "total_visit" : 12},
    "UK" : {"cities_visited" : ["London", "Manchester"], "total_visit" : 5}
}

# nesting dictionary in a list
travel_log1 = [
    {
        "country": "Indonesia",
        "cities_visited": ["Semarang", "Bandung"],
        "total_visit": 12
    },
    {
        "country": "UK",
        "cities_visited": ["London", "Manchester"],
        "total_visit": 5
    },
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
          "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    }
]

def add_new_country(country, visits, cities):
    travel_log1.append(
        {
            "country": country,
            "visits": visits,
            "cities": cities
        }
    )

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log1)
