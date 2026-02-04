highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

# Separating the poems into individual lists
highlighted_poems_list = highlighted_poems.split(",")

# Removing unnecessary whitespace from each list
highlighted_poems_stripped = []
for poem in highlighted_poems_list:
  highlighted_poems_stripped.append(poem.strip(" "))

# Separating the poem details into individual lists
highlighted_poems_details = []
for poem in highlighted_poems_stripped:
  highlighted_poems_details.append(poem.split(":"))

# Grouping the details into lists
titles = []
poets = []
dates = []

for detail in highlighted_poems_details:
  titles.append(detail[0])
  poets.append(detail[1])
  dates.append(detail[2])

# Printing out final result
for index in range(len(highlighted_poems_details)):
  print("The poem {} was published by {} in {}.".format(titles[index], poets[index], dates[index]))
