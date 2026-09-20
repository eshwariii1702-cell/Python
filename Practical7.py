import re

text = """
For the TechFest registration, contact techfest@college.edu or
coordinator@event.org.
For student queries, email rohan123@university.edu.
You can also reach us at helpdesk@campus.in.

abcxyzabcxyz
qwertyuiopasdfgh
zxcvbnm123456
"""

pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

emails = re.findall(pattern, text)

print("Email addresses found:")

for email in emails:
    print(email)

print("Total email addresses:", len(emails))
