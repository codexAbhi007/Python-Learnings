import re

text_to_search = '''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890abc

ha haha 

Meta characters (need to escape it):
. ^ $ * + ? { } [ ] \\ | ( )

abhi.com

123-456-121
213.231.121
213#231#121
500#231#121
600#231#121
213#231#121

cat
mat
bat
hat
sat

Mr. SMith
Mr samuel
Ms Davis
Mr. Boss
Mrs Hello
Mr. T

abhi2203@gmail.com
abhi.22@gmail.edu
abhi-22-03@email.net
abhi-22-03@email.org

https://google.com
http://coreyms.com
https://www.nasa.gov
http://www.youtube.com




'''

sentence = 'start it a sentecne and bring to an end!'

#pattern = re.compile(r'abc')
# pattern = re.compile(r'.') #~ gives wrong output as it is a meta character
# pattern = re.compile(r'\.')
# pattern = re.compile(r'abhi\.com')
# pattern = re.compile(r'ha\b')
# pattern = re.compile(r'ha\b')
# pattern = re.compile(r'\Bha')
# pattern = re.compile(r'^start')
# pattern = re.compile('$start')
# pattern = re.compile(r'\d\d\d[-#.]\d\d\d[-#.]\d\d\d')
## [] this represents a character set even tough content inside can be long still it macthes only one particular character from our text

# pattern = re.compile(r'[56]00[-#.]\d\d\d[-#.]\d\d\d')
##this represents first character should be either 5 or 6 next two characters 0 and 0 

# pattern = re.compile(r'[0-5]\d\d[-#.]\d\d\d[-#.]\d\d\d')

## - is when used betwenn values represent range of values
# pattern = re.compile(r'[a-zA-Z]')

# pattern = re.compile(r'[^a-zA-Z]')
##using the caret works like not


# pattern = re.compile(r'[^b]at')
##everything except starting with b and ending with at


# pattern = re.compile(r'\d{3}[-#.]\d{3}[-#.]\d{3}')
##instead of writing \d 3 times we can use quantifiers to specify


# pattern = re.compile(r'Mr\.?\s\w*')
##Mr is taking the Mr first then \.? tells . is optional after that. \s represents a space after that. \w represents (a-z),(A-Z),(0-9). but it represent single character we use quantifier * which shows 0 or more occurences


# pattern = re.compile(r'M(s|rs)\.?\s\w*')
##() represents group | sign represents or 

# pattern = re.compile(r'[a-zA-Z0-9.-]+@[a-zA-z]+\.\w{3}')
# pattern = re.compile(r'[a-zA-Z0-9.-]+@[a-zA-z-]+\.(com|edu|net)')
##Email validation

pattern = re.compile(r'https?://(www\.)?\w+\.\w+')













matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)

