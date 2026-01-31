lambda kv: (
    ''.join(c for c in kv[0].lower() if c.isalpha()),
    sum(kv[1]) if type(kv[1]) is not int else kv[1]
)
