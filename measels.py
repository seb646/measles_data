# Analytical Visualization Project - CCT111
# Sebastian Rodriguez & Saniya Hussain
import csv

print("This program compiles data about Measels immunization levels around the world.")
print("Data provided by the World Health Organization.\n")

# Prompt the user for the name of an output file
output_name = str(input("What do you want to name the output file (without extension)? "))
output_name += ".csv"

# Prompt the user to enter a year from 1980 to 2017 (or all)
year = False
while year == False:
    year_prompt = input("Please enter a year from 1980 to 2017 (or type \"all\"): ") 
    if str(year_prompt).lower() == "all":
        year = "all"
    elif int(year_prompt) >= 1980 and int(year_prompt) <= 2017:
        year = int(year_prompt)
    else:
        print("The year you entered is not valid. Please type \"all\" or a year between 1980 to 2017.")

# Prompt the user to enter an income level
# LI = low income (WB_LI)
# LMI = lower middle income (WB_LMI)
# UMI = upper middle income (WB_UMI) 
# HI = high income (WB_HI)
# ALL = show all
print("\nIncome level options: LI (Low Income), LMI (Lower Middle Income), UMI (Upper Middle Income), HI (High Income), all")
income_lvl = False
while income_lvl == False:
    income_prompt = str(input("Please enter an income level (ex: LMI): "))
    if income_prompt.upper() == "LI":
        income_lvl = "WB_LI"
    elif income_prompt.upper() == "LMI":
        income_lvl = "WB_LMI"
    elif income_prompt.upper() == "UMI":
        income_lvl = "WB_UMI"
    elif income_prompt.upper() == "HI":
        income_lvl = "WB_HI"
    elif income_prompt.upper() == "ALL":
        income_lvl = "ALL"
    else:
        print("You did not enter a valid income level. The options are: LI, LMI, UMI, HI, all.")

with open(output_name, 'w', newline='') as output_file:
    data_writer = csv.writer(output_file, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
    if year != "all":
        data_writer.writerow(['Country', 'World_Bank_Income_Level', f'{year}'])
        
    with open("measles.csv", "r") as input_file:
        csv_reader = csv.reader(input_file, delimiter=',')
        for row in csv_reader:
            if row[0] == "Country" and year == "all":
                data_writer.writerow(row)
                
            if row[0] == "Country" and year != "all":
                index = row.index(str(year))
            
            if row[0] != "Country" and row[1] == income_lvl and year == "all":
                data_writer.writerow(row)
            elif row[1] == income_lvl:
                data_writer.writerow([f'{row[0]}', f'{row[1]}', f'{row[index]}'])
            elif income_lvl == "ALL":
                data_writer.writerow(row)
                
# Collect Stats
with open(output_name, 'r') as file:
    record_count = 0
    stats = []
    
    csv_reader = csv.reader(file, delimiter=',')
    for row in csv_reader:
        if row[0] != "Country" and year != "all":
            record_count += 1
            stats.append(row[2])
        elif row[0] != "Country" and year == "all": 
            for item in row[2:39]:
                record_count += 1
                if item != "":
                    stats.append(int(item))

    highest_stat = max(stats)
    lowest_stat = min(stats)

with open(output_name, 'r') as file:
    csv_reader = csv.reader(file, delimiter=',')
    for row in csv_reader:
        if int(row[2]) == int(highest_stat):
            highest = row[0]
        if int(row[2]) == int(lowest_stat):
            lowest = row[0]
        if row[0] != "Country" and year == "all" and income_lvl == "ALL":
            for item in row[2:39]:
                if item != '':
                    if int(item) == int(highest_stat):
                        highest = row[0]
                    if int(item) ==  int(lowest_stat):
                        lowest = row[0]

# Outputs a message with the count of records in the input file that match the user’s criteria
print("\nThere are {} records that match your criteria.".format(record_count))

# Outputs a message with the average percentage for those records (displayed with one fractional digit)
stat_sum = 0
for stat in stats:
    stat_sum += int(stat)

avg = round((stat_sum/record_count), 1)
print("The average percent of children vaccinated is {}%.".format(avg))

# Outputs a message with the country with the lowest percentage for those records
print("The country with the lowest percent of childrent vaccinated is {}.".format(lowest))

# Outputs a message with the country with the highest percentage for those records
print("The country with the highest percent of childrent vaccinated is {}.".format(highest))

# Outputs a message with the name of the country and the percent of children vaccinated will be displayed for the last two items (lowest percentage and highest percentage).
print("The country with the lowest percent of childrent vaccinated is {} at {}%.".format(lowest, lowest_stat))
print("The country with the highest percent of childrent vaccinated is {} at {}%.".format(highest, highest_stat))