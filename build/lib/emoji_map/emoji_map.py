import os

emojis = dict()

with open(os.path.join(os.path.dirname(__file__), 'emoji.csv'), 'r') as f:
    for l in f:
        l = l.strip().split(',')
        emojis[l[0]] = l[1]

def emoji_map(string):
    if string[0] == '\\':
        string = string[1:]
    return emojis[string.upper()]

if __name__ == "__main__":
    print emoji_map('\U0001F30E')
