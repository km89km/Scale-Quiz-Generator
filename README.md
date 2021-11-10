A program that creates the desired number of Musical scale quizzes and a corresponding answer file. Although useful for any musician, having been
a guitar teacher, I know that music theory can be a weak point for guitarists so simple quizzes like this can be helpful, particularly for anyone
that aspires to complete grades. It is by no means comprehensive and for the sake of simplicity I have included a tuple of 'excluded keys'. Without 
going into to much detail, there are particular musical keys that are called 'theoretical keys', that would have at least one double-flat or double-sharp,
creating issues for the program and a much simpler equivalent exists. Therefore, the equivalent is included and the other not.

Each section focuses on a randomly chosen musical key, with 5 keys chosen in total, and 3 randomly selected musical degrees form the basis of the questions.

The desired number of quizzes is put into a for loop and then a quiz file and an answer file are created with the appropriate name and headings. 5 keys are
then randomly chosen using random.choice() from a tuple of the musical notes contained in the auxiliary file, SCALE_FUNC.py. We first determine if it will be
a sharp or flat key if an enharmonic pair (i.e. F#/Gb) is chosen and then if it will be major or minor. When we have created the final key, we check to see if it is
in the 'excluded_keys' tuple, and if not it is appended to the 'chosen_keys' list. When we have 5 keys that are not duplicates then it is time to start writing
to the created quiz and answer files.

The program will then loop through the 'chosen_keys' list and each one will be passed to the scale_maker() function from the auxiliary file. This function
accepts a string value of the musical note and the type of key (Major/Minor). After the necessary checks are done the function returns a dictionary that is the result of
zipping the degrees of a musical scale with their corresponding musical values, determined by which scale was passed to the function. 3 questions are then created
for each chosen key and these questions and their corresponding answers are then written to the relevant files.

