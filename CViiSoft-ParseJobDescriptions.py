from collections import Counter
import re

with open("python-developer/skills.txt", "r") as skills:
    key_words = (skills.read().lower().split('\n'))[0:12]


def special_words_catcher(special_char: str, text_file: str):
    searcher = re.compile(special_char).search
    counts = 0
    file = open(text_file, "r", encoding="utf-8-sig")
    for line in file:
        if searcher(line):
            counts += 1
    return counts


def build_dictionary_of_frequencies(text_file: str):
    subject_matter_expert = special_words_catcher(key_words[0], text_file)
    j_sox = special_words_catcher(key_words[9], text_file)
    answer = Counter()
    words = re.findall('\w+', open(text_file, "r", encoding="utf-8-sig").read())
    for word in words:
        if word in key_words:
            answer[word] += 1
            if subject_matter_expert > 0:
                answer[key_words[0]] = subject_matter_expert
            if j_sox > 0:
                answer[key_words[9]] = j_sox
    for words in key_words:
        if words not in answer:
            answer[words] = 0
    return answer


with open("Task Results.txt", "w") as task:
    answer1 = build_dictionary_of_frequencies('job description 1.txt')
    answer2 = build_dictionary_of_frequencies('job description 2.txt')
    print('In the first job description for the Financial Controller:', file=task)
    for answers in answer1:
        print('{} shows up {} times.'.format(answers, answer1[answers]), file=task)
    print('\nIn the second job description for the Financial Accountant', file=task)
    for answers in answer2:
        print('{} shows up {} times'.format(answers, answer2[answers]), file=task)
    task.close()
