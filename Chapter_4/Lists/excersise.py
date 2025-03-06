#This is a list of great skills
great_skills = ["Programming", "Investing", "Persuasion", "Copywriting", "Design"]

#List gets sorted and reversed.
great_skills.sort(reverse = True)
print(great_skills)

#Item of the list gets taken out.
great_skills.pop(0)
#New item "Marketing" gets inserted,
great_skills.insert(0, "Marketing")
#Here the list gets sorted, then reversed.
great_skills.sort(reverse = True)
print(great_skills)

#Number of items/values get counted.
print(len(great_skills))