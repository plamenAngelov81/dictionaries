countries = input().split(", ")
capitals = input().split(", ")

countries_capitals = dict(zip(countries, capitals))

for country in countries_capitals:
    print(f"{country} -> {countries_capitals[country]}")
