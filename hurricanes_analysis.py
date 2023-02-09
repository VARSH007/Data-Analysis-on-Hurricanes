# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 1
# Update Recorded Damages
def update_damages_list(damages):
    conversion = {"M": 1000000,"B": 1000000000}
    updated_damages = list()
    for damage in damages:
        if damage == "Damages not recorded":
            updated_damages.append(damage)
        if damage.find('M') > 0:
            updated_damages.append(float(damage[0:damage.find('M')]) * conversion["M"])
        if damage.find('B') > 0:
            updated_damages.append(float(damage[0:damage.find('B')]) * conversion["B"])
    return updated_damages
updated_damages = update_damages_list(damages)
#print(updated_damages)
# 2
# Create a Table
def joining_records_by_hurricane_names(names,months, years,max_sustained_winds,areas_affected,damages, deaths):
    hurricanes = dict()
    total_length = len(names)
    for data in range(total_length):
        hurricanes[names[data]] = {"Name":names[data],"Months":months[data],"years":years[data],
                                   "Max_sustained_winds":max_sustained_winds[data],
                                   "Areas_Affected":areas_affected[data],"Damage":damages[data],"Deaths":deaths[data]}
    return hurricanes
hurricanes_dict = joining_records_by_hurricane_names(names, months, years, max_sustained_winds, areas_affected, damages, deaths)
#print(hurricanes_dict)

# 3
# Organizing by Year
def records_by_year(hurricanes_dict):
    hurricanes_dict_by_year = {}
    for data in hurricanes_dict:
        current_year = hurricanes_dict[data]['years']
        current_data = hurricanes_dict[data]
        if current_year not in hurricanes_dict_by_year:
            hurricanes_dict_by_year[current_year] = [current_data]
        else:
            hurricanes_dict_by_year[current_year].append(current_data)
    return hurricanes_dict_by_year
# create a new dictionary of hurricanes with year and key
hurricanes_dict_by_year = records_by_year(hurricanes_dict)
print(hurricanes_dict_by_year)


# 4
# Counting Damaged Areas
def damaged_areas_count(hurricanes_dict):
    most_affected_areas = dict()
    for data in hurricanes_dict:
        for count in hurricanes_dict[data]['Areas_Affected']:
            if count not in most_affected_areas:
                most_affected_areas[count] = 1
            else:
                most_affected_areas[count] += 1
    return most_affected_areas
# create dictionary of areas to store the number of hurricanes involved in
most_affected_areas = damaged_areas_count(hurricanes_dict)


# 5 
# Calculating Maximum Hurricane Count
def hurricane_count(most_affected_areas):
    max_area = ''
    max_area_count = 0
    for xdata in most_affected_areas:
        if most_affected_areas[xdata] > max_area_count:
            max_area =  xdata
            max_area_count = most_affected_areas[xdata]
    return max_area,max_area_count

maximum_hurricane_count = hurricane_count(most_affected_areas)



# 6
# Calculating the Deadliest Hurricane
def dead_list_hurricane(hurricanes_dict):
    max_name = ''
    max_deaths = 0
    for data in hurricanes_dict:
        if hurricanes_dict[data]['Deaths'] > max_deaths:
            max_name = data
            max_deaths = hurricanes_dict[data]['Deaths']
    return  max_name,max_deaths
deadliest_hurricane = dead_list_hurricane(hurricanes_dict)


# 7
# Rating Hurricanes by Mortality
def categorize_by_mortality(hurricanes_dict):
    mortality_scale = {0: 0, 1: 100, 2: 500, 3: 1000, 4: 10000}
    hurricanes_categorize = {0:[],1:[],2:[],3:[],4:[],5:[]}
    for data in hurricanes_dict:
        num_deaths = hurricanes_dict[data]['Deaths']
        if num_deaths == mortality_scale[0]:
            hurricanes_categorize[0].append(hurricanes_dict[data])
        elif num_deaths > mortality_scale[0] and num_deaths <= mortality_scale[1]:
            hurricanes_categorize[1].append(hurricanes_dict[data])
        elif num_deaths > mortality_scale[1] and num_deaths <= mortality_scale[2]:
            hurricanes_categorize[2].append(hurricanes_dict[data])
        elif num_deaths > mortality_scale[2] and num_deaths <= mortality_scale[3]:
            hurricanes_categorize[3].append(hurricanes_dict[data])
        elif num_deaths > mortality_scale[3] and num_deaths <= mortality_scale[4]:
            hurricanes_categorize[4].append(hurricanes_dict[data])
        elif num_deaths > mortality_scale[4]:
            hurricanes_categorize[5].append(hurricanes_dict[data])
    return hurricanes_categorize
# categorize hurricanes in new dictionary with mortality severity as key

hurricanes_mortality = categorize_by_mortality(hurricanes_dict)


#8
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}

