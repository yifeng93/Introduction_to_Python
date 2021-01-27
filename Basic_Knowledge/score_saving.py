# _*_ coding: utf-8 _*_

"""

1. Save 3 courses scores for 6 students.
2. Calculate student's average score and course's average score.

Oringinal author: 骆昊
Enhanced detail editor: Yifeng

"""


names = ['A', 'B', 'C', 'D', 'E', 'F']
courses = ['math', 'English', 'statistics']


scores = [[0] * len(courses) for _ in range(len(names))]
# Here we create a nesting list to save scores.
# scores = [[0,0,0], [0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]


print(scores)
# When we finish creating list, we need to input scores.
# check `enumerate` in advance.
for i, name in enumerate(names):
	print(f'please input {name} score ===>')
	for j, course in enumerate(courses):
		# use print to check what happen with 'enumerate'
		scores[i][j] = float(input(f'{course}: '))
		
# calculate score info and display
print('-' * 5, 'Student Average Score', '-' * 5)

for index, name in enumerate(names):
	# strongly advice you to print(score[index]). scores[0] is actually the first 'little list'.
	avg_score = sum(scores[index]) / len(courses)
	print(f'{name} average score is: {avg_score:.1f}')

print('-' * 5, 'Course Average Score', '-' * 5)
for index, course in enumerate(courses):
	curr_course_scores = [score[index] for score in scores]
	avg_score = sum(curr_course_scores)/len(names)
	print(f'{course} average score is: {avg_score:.1f}')



