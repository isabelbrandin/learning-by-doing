def has_equal_ends(a):
    return a[0].lower() == a[-1].lower()

asdf = ['hej', 'groda', 'tacos', 'HEJ', 'Hejdå']

print(has_equal_ends(asdf))
