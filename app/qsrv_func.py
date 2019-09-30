#!/usr/bin/env python

# A simple script to parse a BSD fortune file format without the strfile(8) index.

from os import listdir
from os.path import isfile, join


def get_fortunes(fortune_path):
    available_fortunes = get_fortune_list(fortune_path)
    all_fortunes = {}
    for fortune_file in available_fortunes:
        path_to_fortunes = fortune_path + "/" + fortune_file
        fortunes = parse_fortunes(path_to_fortunes)
        all_fortunes.update({fortune_file:fortunes})
    return all_fortunes

def get_fortune_list(fortune_path):
    fortune_list = [f for f in listdir(fortune_path) if isfile(join(fortune_path, f))]
    return fortune_list

def parse_fortunes(fortune_file):
    fortunes = []
    with open(fortune_file) as fi:
        fortune = ""
        for line in fi:
            if line.rstrip() != "%":
                fortune = fortune + line
            else:
                fortunes.append(fortune)
                fortune = ""
    return fortunes



if __name__ == "__main__":
    import random
    fortune_path = 'fortunes'
    all_fortunes = get_fortunes(fortune_path)
    #fortune = random.choice(all_fortunes[fortune_file])
    db = random.choice(list(all_fortunes.keys()))
    fortune = random.choice(all_fortunes[db])
    print("Random fortune")
    print("Database: " + db)
    print("Fortune: " + fortune)
