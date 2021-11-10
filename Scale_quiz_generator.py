#! python3
# Scale_quiz_generator.py - A quiz generator for guitar students to help them improve their
# musical knowledge and grasp of scales. Inspired by Al Sweigart's 'Automate the boring stuff'.

# import scale maker module from separate file to access musical notes, scale degree names
# and scale making function.
import SCALE_FUNC as SF

import random

# create the desired number of quiz files and their corresponding answer files.
for quiz_number in range(#NUMBEROFQUIZZES):
    quiz_file = open(f'ScaleQuiz{quiz_number+1}.txt', 'w')
    quiz_file.write((' ' * 20) + f'Scale Quiz (Form {quiz_number+1})\n\n')
    quiz_file.write('Write the corresponding musical note from the key and degree given.\n\n')

    answer_file = open(f'ScaleAnswers{quiz_number+1}.txt', 'w')
    answer_file.write(f'Answers {quiz_number+1}\n\n')

    # theoretical keys and keys containing non-standard notes (i.e. Fb/Cb) are avoided for simplicity.
    excluded_keys = ('F# Major', 'C# Major', 'G# Major', 'D# Major', 'A# Major', 'Gb Major',
                     'Eb Minor', 'Db Minor', 'Gb Minor', 'Ab Minor', 'A# Minor', 'D# Minor')

    # there will be 5 keys chosen and 3 questions for each.
    chosen_keys = []
    while len(chosen_keys) < 5:
        # random choice from the muscial notes contained in the auxiliary file.
        chosen_note = random.choice(SF.notes)
        # decide between enharmonic equivalents, i.e. F#/Gb.
        if len(chosen_note) > 1: # if note is not simply A or B but Bb/A# it's length will be > 1.
            options = chosen_note.split('/') # split the two notes into 'options' list.
            chosen_note = options[random.randint(0, 1)]
        # determine whether the key will be major or minor.
        majormin = random.randint(0, 1)
        if majormin == 0:
            majormin = 'Major'
        else:
            majormin = 'Minor'
        # put the final chosen key together.
        key_name = f'{chosen_note} {majormin}'
        # check if the key is in excluded_keys tuple.
        if key_name in excluded_keys:
            pass
        # avoid duplicates by passing if key already in chosen group.
        elif key_name in chosen_keys:
            pass
        else:
            chosen_keys.append(key_name)

    # iterate through each key in chosen group and create section for each.
    for current_key in chosen_keys:
        quiz_file.write(f'. {current_key}\n\n')
        answer_file.write(f'. {current_key}\n\n')
        # split the key name into 'key' and 'type' to pass to scale_maker() function in auxiliary file.
        parts_key = current_key.split()
        # use scale function to create dictionary of chosen key.
        scale_dict = SF.scale_maker(parts_key[0], parts_key[1])
        # randomly select 3 scale degrees.
        question_degrees = random.sample(scale_dict.keys(), 3)
        # iterate through each degree and write to question file and corresponding answer to answer file.
        for degree in question_degrees:
            quiz_file.write(f'  . {degree} =\n')
            answer_file.write(f'  . {scale_dict[degree]}\n')

        # add a newline to separate each different musical key section.
        quiz_file.write('\n')
        answer_file.write('\n')

    quiz_file.close()
    answer_file.close()
