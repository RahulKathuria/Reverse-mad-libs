#!/usr/bin/python
# -*- coding: utf-8 -*-

# Question string for level 1

level_1 = \
    """
Narendra Damodardas __1__ , born 17 September 1950 is an Indian politician who is the
	 14 and current Prime Minister of __2__ , in office since May 2014. He was the Chief Minister of __3__
 	from 2001 to 2014, and is the Member of __4__ for Varanasi. Modi, a member of the Bharatiya Janata
 	__5__ (BJP),  is a Hindu nationalist and member of the right-wing Rashtriya Swayamsevak Sangh (RSS)."""

# Answer for level 1

level_1_answers = ['Modi', 'India', 'Gujarat', 'Parliament', 'Party']

# Question string for level 2

level_2 = \
    """Android is a mobile operating system developed by __1__ , based on the __2__ kernel and designed \
	primarily for touchscreen mobile devices such as smartphones and tablets. Android's user __3__ is
 	mainly based on direct manipulation, using __4__ gestures that loosely correspond to real-world actions,
 	such as swiping, tapping and pinching, to manipulate on-screen objects, along with a virtual __5__
 	or text input."""

# Answer for level 2

level_2_answers = ['Google', 'Linux', 'interface', 'touch', 'keyboard']

# Question string for level 3

level_3 = \
    """"Facebook is an American for-profit corporation and an online __1__ media
 and __1__ networking service based in Menlo Park, California. The Facebook website was launched
 on February 4, 2004, by __2__ Zuckerberg, along with fellow __3__ College students and roommates,
 Eduardo Saverin, Andrew McCollum, __4__ Moskovitz, and __5__ Hughes."""

# Answer for level 3

level_3_answers = ['social', 'Mark', 'Harvard', 'Dustin', 'Chris']

# question string for level 4

level_4 = \
    """Instagram is a mobile, desktop, and Internet-based __1__ -sharing application and service that
 allows users to share pictures and videos either publicly or __2__ . It was created by Kevin
 Systrom and Mike Krieger, and launched in October 2010 as a free __3__ app exclusively for the iOS
  operating __4__ . A version for Android devices was released two __5__ later, in April 2012."""

# answer for level 4

level_4_answers = ['photo', 'privately', 'mobile', 'system', 'years']


def playing_level():
    '''
....The function has no input parameter but asks the user for entering the level and then returns the
....respective level selected by the user.

....'''

    level = \
        raw_input('''Enter
easy for level 1
medium for level 2
hard for level 3
master for level 4
press quit anytime to exit!
''').lower()
    if level == 'easy':
        print str(level_1)
        start_game(level_1, level_1_answers)
    elif level == 'medium':
        print level_2
        start_game(level_2, level_2_answers)
    elif level == 'hard':
        print str(level_3)
        start_game(level_3, level_3_answers)
    elif level == 'master':
        print str(level_4)
        start_game(level_4, level_4_answers)
    elif level == 'quit':
        exit()
    else:
        print 'You entered a wrong choice!!, please enter a correct one\n'
        playing_level()


def start_game(ques_string, answer_list):
    '''
....This function takes two input parameter, one is the level string and the other is the answer list
....entered by the user, this function is called in the playing_level() function where the
....level entered by the user is passed in this function. The function returns nothing.
 ....'''

     # length_check variable is used to iterate the loop

    length_check = 0

        # count variable is used to count the number of wrong attempts given to the user.

    count = 5

        # update variable is initialized with the question string and later will be updated with the question string having blanks replaced by the answer

    update = ques_string

        # flag1 variable is used as a parameter inside the flag function

    flag1 = 1
    while length_check < len(answer_list):
        answer = raw_input('What should be the answer to blank __'
                           + str(length_check + 1) + '__ ?\n').lower()
        if is_correct(answer, answer_list[length_check]):
            update = update_ques_string(update, length_check, answer)
            length_check = length_check + 1
        else:
            count = count - 1
            print 'Wrong answer, Try again, ' + str(count) \
                + ' attempts remaining.'
            max_attempts = 1
            if count < max_attempts:
                flag1 = 0
                break
    flag(flag1)


def flag(input):
    '''
....Takes the flag1 variable as input parameter which would be either one or zero, and print
 ....the Winning and loosing message and returns nothing.
....'''

    default_flag = 0
    if input == default_flag:
        print 'Sorry, You lost!!'
    else:
        print 'All the answers were correct!!'


def is_correct(user_answer, correct_answer):
    '''
....This function takes the answer entered by the user and the correct answer from the answer list as
 ....its parameters and returns a boolean wether it istrue of not
....'''

    if user_answer == correct_answer:
        return True
    elif user_answer == 'quit':
        exit()
    else:
        return False


def update_ques_string(question, blank_index, user_answer):
    '''
....This function takes the question string, index of the blank and the answer entered by the user
....as its parameters,and return the updated question having blanks replaced by the correct answer
....'''

    question = question.split()

        # index is used to store the index of the first blank in the question

    index = question.index('__' + str(blank_index + 1) + '__')

        # blank string is replaced by the next line of code

    question[index] = question[index].replace('__' + str(blank_index
            + 1) + '__', user_answer)
    question = ' '.join(question)
    print question + '\n'
    print 'Correct answer'
    return question


playing_level()
