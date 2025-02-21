def read_file(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def count_words(text):
    list_words = text.split()
    return len(list_words)

def count_occurences(text):
    occurences = {}
    for c in text:
        cl = c.lower()
        if cl in occurences:
            occurences[cl] += 1
        else:
            occurences[cl] = 1
    return occurences

def print_report(file, word_count, occurrences: dict):
    print(f'--- Begin report of {file[2:]} ---')
    print(f'{word_count} words found in the document')
    print()
    for k in occurrences.keys():
        if k.isalpha():
            print(f'The \'{k}\' character was found {occurrences[k]} times')
    print('--- End report ---')

if __name__ == "__main__":
    book_file = "./books/frankenstein.txt"
    file_string = read_file(book_file)
    word_count = count_words(file_string)
    occurrences = count_occurences(file_string)
    print_report(book_file, word_count, occurrences)