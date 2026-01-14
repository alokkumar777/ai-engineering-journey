# markdown link parser
def parse_link(markdown):
    text = markdown[markdown.index('[')+1:markdown.index(']')]
    link = markdown[markdown.index('(')+1:markdown.index(')')]

    return f'<a href="{link}>{text}</a>"'

parse_link = parse_link("[Contribute to our repository at https://github.com/freeCodeCamp/freeCodeCamp.](https://github.com/freeCodeCamp/freeCodeCamp/)")

print(parse_link)