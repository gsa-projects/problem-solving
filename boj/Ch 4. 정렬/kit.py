from time import time
from random import shuffle

very_long_case = list(range(1, 10000))
shuffled_case = very_long_case.copy()
shuffle(shuffled_case)

def sort_test(sort_function):
	test_cases = [
		(list(range(1, 100)),
			list(range(1, 100))),
		([69, 10, 30, 2, 16, 8, 31, 22],
			[2, 8, 10, 16, 22, 30, 31, 69]),
		([7] * 50,
			[7] * 50),
		([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],
			[1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]),
		([],
			[]),
		([63, 25, 73, 1, 68, 20, 7, 58, 71, 61, 5, 16, 9, 26, 83, 31, 96, 78, 24, 56, 86, 27, 93, 37, 49, 54, 2, 57, 87, 88, 41, 48, 52, 55, 89, 38, 97, 60, 69, 64, 0, 21, 39, 73, 15, 6, 36, 90, 4, 72, 23, 46, 14, 17, 50, 76, 98, 81],
			[0, 1, 2, 4, 5, 6, 7, 9, 14, 15, 16, 17, 20, 21, 23, 24, 25, 26, 27, 31, 36, 37, 38, 39, 41, 46, 48, 49, 50, 52, 54, 55, 56, 57, 58, 60, 61, 63, 64, 68, 69, 71, 72, 73, 73, 76, 78, 81, 83, 86, 87, 88, 89, 90, 93, 96, 97, 98]),
		(shuffled_case,
			very_long_case)
	]
	
	for i, (input_case, output_case) in enumerate(test_cases):
		try:
			input_copied = input_case.copy()
			
			start_time = time()
			got_data = sort_function(input_copied)
			end_time = time()
			
			duration = end_time - start_time
			
			if got_data is None:
				got_data = input_copied
		except Exception as e:
			print(f"⛔ Test case #{i + 1}/{len(test_cases)} failed! ({duration:.5f} s)")
			print(f"Input    : {input_case}\nExpected : {output_case}\nGot      : {type(e).__name__} [ {e} ]")
			
			print(f"function '{sort_function.__name__}' has failed a test case!")
			
			return False
		
		if got_data != output_case:
			print(f"⛔ Test case #{i + 1}/{len(test_cases)} failed! ({duration:.5f} s)")
			print(f"Input    : {input_case}\nExpected : {output_case}\nGot      : {got_data}")
			
			print(f"function '{sort_function.__name__}' has failed a test case!")
			
			return False
		else:
			print(f"✅ Test case #{i + 1}/{len(test_cases)} passed! ({duration:.5f} s)")
	
	print(f"function '{sort_function.__name__}' has passed all test cases!")
	return True
