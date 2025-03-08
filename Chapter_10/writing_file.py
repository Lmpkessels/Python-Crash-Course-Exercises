# We create a variable, wich we assign to a document we want to create.
first_last_name = ("/Users/luukkessels/Documents/Books - Python/Chapter_10/"
                   "first_and_last_name.txt")

# Here we open the document, we tell python with "w" we want to write, 
# then we assign it to first_and_last_name.
#
# Then we access first_and_last_name, we use .write("here message") to write 
# a message in the file.
#
# The "w" tells python we want to open the file in write mode.
with open(first_last_name, "w") as first_and_last_name:
    first_and_last_name.write("Luuk Kessels\n")
    first_and_last_name.write("\n")
    first_and_last_name.write("About me: \n\nI am born in a little farmers town, " 
                              "called stramproy on 23-02-2000. \nI am," 
                              " as you can count 25 years old.\n")
    

with open(first_last_name, "a") as f_and_l_name:
    f_and_l_name.write("Luuk Kessels his baptise names are; Martinus Petrus.\n")
    f_and_l_name.write("\n")
    f_and_l_name.write("So Luuk Kessels its full name is, Luuk Martinus Petrus" 
                       " Kessels.\n")
    