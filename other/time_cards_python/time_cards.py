#!/usr/bin/env python3
"""
Time Cards

- People are badging in and out of work, how can you figure out how many
  people started in the day and out at night? You will write a
  programing procedure to figure this out.
- You must use Python, Pandas and SQL (you can use SQL inside of Pandas
  or vice versa)

Implementation Notes

- The problem description is vauge, so I will make some assumptions:
  - Time will be in 24-hour format (18:00 means 6PM)
  - I interpret "start in the day" as "start before noon"
  - Likewise "out at night" means "out after 6PM"
  - I assume that there is a user ID (uid) associate with each
"""
import pandas as pd


def main():
    """ Entry """
    times = pd.read_csv("time.csv", parse_dates=[1, 2])

    print("\nAll records")
    print(times)

    # Filter out those that start in the day and out at night
    selected = times.query("`in` < '12:00' and `out` > '18:00'")
    print("\nSelected records")
    print(selected)


if __name__ == '__main__':
    main()


# Below is a sample output
#
# All records
#    uid                  in                 out
# 0  501 2021-09-16 06:00:00 2021-09-16 15:00:00
# 1  502 2021-09-16 06:15:00 2021-09-16 15:20:00
# 2  503 2021-09-16 08:00:00 2021-09-16 19:45:00
# 3  504 2021-09-16 11:59:00 2021-09-16 18:00:00
# 4  505 2021-09-16 11:59:00 2021-09-16 18:01:00
# 5  506 2021-09-16 13:45:00 2021-09-16 17:55:00

# Selected records
#    uid                  in                 out
# 2  503 2021-09-16 08:00:00 2021-09-16 19:45:00
# 4  505 2021-09-16 11:59:00 2021-09-16 18:01:00

