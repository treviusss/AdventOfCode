#!/usr/bin/env python3
import itertools
import pathlib

import requests

SESSION = ""  # session cookie
YEARS = [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
DAYS = [day for day in range(1, 26)]
URL = "https://adventofcode.com/{}/day/{}/input"
cookies = dict(session=SESSION)

for year, day in itertools.product(YEARS, DAYS):
    dest_path = f"./{year}/day{day}"
    pathlib.Path(dest_path).mkdir(parents=True, exist_ok=True)
    with open(pathlib.Path(dest_path + f"/day{day}_input"), "w") as f:
        r = requests.get(URL.format(year, day), cookies=cookies)
        f.write(r.text)
        f.write(r.text)
