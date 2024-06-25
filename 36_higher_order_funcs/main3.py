def html_tag(tag):

    def wrap_text(msg):
        print(f'<{tag}>{msg}</{tag}>')

    return wrap_text

h1 = html_tag('h1')
h1('Hey this is a heading')