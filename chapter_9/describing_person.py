import person
import person_man

luuk = person_man.PersonMan(first_name="luuk", last_name="kessels", 
                               baptise_names="martinus petrus",)

johan = person.Person(first_name="johanus", last_name="kessels", 
               baptise_names="loduwikus")

luuk.get_fn_in_dictionary()

johan.get_full_name()
johan.get_fn_in_dictionary()