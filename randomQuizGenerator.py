#! python3
#randomQuizGenerator.py - creates quizzes with questions and answers in
#random order, algon with the answer key.

import random

capitals = { 'Ohio': 'Columbus', 'Texas': 'Austin', 'Georgia': 'Atlanta'}

for quizNum in range(5):
    #create the quiz and answer key files
    quizFile = open('capitalsquiz%s.txt' % (quizNum + 1), 'w')
    answerKeyFile = open('capitalsquiz_answers%s.txt' % (quizNum + 1), 'w')

    #Write out the header for the quiz.
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum+1))
    quizFile.write('\n\n')

    #shuffle the order of the states
    states = list(capitals.keys())
    random.shuffle(states)

    #loop through all the states, making a question for each
    for questionNum in range(3):
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 2)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

        #write the question and answer options to the quiz file.
        quizFile.write('%s. What is the capital of %s?\n' % (questionNum + 1,
            states[questionNum]))
        for i in range(3):
            quizFile.write('%s. %s\n' % ('ABC'[i], answerOptions[i]))
        quizFile.write('\n')
        #write the answer key to a file
        answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[
            answerOptions.index(correctAnswer)]))
    quizFile.close()
    answerKeyFile.close()
