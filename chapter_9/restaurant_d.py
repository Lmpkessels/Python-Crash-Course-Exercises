import restaurant.restaurant as restaurant

peking_garden = restaurant.Restaurant(name="peking garden", 
                                      location="stramproy", 
                                      adress="Frans Strouxstraat 32, 6039 " 
                                      "GK Stramproy",
                                      kitchen="chinese")

peking_garden.get_descriptive_restaurant()

print("\n")
peking_garden.open_restaurant()