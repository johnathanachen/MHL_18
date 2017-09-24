import re

mystring =  "https://www.amazon.com/Muscle-Mac-Protein-Macaroni-Cheese/dp/B01JIZYD64/ref=sr_1_1_sspa/146-1146615-6346226?ie=UTF8&qid=1506202063&sr=8-1-spons&keywords=mac#customerReviews"

# regexp = re.compile("/dp/(...)/}")
# print(regexp.search(mystring).group(1))

m = re.search('(?<=/dp/)\w+', mystring)
print(m.group(0))