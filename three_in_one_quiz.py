animal = [
    ('\nQuestion 1: \n*********** \nA farmer had 15 cows. All but seven died. How many survived? \nAnswer: ', '7', 'seven'),
    ('Question 2: \n*********** \nThere are penguins in the arctic! True or False? \nAnswer: ', 'false'),
    ('Question 3: \n*********** \nWhich animal can not jump? \nA: All animals can jump! \nB: Cows \nC: Elephants \nD: Hedgehogs \nAnswer: ', 'c', 'elephants'),
    ('Question 4: \n*********** \nGiraffes have the world\'s longest neck, but how many vertebrae do they have? \n7, 9, 10 or 13? \nAnswer: ', '7', 'seven'),
    ('Question 5: \n*********** \nWhat two keys can not open any door? (Do only write down ONE!) \nAnswer: ', 'monkey', 'donkey'),
    ('Question 6: \n*********** \nWhat animal can jump higher than a building? \nA: Any \nB: A kangaroo \nC: No one \nD: A flea \nAnswer: ', 'a', 'kangaroo'),
    ('Question 7: \n*********** \nWhat happens when a female in a group of clownfish dies? \nA: Nothing \nB: The most dominant male turns into a female \nC: Everyone in the group dies \nAnswer: ', 'b', 'the most dominant male turns into a female'),
    ('Question 8: \n*********** \nKoalas sleep for 22 hours a day. True or False? \nAnswer: ', 'true')
]

math = [
    ('\nQuestion 1: \n*********** \nWhat is the sum of 111 + 222 + 333? \nAnswer: ', '666'),
    ('Question 2: \n*********** \nSubstract 457 from 832 \nAnswer: ', '375'),
    ('Question 3: \n*********** \n50 times 5 is equal to? \nAnswer: ', '250'),
    ('Question 4: \n*********** \nWhat is 90 / 10? \nAnswer: ', '9'),
    ('Question 5: \n*********** \nSimplify 26 + 32 - 12 \nAnswer: ', '46'),
    ('Question 6: \n*********** \nFind the product of 72 * 3 \nAnswer: ', '216'),
    ('Question 7: \n*********** \nSolve 200 -(96 / 4) \nAnswer: ', '176'),
    ('Question 8: \n*********** \nSolve 24 + 4 / 4 \nAnswer: ', '25'),
    ('Question 9: \n*********** \nSimplify 3 + 6 * (5 + 4) / 3 - 7 \nAnswer: ', '14'),
    ('Question 10: \n************ \nSimplify 150 / (6 + 3 * 8) - 5 \nAnswer: ', '0')
]

disney = [
    ('\nQuestion 1: \n*********** \nIn The Jungle Book who teaches Mowgli about The Bare Necesseties of life? \nAnswer: ', 'baloo'),
    ('Question 2: \n*********** \nWhat is the name of the boy who owns Buzz Lightyear in the movie Toy Story? \nAnswer: ',  'andy'),
    ('Question 3: \n*********** \nIn the movie Finding Nemo, which country has Nemo been taken to? \nAnswer: ',  'australia'),
    ('Question 4: \n*********** \nWhat does the crocodile swallow in Peter Pan? \nAnswer: ', 'a clock', 'clock'),
    ('Question 5: \n*********** \nIn Peter Pan, did Captain Hook have a hook for his left hand or his right hand? \nAnswer: His ', 'left hand'),
    ('Question 6: \n*********** \nWhich Disney movie features the song Two Worlds? \nAnswer: ',  'tarzan'),
    ('Question 7: \n*********** \nRandall Boggs is a villain in which Disney movie? \nAnswer: ', 'monsters inc'),
    ('Question 8: \n*********** \nWhich was the first Disney movie to receive an Oscar nomination for Best Picture? \nAnswer: ', 'beauty and the beast', 'the beauty and the beast'),
    ('Question 9: \n*********** \nWhat is the name of The Lion King? \nAnswer: ', 'simba'),
    ('Question 10: \n************ \nIn which city is the Disney movie Ratatouille based? \nAnswer: ', 'paris')
]
again = 'yes'
while again == 'yes':
    score = 0 

    questions = str.lower(input('\nWelcome! Which quiz do you want to take? \nA: Quiz about animals \nB: A math quiz \nC: A disney quiz \nAnswer: '))

    if questions == 'a':
        questions = animal
    elif questions == 'b':
        questions = math
    else:
        questions = disney

    for q in questions:
        answer = input(q[0]).lower()
        if answer in q[1:]:
            print('\nCorrect! \n')
            score += 1
        else:
            print('\nIncorrect \n')

    if score > len(questions)/2:
        print('Congratulations! \nYou got', str(score), 'out of', len(questions), 'It means that you got ', str(score / len(questions) * 100), '%', ' of all questions correct! \n')
    else:
        print('You got', str(score), 'out of', len(questions), 'answers correct.. ', '\nIt means that you only got ', str(score / len(questions) * 100), '%', 'of all questions correct.. \nI am sorry, better luck next time! \n')
    
    again = input('Do you want to try an another quiz? \nAnswer: ').lower()
    if again == 'no':
        print('Okay, good bye! \n')
        break