

def parse_ranges(ranges_string):
    main_list = (list(map(int, item.split('-')))
                 for item in ranges_string.split(","))
    range_list = ((range(item[0], item[1] + 1)) for item in main_list)
    result_list = [x for i in range_list for x in i]
    return result_list


def main():
    assert parse_ranges(
        "0-0,4-8,20-21,43-45") == [0, 4, 5, 6, 7, 8, 20, 21, 43, 44, 45]
    assert parse_ranges("1-2,4-4,8-10") == [1, 2, 4, 8, 9, 10]
    print("Good enough")


if __name__ == '__main__':
    main()

# frontend:
# single-page-app

# backend:
# nodejs
# ecmse6
# jest
# unit-test
# micro-services
# express
# AMUP

# DB:
# postgres
# rest

# Others:
# AWS-SDK
# PCS
# Docker
# Kubernetis
# Git & Github
