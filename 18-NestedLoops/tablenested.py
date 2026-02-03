# Nested loops examples
tables = ['customers','orders','products']
columns = ['id','create_date']
for t in tables:
    for c in columns:
        print(f'SELECT count(*) FROM {t} WHERE {c} IS NULL;')