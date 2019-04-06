
import re

# line = "gjc123"
# regex_str = "^g.*3$"


# line = "gsafasggjc123"
# regex_str = ".*?(g.*?g).*"  ## ?防止贪婪匹配模式
# match_obj = re.match(regex_str,line)
# if match_obj:
#     print(match_obj.group(1))



line = "gsafasggjc123"
regex_str = ".*(b.+b).*"  ## + 
match_obj = re.match(regex_str,line)
if match_obj:
    print(match_obj.group(1))

