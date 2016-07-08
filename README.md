# emoji_map

This is a small python package to help you easily understand what emojis you are looking at.  If you are scraping web data like tweets, messages, etc. you will be returned the unicode encoding of all emojis that you receive.  This package enables a quick lookup of a unicode emoji, and returns the description.

========================

I envision this package helping with cleaning data for text mining and other data science applications.

## Using emoji_map

```python
from emoji_map import emoji_map

emoji_map('\U0001F30E')
# earth globe americas
emoji_map('U0001F30E')
# earth globe americas
```

## Installation

python setup.py install

## Credits

The list of all emojis can be found here: [link](http://apps.timwhitlock.info/emoji/tables/unicode)

Thanks to the guys of [Spotfund](http://spotfund.com) for being open to open sourcing :)
