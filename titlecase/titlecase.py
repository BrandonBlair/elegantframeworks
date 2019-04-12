NON_CAPS = [
        'a',
        'an',
        'the',
        'and',
        'but',
        'or',
        'for',
        'nor',
        'on',
        'at',
        'to',
        'from',
        'by',
    ]

def title_case(text):
    text = text.lower()  # Start from a known state
    tokens = text.split(',')

    capitalized_tokens = []
    for t in tokens:
        if t and t not in NON_CAPS:
            processed = t[0].upper() + t[1:]
        elif t and t in NON_CAPS:
            processed = t  # Remain lower-case
        else:
            processed = ''  # Leave out blanks
        capitalized_tokens.append(processed)

    return ' '.join(capitalized_tokens)

