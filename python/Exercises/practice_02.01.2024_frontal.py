import re

# email = 'mendy@tecladocode.com'
# # expreesion = '[a-z]+\.'
# expreesion = '[a-z\.]+'
#
# matches = re.findall(expreesion,email)
# print(matches)
#
# name = matches[0]
# domain = matches[1]
#---------------------------------
'''email = 'Mendy@Mendelson.com'
parts = email.split('@')
name = parts[0]
domain = parts[1]
print(f'{name}\n{domain}')'''
#----------------------------------------------------------
'''def validate_email(email):
    parts = email.split('@')

    if len(parts) != 2:
        return False

    userName = parts[0]
    if not userName or not re.match(r"[a-zA-Z0-9_\.]+", userName):
        return False

    domain = parts[1]
    if not domain or "." not in domain:
        return False

    subdomains = domain.split('.')
    if len(subdomains) < 2:
        return False

    return True

valid_emails = ["Eyal@Eyal.com", "869@tal.sh.com"]
invalid_emails = ["user", "user@", "user@user@unvalid", "tal.ex", "@.com"]

for email in valid_emails:
    if validate_email(email):
        print(f"{email} is valid")
    else:
        print(f"{email} is invalid")

for email in invalid_emails:
    if validate_email(email):
        print(f"{email} is valid (SHOULD BE INVALID)")
    else:
        print(f"{email} is invalid as expected")'''
#----------------------------------------------------------
price = 'price: $18,649.50'
# expression = '189.50'
# expression = 'price: \$(189.50)'
expression = 'price: \$([0-9\,]+\.[0-9]{2})'


matches = re.search(expression, price)
# print(matches.group(0))
# print(matches.group(1))

# price_num = float(matches.group(1))
# print(price_num)

price_without_comma = matches.group(1)
print(price_without_comma)

price_fixed = matches.group(1).replace(',','')

print(f"{float(price_fixed):.2f}")