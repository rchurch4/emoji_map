
# emoji_map

This is a small python package to help you easily understand what emojis you are looking at.  If you are scraping web data like tweets, messages, etc. you will be returned the unicode encoding of all emojis that you receive.  This package enables a quick lookup of a unicode emoji, and returns the official keywords.

========================

I envision this package helping with cleaning data for text mining and other data science applications.

## Using emoji_map

There are two functions: `emoji_map`, and `replace_emojis`

`emoji_map`: Given a unicode emoji, returns keywords of that emoji, or `KeyError` if the emoji is not found.

`replace_emojis`: Given a string, replaces all found emojis with their keywords, and returns the new string.

```python
from emoji_map import emoji_map

emoji_map('\U0001F30E')
# earth globe americas
emoji_map('U0001F30E')
# earth globe americas
emoji_map('\u1F469\u200D\u2764\uFE0F\u200D\u1f48b\u200D\u1f468')
# kiss man woman

from emoji_map import replace_emojis

replace_emojis('hello, \U0001F30E!')
# hello, earth globe americas !
```

## Installation

python setup.py install

## Credits

The list of all emojis can be found here: [link](http://unicode.org/emoji/charts/full-emoji-list.html)

Thanks to the guys of [Spotfund](http://spotfund.com) for being open to open sourcing :)
