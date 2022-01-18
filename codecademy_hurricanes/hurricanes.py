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

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}

def update_damages(damages):
  updated_damages = []
  for index in range(len(damages)):
    if damages[index] == 'Damages not recorded':
      updated_damages.append(damages[index])
    else:
      updated_damages.append(float(damages[index][:-1]) * conversion[damages[index][-1]])
  return updated_damages

# test function by updating damages
damages_updated = update_damages(damages)
#rint(damages_updated)

# 2
# Create a Table

# Create and view the hurricanes dictionary
def make_table(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
  hurricanes = {}
  for index in range(len(names)):
    hurricanes[names[index]] = {'Name': names[index], 'Month': months[index], 'Year': years[index], 'Max Sustained Wind': max_sustained_winds[index], 'Areas Affected': areas_affected[index], 'Damage': damages[index], 'Deaths': deaths[index]}
  return hurricanes

hurricanes = make_table(names, months, years, max_sustained_winds, areas_affected, damages_updated, deaths)
#print(hurricanes)

# 3
# Organizing by Year

# create a new dictionary of hurricanes with year and key
def by_year(hurricanes):
  hurricanes_by_year = {}
  for hurricane in hurricanes.values():
    if hurricane['Year'] in hurricanes_by_year:
      hurricanes_by_year[hurricane['Year']].append(hurricane)
    else:
      hurricanes_by_year[hurricane['Year']] = [hurricane]
  return hurricanes_by_year

hurricanes_by_year = by_year(hurricanes)
# print(hurricanes_by_year[1932])
# 4
# Counting Damaged Areas

# create dictionary of areas to store the number of hurricanes involved in

def area_counts(hurricanes):
  times_affected = {}
  for hurricane in hurricanes.values():
    for area in hurricane['Areas Affected']:
      if area in times_affected:
        times_affected[area] += 1
      else:
        times_affected[area] = 1
  return times_affected

times_affected = area_counts(hurricanes)
#print(times_affected)

# 5
# Calculating Maximum Hurricane Count

# find most frequently affected area and the number of hurricanes involved in
def most_hit(times_affected):
  top_area = {'Place': '', 'Times Hit': 0}
  for area, times_hit in times_affected.items():
    if times_hit > top_area['Times Hit']:
      top_area['Place'] = area
      top_area['Times Hit'] = times_hit
  return top_area

most_affected = most_hit(times_affected)
#print(most_affected)
# 6
# Calculating the Deadliest Hurricane

# find highest mortality hurricane and the number of deaths

def most_deadly(hurricanes):
  deadliest = {'Name': 'Gary', 'Deaths': 0}
  for hurricane in hurricanes.values():
    if hurricane['Deaths'] > deadliest['Deaths']:
      deadliest['Name'] = hurricane['Name']
      deadliest['Deaths'] = hurricane['Deaths']
  return deadliest

most_deaths = most_deadly(hurricanes)
#print(most_deaths)

# 7
# Rating Hurricanes by Mortality

mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}

def mortality_scale(deaths):
  if deaths == 0: return 0
  elif deaths < 100: return 1
  elif deaths < 500: return 2
  elif deaths < 1000: return 3
  elif deaths < 10000: return 4
  else: return 5

def by_mortality_scale(hurricanes):
  by_mortality = {}
  for hurricane in hurricanes.values():
    scale = mortality_scale(hurricane['Deaths'])
    if scale in by_mortality:
      by_mortality[scale].append(hurricane)
    else:
      by_mortality[scale] = [hurricane]
  return by_mortality

# categorize hurricanes in new dictionary with mortality severity as key

by_mortality = by_mortality_scale(hurricanes)
#print(by_mortality)

# 8 Calculating Hurricane Maximum Damage

# find highest damage inducing hurricane and its total cost
def most_damage(hurricanes):
  top_damage = {'Name': 'Gary', 'Damage': 0.0}
  for hurricane in hurricanes.values():
    if hurricane['Damage'] != 'Damages not recorded' and (hurricane['Damage'] > top_damage['Damage']):
      top_damage['Name'] = hurricane['Name']
      top_damage['Damage'] = hurricane['Damage']
  return top_damage

top_damage = most_damage(hurricanes)
#print(top_damage)

# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}

def damage_scale(damage):
  if damage == 'Damages not recorded': return damage
  elif damage == 0: return 0
  elif damage < 100000000: return 1
  elif damage < 1000000000: return 2
  elif damage < 10000000000: return 3
  elif damage < 50000000000: return 4
  else: return 5

def by_damage(hurricanes):
  hurricanes_by_damage = {}
  for hurricane in hurricanes.values():
    scale = damage_scale(hurricane['Damage'])
    if scale in hurricanes_by_damage:
      hurricanes_by_damage[scale].append(hurricane)
    else:
      hurricanes_by_damage[scale] = [hurricane]
  return hurricanes_by_damage
# categorize hurricanes in new dictionary with damage severity as key

hurricanes_by_damage = by_damage(hurricanes)
print(hurricanes_by_damage)
