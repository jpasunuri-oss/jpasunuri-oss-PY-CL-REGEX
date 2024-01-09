from lab import regExFunctions, regExExerciseOne, regExExerciseTwo, regExExerciseThree

if __name__ == "__main__":
    print('regExFunctions')
    regExFunctions()

    words_replace = "Alice has 3 apples, Bob has 5 oranges, and Charlie has 2 bananas. David has 8 grapes, and Emily has 4 peaches."    
    print('regExExerciseOne: ', regExExerciseOne(words_replace))

    numbers_replace_letters = "There are 3 apples, 4 bananas and 10 straberries"
    print('regExExerciseTwo: ', regExExerciseTwo(numbers_replace_letters))

    while True:
        print("Enter test email address for exercise 3")
        email = input()
        print('regExExerciseThree: ', regExExerciseThree(email))
