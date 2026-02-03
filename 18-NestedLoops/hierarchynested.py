# hierarchy nested loops
years = [2026, 2027]
months = ['Jan','Feb']
days = range(1,29)

for year in years:
    for month in months:
        for day in days:
            print(f"report_{year}_{month}_{day}")