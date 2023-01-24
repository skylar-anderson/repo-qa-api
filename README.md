[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/petehunt/langchain-github-bot)

## Getting started

```bash
$ pip install -r requirements.txt
$ export OPENAI_API_KEY=sk-...
$ python3 -c'from langchain_bot_simple import print_answer; print_answer("who is the lead singer of matchbox 20")'
 The lead singer of Matchbox 20 is Rob Thomas.
SOURCES: https://en.wikipedia.org/wiki/Matchbox_Twenty
$ dagit -f langchain_bot.py
```


```python
print_answer("What are the guidelines for using labels on forms?")
print_answer("What component should I use to show a users profile?")
print_answer("What are the best practices for progressive disclosure?")
print_answer("What are the dimensions each of the size variants of the Dialog component?")
```