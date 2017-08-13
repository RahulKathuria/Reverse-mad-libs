#!/usr/bin/python
# -*- coding: utf-8 -*-
level_1 = \
    """
Narendra Damodardas __1__ , born 17 September 1950 is an Indian politician who is the 
	 14 and current Prime Minister of __2__ , in office since May 2014. He was the Chief Minister of __3__
 	from 2001 to 2014, and is the Member of __4__ for Varanasi. Modi, a member of the Bharatiya Janata
 	__5__ (BJP),  is a Hindu nationalist and member of the right-wing Rashtriya Swayamsevak Sangh (RSS)."""

level_1_answers = ['Modi', 'India', 'Gujarat', 'Parliament', 'Party']

level_2 = \
    """Android is a mobile operating system developed by __1__ , based on the __2__ kernel and designed \
	primarily for touchscreen mobile devices such as smartphones and tablets. Android's user __3__ is 
 	mainly based on direct manipulation, using __4__ gestures that loosely correspond to real-world actions, 
 	such as swiping, tapping and pinching, to manipulate on-screen objects, along with a virtual __5__ 
 	or text input."""

level_2_answers = ['Google', 'Linux', 'interface', 'touch', 'keyboard']

level_3 = \
    """"Facebook is an American for-profit corporation and an online __1__ media
 and __1__ networking service based in Menlo Park, California. The Facebook website was launched 
 on February 4, 2004, by __2__ Zuckerberg, along with fellow __3__ College students and roommates,
 Eduardo Saverin, Andrew McCollum, __4__ Moskovitz, and __5__ Hughes."""

level_3_answers = ['social', 'Mark', 'Harvard', 'Dustin', 'Chris']

level_4 = \
    """Instagram is a mobile, desktop, and Internet-based __1__ -sharing application and service that 
 allows users to share pictures and videos either publicly or __2__ . It was created by Kevin 
 Systrom and Mike Krieger, and launched in October 2010 as a free __3__ app exclusively for the iOS
  operating __4__ . A version for Android devices was released two __5__ later, in April 2012."""

level_4_answers = ['photo', 'privately', 'mobile', 'system', 'years']


def playing_level():
    level = \
        raw_input('''Enter
1 for level 1
2 for level 2
3 for level 3
4 for level 4
''')
    if level == '1':
        print str(level_1)
        start_game(level_1, level_1_answers)
    elif level == '2':
        print level_2
        start_game(level_2, level_2_answers)
    elif level == '3':
        print str(level_3)
        start_game(level_3, level_3_answers)
    elif level == '4':
        print str(level_4)
        start_game(level_4, level_4_answers)


def start_game(ques_string, answer_list):
    i = 0
    count = 5
    flag = 1
    update = ques_string
    while i < len(answer_list):
        answer = raw_input('What should be the answer to blank __'
       						 + str(i + 1) + '__ ?')

        if is_correct(answer, answer_list[i], update, i):
        	i = i + 1
        else:
            print 'Wrong answer, Try again, ' + str(count - 1) \
                + ' attempts remaining.'
            count = count - 1
            if count < 1:
                flag = 0
                break
    if flag == 1:
        print 'All the answers were correct!!'
    else:
        print 'Sorry, You lost!!'


def is_correct(
    user_answer,
    correct_answer,
    question,
    blank_index,
    ):
    if user_answer == correct_answer:
        question = question.split()
        index = question.index('__' + str(blank_index + 1) + '__')
        question[index] = question[index].replace('__'
                + str(blank_index + 1) + '__', user_answer)
        question = ' '.join(question)
        print question + '\n'
        print 'Correct answer'
        return (True, question)
    else:
        return False


playing_level()


