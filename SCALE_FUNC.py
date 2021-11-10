#! python3
# SCALE_FUNC.py - contains 2 tuples with the musical notes and scale degrees and a scale making function.
# These will be used for creating the scales in the functionvand will also serve as the basis for the
# questions in the main file.

notes = ('E', 'F', 'F#/Gb', 'G', 'G#/Ab', 'A', 'A#/Bb',
         'B', 'C', 'C#/Db', 'D', 'D#/Eb')
degrees = ('Tonic', 'Supertonic', 'Mediant', 'Subdominant',
           'Dominant', 'Submediant', 'Leading Tone')


# Function that accepts a string value of musical note to form the basis of the scale and a string value
# of the type, be it major or minor, and returns a dictionary with the degree names as keys and musical
# notes as values; i.e. 'Tonic' : 'A'.
def scale_maker(key, type_of_scale='Major'):
    # the steps used to create either a major or minor scale from the musical alphabet.
    major = (0, 2, 4, 5, 7, 9, 11)
    minor = (0, 2, 3, 5, 7, 8, 10)

    scale_notes = []
    # if the chosen note is a sharp or flat, the function will change the index accordingly. Either way,
    # the musical notes will be ordered so that the chosen note is the first item in a new 'new_notes' list,
    #  allowing easier construction of the chosen scale.
    if len(key) > 1:
        # as the enharmonic notes in the 'notes' tuple above are paired together, i.e. 'F#/Gb', it makes finding
        # the index of say F# difficult. So we isolate just the letter part of the passed key (F for example) and
        # adjust the index by 1. + for sharp and - for a flat.
        if key[1] == '#':
            sharp_key = key[0]
            index = notes.index(sharp_key.upper()) + 1
            new_notes = notes[index:] + notes[:index]
        elif key[1] == 'b':
            flat_key = key[0]
            index = notes.index(flat_key.upper()) - 1
            new_notes = notes[index:] + notes[:index]
    else:
        new_notes = notes[notes.index(key.upper()):] + notes[:notes.index(key.upper())]

    # the steps to construct the correct scale are determined whether it is major or minor.
    if type_of_scale.lower() == 'major':
        for step in major:
            # choose correct enharmonic equivalent for answer if needed.
            if len(new_notes[step]) > 1:
                answer_choices = new_notes[step].split('/')
                if len(key) > 1 and key[1] == '#':
                    scale_notes.append(answer_choices[0])
                elif len(key) > 1 and key[1] == 'b':
                    scale_notes.append(answer_choices[1])
                # F major has the exception of having a Bb.
                elif key == 'F':
                    scale_notes.append(answer_choices[1])
                else:
                    scale_notes.append(answer_choices[0])
            else:
                scale_notes.append(new_notes[step])
        # a dictionary of the scale degrees and corresponding notes is returned.
        return dict(zip(degrees, scale_notes))

    elif type_of_scale.lower() == 'minor':
        for step in minor:
            if len(new_notes[step]) > 1:
                answer_choices = new_notes[step].split('/')
                if len(key) > 1 and key[1] == '#':
                    scale_notes.append(answer_choices[0])
                elif len(key) > 1 and key[1] == 'b':
                    scale_notes.append(answer_choices[1])
                # E and B minor have the exceptions of having sharp notes.
                elif key == 'E' or key == 'B':
                    scale_notes.append(answer_choices[0])
                else:
                    scale_notes.append(answer_choices[1])
            else:
                scale_notes.append(new_notes[step])
        return dict(zip(degrees, scale_notes))
