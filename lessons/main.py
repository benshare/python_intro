import lesson1, lesson2
import os
from inspect import signature


lesson_map = {"lesson1": lesson1, "lesson2": lesson2}

def clear():
	os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
	line = input("What lesson number do you want to run? Type then hit return. ")
	while line:
		try:
			lesson_num = int(line)
			function_objs, function_names = lesson_map["lesson" + str(lesson_num)].getFunctions()
		except:
			line = input("Invalid input. Please type a lesson number then hit return. ")
		clear()
		fn_string = "Available functions to run:\n"
		for i in range(len(function_names)):
			fn_string += str(i) + ": " + function_names[i] + '\n'
		fn_string += "\nWhich function would you like to run? Type a number then hit return. Return on\
			an empty line to quit. "
		fn_line = input(fn_string)
		while fn_line:
			try:
				fn_num = int(fn_line)
				function_obj = function_objs[fn_num]
			except:
				fn_line = input("Invalid input. Please type a function number then hit return. ")
			clear()
			print("Running function %s" %function_names[fn_num])
			function_to_run = function_obj[0]
			param_types = function_obj[1]
			sig = signature(function_to_run)
			parameter_values = []
			i = 0
			for param in sig.parameters:
				param_value = input("\nWhat value should the parameter %s have? " %param)
				if param_types[i] == "Int":
					while param_value:
						try:
							param_int = int(param_value)
							parameter_values.append(param_int)
							break
						except:
							param_value = input("\t\tPlease type a valid integer for parameter %s. " %param)
				else:
					parameter_values.append(param_value)
				i += 1
			print("\n\nFunction output:")
			function_to_run(*parameter_values)
			print("\n\n")
			fn_line = input(fn_string)

		line = input("\nWhat lesson number do you want to run? Type then hit return. Return on an empty\
			 line to quit. ")

