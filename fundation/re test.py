line1="xxx出生于2001年6月1日"
line2="xxx出生于2001/6/1"
line3="xxx出生于2001-6-1"
line4="xxx出生于2001-06-01"
line5="xxx出生于2001-06"
re_pattern=".*出生于(\d{4}[/\-年]\d{1,2}($|[-/月]\d{1,2}($|日)))"
import re

match=re.match(re_pattern,line3)
if match:
    print(match.group(1))
