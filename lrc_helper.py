import re

''' Cut lyrics file into sentences with necessary information

    Example
    path = "data/example.txt"
    song = extract_sentences(path)

    song: list of sentence [sentence]
    sentence: dictionary 'start_time' & 'duration' & 'words'
    words: list of word [word]
    word: dictionary 'start_time' & 'time_duration' & 'word'
'''


def extract_sentence(path):
    lrc_file = open(path, 'r')
    lines = re.findall(r"\[\d*?,\d*?\].*", lrc_file.read())

    song = []

    i = 0
    for line in lines:
        sentence = {}
        # print line
        time_signature = re.findall(r"\[(\d*),(\d*)\]", line)
        start_time = float(time_signature[0][0])
        duration = float(time_signature[0][1])
        sentence['start_time'] = float(start_time)
        sentence['duration'] = float(duration)

        merge_flag = False

        if i > 0:
            # print i
            last_sentence = song[i-1]
            if start_time == last_sentence['start_time'] + last_sentence['duration']:
                # print i
                merge_flag = True

        if merge_flag:
            # modify current sentence's word time
            last_sentence_words = last_sentence['words']
            word_new_start_time = last_sentence_words[-1]['start_time'] + last_sentence_words[-1]['time_duration']
            last_sentence['duration'] += duration

            word_signatures = re.findall(r"\<(\d*),(\d*),\d\>(.)", line)
            for word_signature in word_signatures:
                word = {}
                word['start_time'] = float(word_new_start_time) + float(word_signature[0])
                word['time_duration'] = float(word_signature[1])
                word['word'] = word_signature[2]
                last_sentence_words.append(word)

        else:
            sentence['words'] = []

            word_signatures = re.findall(r"\<(\d*),(\d*),\d\>(.)", line)
            for word_signature in word_signatures:
                word = {}
                word['start_time'] = float(word_signature[0])
                word['time_duration'] = float(word_signature[1])
                word['word'] = word_signature[2]
                sentence['words'].append(word)

            song.append(sentence)
            i += 1

    return song


def get_sequence(path):
    lrc_sentences = extract_sentence(path)

    lrc_sequence = []

    for i, sentence in enumerate(lrc_sentences):
        sentence_start_time = sentence['start_time']
        sentence_duration = sentence['duration']

        duration = 0
        for word in sentence['words']:
            to_begin_time = sentence_start_time + word['start_time']
            word_tuple = {}
            word_tuple['start_time_to_begin'] = to_begin_time
            word_tuple['duration'] = word['time_duration']
            word_tuple['word'] = word['word']
            word_tuple['isSpace'] = False
            lrc_sequence.append(word_tuple)
            duration += word['time_duration']

        space_tuple = {}
        space_tuple['isSpace'] = True
        if i + 1 == len(lrc_sentences):
            space_tuple['start_time_to_begin'] = sentence_start_time + duration
            space_tuple['duration'] = sentence_duration - duration

        else:
            space_tuple['start_time_to_begin'] = sentence_start_time + sentence_duration
            space_tuple['duration'] = lrc_sentences[i+1]['start_time'] - space_tuple['start_time_to_begin']
        lrc_sequence.append(space_tuple)

    return lrc_sequence