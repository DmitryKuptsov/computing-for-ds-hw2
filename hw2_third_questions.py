def total_registered_cases(data, country):
    if data.get(country) is None:
        return 0
    arr_cases = data[country]
    return sum(arr_cases)


def total_registered_cases_per_country(data):
    dict_total_cases = {}
    for country in data.keys():
        total = total_registered_cases(data, country)
        dict_total_cases[country] = total
    return dict_total_cases


def country_with_most_cases(data):
    dict_total_cases = total_registered_cases_per_country(data)
    max_cnt = 0
    for country, cnt in dict_total_cases.items():
        if cnt > max_cnt:
            max_cnt = cnt
            max_country = country
    return max_country
