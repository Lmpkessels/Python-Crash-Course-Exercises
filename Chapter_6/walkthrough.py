# Simple dictionary
alien_0 = {"color": "green", "points": 5}
print(alien_0["color"])
print(alien_0["points"])

# Telling the user how much points he has earned for shooting down the 
# alien
#
# Using two different forms I can code it for reputation
new_points = alien_0["points"]
earned_points = f"You have earned {str(new_points)} points!" 
earned_points = "You have earned " + str(new_points) + " points!"
print(earned_points)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)