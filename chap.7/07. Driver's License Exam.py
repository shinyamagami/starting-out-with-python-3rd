# Chapter.7
# 07. Driver's License Exam

def correct_answers():
    correct_list = ['A', 'C', 'A', 'A', 'D', 'B', 'C', 'A', 'C', 'B',
                       'A', 'D', 'C', 'A', 'D', 'C', 'B', 'B', 'D', 'A']
    return correct_list
def open_answers():
    answers_list = []
    object_file = open('answers.txt', 'r')
    for i in object_file:
        i = i.rstrip('\n')
        answers_list.append(i)
    return answers_list
def check(correct_list, answers_list):
    count = 0
    print(correct_list)
    print(answers_list)
    wrong_answers = []
    for i in range(20):
        if correct_list[i] == answers_list[i]:
            count += 1
        else:
            wrong_answers.append(i)
            count += 0
    if count < 15:
        print('You failed')
    else:
        print('You passed')
    print('The number of correctly answerd question is', count)
    print('The number of incorrectly answerd question is', 20 - count)
    print('The question numbers of the incorrectly answered quesions are',
          wrong_answers)
def main():
    correct_list = correct_answers()
    answers_list = open_answers()
    check(correct_list, answers_list)
main()
