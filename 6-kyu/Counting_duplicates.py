import string


def duplicates(s):
    cnt = 0
    s.lower
    for i in string.ascii_lowercase + string.digits + string.punctuation+string.whitespace:
        if s.count(i) > 1:
            cnt += 1
    return cnt

def duplicate_count(text):
    return len([c for c in set(text.lower()) if text.lower().count(c)>1])

print(duplicate_count("halabalAlalApadamnakrzyk12121i"))
