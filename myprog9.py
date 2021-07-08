def input_value(string_to_print):
	name = input(string_to_print)
	return name

def grade_maths(a, b, c):
	ict_score = ((a + b +c) / 175 * 100)
	return ict_score

student_name = input_value("What is your name? ")
homework_score = int(input_value("What is your homework score? "))
assessment_score = int(input_value("What is your assessment score? "))
final_score = int(input_value("What is your final exam score? "))

final_output = grade_maths = ((homework_score + assessment_score + final_score) / 175 * 100)

overall_score = f"({student_name}, {final_output})"

print(overall_score)