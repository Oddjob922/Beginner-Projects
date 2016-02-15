# Mad Libs Story Maker
# Python 3.5.1
# Written by alfredmuffin

print("Please enter: ")
name = input("A name: ")
pronoun = input("A third-person pronoun for your name: ")
pronoun2 = input("Possessive pronoun: ")
noun1 = input("A noun: ")
noun2 = input("A second noun: ")
noun3 = input("A third noun: ")
noun4 = input("A fourth noun: ")
ad1 = input("An adjective: ")
ad2 = input("A second adjective: ")
ad3 = input("A third adjective: ")
ad4 = input("A fourth adjective: ")
ad5 = input("A fifth adjective: ")


l1 = "Today {0} decided that {1} was going to take {2} {3} to the {4}. ".format(name, pronoun, pronoun2, noun1, noun2)

l2 = "{0} thought that {1} was finally ready to let the {2} {3} be {4}. ".format(name, pronoun, ad1, noun1, ad2)

l3 = "You see, the {0} had caused {1} much {2} over the last few {3}. ".format(noun1, name, ad3, noun3)

l4 = "When {0} arrived at the {1}, {2} decided that {2} {3} another {4} for his {5} instead. ".format(name, noun2, pronoun, ad4, noun4, noun1)

l5 = "So {0} went back home, and to {1} {2}, the {3} was still with {4}.".format(name, pronoun2, ad5, noun1, pronoun)

story = l1 + l2 + l3 + l4 + l5
print("\n" + story)
