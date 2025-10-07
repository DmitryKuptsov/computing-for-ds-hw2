import pandas as pd

covid = pd.read_csv('covid.csv')


def death_ratio(df, min_active):
    subset = covid[covid["Active"] > min_active].copy()
    total_deaths = subset["Deaths"].sum()
    total_confirmed = subset["Confirmed"].sum()
    countries = subset["Country"].tolist()
    avg_ratio = total_deaths/total_confirmed

    return countries, avg_ratio


def result_printed():
    for min_active_cases in [500, 1000, 5000]:
        countries, avg_ratio = death_ratio(covid, min_active_cases)
        print(f"\nResult for more then {min_active_cases} active cases")
        print(f"Countries: {', '.join(countries)}")
        print(f"Total average of death/confirmed: {avg_ratio:.2%}")


result_printed()