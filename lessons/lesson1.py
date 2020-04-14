# This is lesson 1! Anything you see in this gray script is just the programmer leaving notes, called
# commenting. In Python, the language this file is written in, you can comment by starting the line
# with "#". Then when we run this file, the computer will ignore all the comments.
# Below, we're defining a bunch of "functions" to do specific tasks. A function is a piece of
# code that does a particular behavior. We then 'run' these functions by calling them in the "main"
# function at the bottom of this file.


# Example 1: write a function to print "hello world"
#
# New concepts:
# 	- 'def' is the special keyword that means we're making a new function. The name of this function
# 		is helloWorld.
#	- 'print' is a built-in function that prints things! You can pass it whatever you want and it
#		will print it out. In this case, we're passing it words--in python, this is called a String
#		(more on that below).
def helloWorld():
	print("Hello world")


# Example 2: print a given String n times
# Introducing the 'for' loop! Often, we want to do a certain task a bunch of times. Instead
# of having to write the same code over and over, we can write the code once, then put it in a
# 'loop'. The loop will say how many times to run the code inside.
#
# New concepts:
# 	- This function takes two 'parameters', "string" and "n". A parameter is something you have
# 		to tell the function when you run it, which changes exactly what it does. In this case, we're
#		writing a function that prints a particular String a particular number of times--but we want
# 		the user to be able to decide what to print, and how many times to print it.
#	- More explicitly, "string" and "n" are 'variables'. A variable is basically a name we use to keep
#		track of a value. We may not know what "n" is going to be equal to, but we can refer to
#		whatever value it ends up being using its name.
# 	- Variables have "types", which just says what type of values we're going to assign to them. In
#		this case, the idea is that "string" will have type String--which just means a sequence of
#		letters. Meanwhile, "n" will have type Int--short for integer, so just a whole number.
#	- For loop! "print(string)" prints our string once, so the for loop is responsible for making
#		that happen a certain number of times. In python, to do something x times, we can use
#		the line  "for i in range(x)". Don't worry about exactly how this works--we'll go into more
#		detail later. The important part is that whatever we put in the "range(__)" determines how
#		many times the thing inside will get run. So in this case, we want to put n in.
def printStringNTimes(string, n):
	for i in range(n):
		print(string)


# Example 3: print a given String n times, with each row numbered (with the first row as 1)
# Like before, we want to do something a bunch of times. This time though, we want to do something
# slightly different each time. This is where loops really come in handy. They let us define a variable
# to keep track of what 'iteration' through the loop we're on (aka how many times we've run the code
# inside), and we can use that number to change what the code inside does.
#
# New concepts:
# 	- Loop index. When we write "for i in range(n)", we're not exactly just saying we want to do the
#		code inside n times--we're saying we want to let the variable i take on each value from 
#		0 up to n (inclusive 0, exclusive n), and run the code once with each of those values. So
#		that's a total of n times. But in this case, we can use the value that i has to do something
#		different inside the loop.
#	- String concatenation. print() prints out a string. In this case, we want to print something like
#		1: Hello world
#		2: Hello world
#		3: Hello world
#		etc.
#		But each line is actually a few separate things glued together. First, we have the number (i).
#		Then we have the same connecting string each time: ": ". Then we have the ACTUAL string that
#		got passed in, e.g. "Hello world". The way we glue them all together is by using the "+"
#		operator.
#	- Two small things you might notice. We didn't actually write i--we wrote i + 1. That's cause, as
#		mentioned above, the loop makes i go from 0 to (n - 1), inclusive. If we want the first line
#		to start at 1, we should just add one to the value of i. Second, we put i + 1 in a call to the
#		function str. str just takes a number (an Int) like i + 1 and turns it into a String--for
#		example, from the value 4 to the character "4". The reason we have to do this is cause we're
#		using the symbol "+" to glue ("concatenate") the strings together--but "+" means something
#		different for ints (namely, adding their values). Writing str(i + 1) tells the computer we
#		want it to use the literal character version of the number, so there's no ambiguity.
def printStringNTimesNumbered(string, n):
	for i in range(n):
		print(str(i + 1) + ": " + string)


