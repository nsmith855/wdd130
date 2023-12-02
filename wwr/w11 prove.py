max_life_expectancy = float('-inf')
min_life_expectancy = float('inf')
total_life_expectancy = 0
count = 0
chosen_year = int(input("What year do you want to know about?: "))
highest_country = ""
lowest_country = ""

with open("life-expectancy.csv") as f:
    next(f)  # Skip the header

    for line in f:
        parts = line.split(",")
        country = parts[0]
        year = int(parts[2])
        life_expectancy = float(parts[3])

        if year == chosen_year:
            if life_expectancy > max_life_expectancy:
                max_life_expectancy = life_expectancy
                highest_country = country

            if life_expectancy < min_life_expectancy:
                min_life_expectancy = life_expectancy
                lowest_country = country

            total_life_expectancy += life_expectancy
            count += 1

# Calculate average life expectancy
avg_life = total_life_expectancy / count if count > 0 else 0

print(f"Overall highest life expectancy in {chosen_year} is in: {highest_country} with a life expectancy of: {max_life_expectancy}")
print(f"Overall lowest life expectancy in {chosen_year} is in: {lowest_country} with a life expectancy of: {min_life_expectancy}")
print(f"The average life expectancy of {chosen_year} is: {avg_life}")