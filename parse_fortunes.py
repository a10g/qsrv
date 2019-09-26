#!/usr/bin/env python

quote_list = []
quote_path = 'fortunes'

def parse_fortunes(fortune_file):

    with open(fortune_file) as f:
        quote = ""
        for line in f:
            line = line.rstrip()
            if line != "%":
                quote = quote + line
            else:
                quote_list.append(quote)
                quote = ""
    return quote_list

if __name__ == "__main__":
    fortune_file = quote_path + '/quotes'
    parse_fortunes(fortune_file)
    print(quote_list)
