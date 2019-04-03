from collections import Counter
import re


def build_dictionary_of_frequencies(text_file: str):
    key_words = (open("python-developer/skills.txt", "r").read().lower().split('\n'))[0:12]
    search_strings = [r'(?=(\b%s\b))' % re.escape(s.strip()) for s in key_words]
    searcher = re.compile('|'.join(search_strings)).findall
    file = open(text_file, "r", encoding="utf-8-sig").read()
    answer = Counter()
    found = []
    for tuples in searcher(file):
        for words in tuples:
            if words != '':
                found.append(words)
    for word in key_words:
        answer[word] = 0
        for words in found:
            if words in word:
                answer[word] += 1
    return answer


with open("Task Results.txt", "w") as task:
    answer_dict = {}
    for i in range(1, 100):
        try:
            answer_dict["answer{}".format(i)] = build_dictionary_of_frequencies('job description {}.txt'.format(i))
            print('In job description {}:'.format(i), file=task)
            for answers in answer_dict['answer{}'.format(i)]:
                print('{} shows up {} times.'.format(answers, answer_dict['answer{}'.format(i)][answers]), file=task)
        except FileNotFoundError:
            break
    task.close()