# Example 4: Print out the first n even numbers (starting with 2), each on its own line
# Similar to before, we want to use the iteration we're in to do something different each time. This
# time, we want to focus on the iteration as a number, and do a simple calculation with it. Like
# before, we'll add one to i to make it so that we start at 2 instead of 0.
#
# New concepts:
#	- * operator. We already saw '+' used to concatenate strings, and to add numbers (i.e. i + 1).
#		* is how you write "times" in Python.
def evenNumbers(n):
	for i in range(n):
		print((i + 1) * 2)


# Exercise 1: Print out the first n odd numbers (starting with 1), each on its own line
# Your code should be very similar to the previous function!
def oddNumbers(n):
	print("Not implemented yet")


# Example 5: Print out the first n powers of two
# In python, there's an operator for "to the power of"--it's "**". So this becomes pretty similar to
# Example 4.
# Note: "the first n powers of two" starts with 1, and goes up to 2^(n-1). So if n is 3, we should
# print 1, 2, and 4 (on separate lines).
def powersOfTwoV1(n):
	for i in range(n):
		print(2**i)


# Example 6: Print the first n powers of two--without using the ** operator
# Same task, but now we can't use the power operator! Can you think of how we could do this?
#
# New concepts:
#	- Setting a variable dependent on itself. It's perfectly legal for us to write
#		"previous_power = previous_power * 2"--the computer just calculates twice the current value,
#		then sets the variable equal to that. So that line is basically us saying
#		"double the value stored in previous_power".
#	
#		Because this is a common thing to want to do, there's actually a shorthand for this.
#		Instead of writing x = x * 2, we can write x *= 2. This is basically saying, we're multiplying
#		the value stored in x--and by how much? A factor of 2. We can put whatever number we want on
#		the right side--even another variable (i.e. x *= y). We can also do this for other operators
#		e.g. to increase the value of x by 5, we write "x = x + 5", OR "x += 5" as shortcut. Similarly,
#		"subtract 3 from x" is "x -= 3" and "halve x" is "x /= 2". One very common use of this is
#		when we "increment" a variable (increment meaning add one), by writing "x += 1". We'll see
#		why this is useful later.
#
#		Anyway, try rewriting the "previous_power = previous_power * 2" line using this notation.
def powersOfTwoV2(n):
	previous_power = 1
	for _ in range(n):
		print(previous_power)
		previous_power = previous_power * 2


# Exercise 2: Can you explain why lines 132 and 133 are in the order they're in? What would the
# function do if we swapped their order? Try to predict it, then swap them. Can you explain why it
# did that?


# Exercise 3: Print the first n powers of a, with b added to each one.
# This combines a couple things into one. It should look pretty similar to the powersOfTwo function
# (either version). For example, if we pass in (n = 4, a = 3, b = 5), it should print out, 6, 8, 14,
# and 32, each on its own line.
def printNPowersOfAPlusB(n, a, b):
	print("Not yet implemented")





# Don't worry about this function! This just allows the main script to run the code in here.
def getFunctions():
	functions = [(helloWorld, []),
		(printStringNTimes, ["String", "Int"]),
		(printStringNTimesNumbered, ["String", "Int"]),
		(evenNumbers, ["Int"]),
		(oddNumbers, ["Int"]),
		(powersOfTwoV1, ["Int"]),
		(powersOfTwoV2, ["Int"]),
		(printNPowersOfAPlusB, ["Int", "Int", "Int"])]
	function_names = ["helloWorld", "printStringNTimes", "printStringNTimesNumbered", "evenNumbers",\
		"oddNumbers", "powersOfTwoV1", "powersOfTwoV2", "printNPowersOfAPlusB"]
	return functions, function_names


