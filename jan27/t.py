# Database
# list(list), list(dict)
# list 
#   0 1 2 3 4 ...
# 0 
# 1
# 2
#   id name birth
# 0
# 1
# 2

_db = []


def insert(*users):
    for user in users:
        _db.append(user)


def _parse_date(d):
    day, month, year = d.split(".")
    return int(year), int(month), int(day)


"""
date     DR = 01.01.2000  (right) (const)

dr1 (left) (var)
dr2 (left) (var)
dr3 (left) (var)
"""


def select(*conditions):
    result = _db[:]

    for cond in conditions:
        field, op, value = cond.split()

        def check(user):
            left = user[field]

            # premanupalating data
            if field == 'id':
                right = int(value)
            elif field == 'birth':
                left = _parse_date(left)
                right = _parse_date(value)
            else:
                right = value
            
            if op == '>':
                return left > right
            if op == '<':
                return left < right
            if op == '>=':
                return left >= right
            if op == '<=':
                return left <= right
            if op == '==':
                return left == right
            if op == '!=':
                return left != right
        
        result = list(filter(check, result))
    return sorted(result, key=lambda u: u['id'])
