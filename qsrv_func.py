#!/usr/bin/env python

# A simple script to parse a BSD fortune file format without the strfile(8) index.



def parse_fortunes(fortune_file):
    quote_list = []
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
    quote_list = []
    quote_path = 'fortunes'
    fortune_file = quote_path + '/quotes'
    parse_fortunes(fortune_file)
    print(quote_list)
