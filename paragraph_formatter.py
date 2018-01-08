import sys
import json

def main():
    book = sys.argv[1]
    chapter = sys.argv[2]
    starting_verse = sys.argv[3]
    end_verse = sys.argv[4]

    print('You are looking for ' + book + ' ' +
    chapter + ':' + starting_verse + '-' + end_verse)

    data = json.load(open('NIV.json'))

main()
