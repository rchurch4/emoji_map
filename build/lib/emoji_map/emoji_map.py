import os
import re

emojis = dict()

with open(os.path.join(os.path.dirname(__file__), 'emoji.csv'), 'r') as f:
    for l in f:
        l = l.strip().split(',')
        emojis[l[0]] = l[1]

def emoji_map(string):
    if string[0] == '\\':
        string = string[1:]
    return emojis[string.upper()]

def replace_emojis(string):
    emoji_regex = re.compile('U[a-fA-F0-9]{8}', re.UNICODE)
    string = repr(string)
    emojis = re.findall(emoji_regex, string)
    for emoji in emojis:
        try:
            desc = emoji_map(emoji)
        except:
            desc = emoji
        string = string.replace(emoji, desc)

    # for parsing multi-part emojis, like skin-tone hands and families. imperfect but gives you what you need to know
    complicated_emoji_regex = re.compile('u[a-fA-F0-9]{3,8}', re.UNICODE)
    complicated_emojis = re.findall(complicated_emoji_regex, string)
    for i in range(0, len(complicated_emojis)):
        possible_emoji = complicated_emojis[i]
        try:
            desc = emoji_map(fill_unicode(possible_emoji))
            string = string.replace(possible_emoji, desc)
        except:
            for j in range(i+1, len(complicated_emojis)):
                possible_emoji += ' ' + complicated_emojis[j]
                try:
                    desc = emoji_map(possible_emoji)
                    string = string.replace(complicated_emojis[i], desc)
                    for k in range(i, j + 1):
                        string = string.replace(complicated_emojis[k], ' ')
                    i = j + 1
                    break
                except:
                    pass

    string = string.replace('\\', ' ')
    return string

if __name__ == "__main__":
    print emoji_map('\U0001F30E')
