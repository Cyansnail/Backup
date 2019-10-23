# Isaac Lynn
# Period 4
taskc = 1 
todo = []
print("Welcome to your to-do list")

while True:
	enter = input("To add an item press a\nTo remove an item then press r\nTo show your list press p\nPress q to quit\nPress c to put your list in a document: ")
	if enter == "a":
		a = input("What would you like to add: ")
		todo.append(a)
	elif enter == "r":
		r = input("What would you like to remove: ")
		todo.pop(r)
	elif enter == "p":
		for task in todo:
			print("Task" + str(taskc) + ": " + task)
			taskc = taskc + 1
	elif enter == "q":
		break
	elif enter == "c":
		file = open("MyToDoList1","w")
		for task in todo:
			file.write("Task" + str(taskc) + ": " + task)
			taskc = taskc + 1
		file.close()
	else:
		print("I don't understand what you mean.")