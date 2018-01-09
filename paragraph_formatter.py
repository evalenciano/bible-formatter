import sys
import json

def main():
    book = sys.argv[1]
    chapter = sys.argv[2]
    initial_verse = sys.argv[3]
    end_verse = sys.argv[4]

    print('You are looking for ' + book + ' ' +
    chapter + ':' + initial_verse + '-' + end_verse)

    data = json.load(open('NIV.json'))

    verse_count = int(initial_verse)
    while (verse_count <= int(end_verse)):
        string_verse = data[book][chapter][str(verse_count)]
        print(string_verse)
        verse_count = verse_count + 1

main()
