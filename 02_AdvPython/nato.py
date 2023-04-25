import string

nato = ['zero', 'wun', 'two', 'tree', 'fower', 'fife', 'six', 'seven', 'ait', 'niner',
        'alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'hotel', 'indigo', 
        'juliet', 'kilo', 'lima', 'mike', 'november', 'oscar', 'papa', 'quebec', 'romeo', 
        'sierra', 'tango', 'uniform', 'victor', 'whiskey', 'xray', 'yankee', 'zulu']

# This does not use the additional keys[] array.
codes = {}

for n in range(0, len(nato)):
    if n < 10:
        codes[str(n)] = nato[n]
    else: 
        codes[string.ascii_uppercase[n - 10]] = nato[n]

# This will use a keys[] array, zip() and dict().
keys = []

for n in range(0, len(nato)):
    if n < 10:
        keys.append(str(n))
    else:
        keys.append(string.ascii_uppercase[n - 10])

zip_result = dict(zip(keys, nato))

# This gets user input.
txt = input("Please enter a phrase: ").upper()

for l in txt:
    # result = codes[l]
    result = zip_result.get(l)
    if result is None:
        print(' ')
    else:
        print(result)
        