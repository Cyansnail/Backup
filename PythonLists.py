# how to make a list
favMovies = ["Star Wars", "Avengers", "LOTR"]
# prints the whole list
print(favMovies)
#prints only one of the items
print(favMovies[1])
# to add you can append or insert
# append adds to the end
favMovies.append("Iron Man 1")
print(favMovies)
# insert will put the item wherevre you want
favMovies.insert(1, "Harry Potter")
print(favMovies)
# how to remove items 
# remove by name or by index
# remove by name use remove
favMovies.remove("LOTR")
print(favMovies)
#favMovies.remove("Kill Bill")
# pop will remove the last item, unless index is given
favMovies.pop()
print(favMovies)
favMovies.pop(1) # will remove whatever is in index 1
print(favMovies)

# get the length of a list
# this is a function
# the function name is len
print("My list has " + str(len(favMovies)) + " items.")
favMovie = input("What is your favorite movie? ")
favMovies.append(favMovie)
print(favMovies)
print(favMovies[len(favMovies)-1])

#loop through a list
count = 1

for movie in favMovies:
	print("My number " + str(count) + " movie is " + movie )
	count = count + 1

numList = [1, 3, 5, 7, 9, 11, 13, 15]
# challenge: Loop through the list and add all of the numbers together
total = 0
for totall in numList:
	total = total + totall
print(total)

if "Harry Potter" in favMovies:
	favMovies.remove("Endgame")
else:
	print("Not in list")