"""
Author: Graham Gilbert-Schroeer
Starting Date: 2/10/26

Initial creation by Dietrich Geisler on 10/23/2025
Reviewed by: Anastasia Kurdia on 02/04/2026

Test cases for the "Chicago listings report" functions
"""

import os
import report

# TODO: add new data files for testing

TEST_PATH_1 = "test1.csv"
TEST_PATH_2 = "test2.csv"
TEST_PATH_3 = "test3.csv"
TEST_PATH_4 = "test4.csv"


def test_read_data():
    """
    Test cases for read_data
    """
    fn_name = "read_data"

    inp = TEST_PATH_1
    expected = [
        ["0", "n/a", "172632", "Sarah", "n/a", "n/a", "0", "0", "Entire home/apt", "5", "0", "0", "0", "0", "0", "n/a", "n/a", ""],
        ["0", "n/a", "329038", "Marvin", "n/a", "n/a", "0", "0", "Private room", "7", "200", "0", "0", "0", "0", "n/a", "n/a", "32-"],
    ]
    result = report.read_data(inp)
    error_message = f"expected {expected} for {fn_name}({inp}), got {result}"
    assert expected == result, error_message

    inp = TEST_PATH_2
    expected = [
        ["0", "n/a", "182736", "Mittens", "n/a", "n/a", "0", "0", "Entire home/apt", "1215", "29", "0", "0", "0", "0", "n/a", "n/a", "it's pending"],
        ["0", "n/a", "182736", "Mittens", "n/a", "n/a", "0", "0", "Private room", "172", "30", "0", "0", "0", "0", "n/a", "n/a", "R1723617236"],
        ["0", "n/a", "182736", "Mittens", "n/a", "n/a", "0", "0", "Entire home/apt", "12798", "235", "0", "0", "0", "0", "n/a", "n/a", "2732+"],
        ["0", "n/a", "127377", "Caeser", "n/a", "n/a", "0", "0", "Entire home/apt", "2374", "5", "0", "0", "0", "0", "n/a", "n/a", "R12873132-"],
        ["0", "n/a", "127377", "Caeser", "n/a", "n/a", "0", "0", "Private room", "2374", "100", "0", "0", "0", "0", "n/a", "n/a", ""],
        ["0", "n/a", "126357", "Gigi", "n/a", "n/a", "0", "0", "Entire home/apt", "37263", "3000", "0", "0", "0", "0", "n/a", "n/a", "pending"],
    ]
    result = report.read_data(inp)
    error_message = f"expected {expected} for {fn_name}({inp}), got {result}"
    assert expected == result, error_message

    print(f"tests for {fn_name} passed")


def test_get_host_name_by_id():
    """
    Test cases for get_host_name_by_id
    """

    fn_name = "get_host_name_by_id"

    file_path = TEST_PATH_1
    inp = report.read_data(file_path)
    expected = "Sarah"
    id_to_test = "172632"
    result = report.get_host_name_by_id(inp, id_to_test)
    error_message = f"expected {expected} for {fn_name}(...{file_path}, {id_to_test}), got {result}"
    assert expected == result, error_message

    expected = "Name not found"
    id_to_test = "999999"
    result = report.get_host_name_by_id(inp, "999999")
    error_message = f"expected {expected} for {fn_name}(...{file_path}, {id_to_test}), got {result}"
    assert expected == result, error_message

    file_path = TEST_PATH_2
    inp = report.read_data(file_path)
    expected = "Mittens"
    id_to_test = "182736"
    result = report.get_host_name_by_id(inp, "182736")
    error_message = f"expected {expected} for {fn_name}(...{file_path}, {id_to_test}), got {result}"
    assert expected == result, error_message

    file_path = TEST_PATH_3
    inp = report.read_data(file_path)
    expected = "Cleo"
    id_to_test = "333"
    result = report.get_host_name_by_id(inp, id_to_test)
    error_message = f"expected {expected} for {fn_name}(...{file_path}, {id_to_test}), got {result}"
    assert expected == result, error_message

    file_path = TEST_PATH_4
    inp = report.read_data(file_path)
    expected = "Name not found"
    id_to_test = "900"
    result = report.get_host_name_by_id(inp, id_to_test)
    error_message = f"expected {expected} for {fn_name}(...{file_path}, {id_to_test}), got {result}"
    assert expected == result, error_message

    print(f"tests for {fn_name} passed")


def test_count_short_term_rentals():
    """
    Test cases for count_short_term_rentals
    """

    fn_name = "count_short_term_rentals"

    file_path = TEST_PATH_1
    inp = report.read_data(file_path)
    expected = 1
    result = report.count_short_term_rentals(inp)
    error_message = f"expected {expected} for {fn_name}(...{file_path}), got {result}"
    assert expected == result, error_message

    file_path = TEST_PATH_2
    inp = report.read_data(file_path)
    expected = 2
    result = report.count_short_term_rentals(inp)
    error_message = f"expected {expected} for {fn_name}(...{file_path}), got {result}"
    assert expected == result, error_message

    file_path = TEST_PATH_3
    inp = report.read_data(file_path)
    expected = 4
    result = report.count_short_term_rentals(inp)
    error_message = f"expected {expected} for {fn_name}(...{file_path}), got {result}"
    assert expected == result, error_message

    file_path = TEST_PATH_4
    inp = report.read_data(file_path)
    expected = 12
    result = report.count_short_term_rentals(inp)
    error_message = f"expected {expected} for {fn_name}(...{file_path}), got {result}"
    assert expected == result, error_message

    print(f"tests for {fn_name} passed")


def test_count_listings_by_type():
    """
    Test cases for count_listings_by_type
    """

    fn_name = "count_listings_by_type"

    file_path = TEST_PATH_1
    inp = report.read_data(file_path)
    expected = {"Entire home/apt": 1, "Private room": 1}
    result = report.count_listings_by_type(inp)
    error_message = f"expected {expected} for {fn_name}(...{file_path}), got {result}"
    assert expected == result, error_message

    file_path = TEST_PATH_2
    inp = report.read_data(file_path)
    expected = {"Entire home/apt": 4, "Private room": 2}
    result = report.count_listings_by_type(inp)
    error_message = f"expected {expected} for {fn_name}(...{file_path}), got {result}"
    assert expected == result, error_message

    file_path = TEST_PATH_3
    inp = report.read_data(file_path)
    expected = {"Entire home/apt": 1, "Private room": 1, "Shared room": 1, "": 1, "Hotel room": 1}
    result = report.count_listings_by_type(inp)
    error_message = f"expected {expected} for {fn_name}(...{file_path}), got {result}"
    assert expected == result, error_message

    file_path = TEST_PATH_4
    inp = report.read_data(file_path)
    expected = {"Entire home/apt": 10, "Private room": 2, "Shared room": 1}
    result = report.count_listings_by_type(inp)
    error_message = f"expected {expected} for {fn_name}(...{file_path}), got {result}"
    assert expected == result, error_message

    print(f"tests for {fn_name} passed")


def test_get_license_status():
    """
    Test cases for get_license_status
    """

    fn_name = "get_license_status"

    file_path = TEST_PATH_1
    inp = report.read_data(file_path)
    expected = {"unlicensed": 1, "pending": 0, "exempt": 1, "licensed": 0}
    result = report.get_license_status(inp)
    error_message = f"expected {expected} for {fn_name}(...{file_path}), got {result}"
    assert expected == result, error_message

    file_path = TEST_PATH_2
    inp = report.read_data(file_path)
    expected = {"unlicensed": 1, "pending": 2, "exempt": 2, "licensed": 1}
    result = report.get_license_status(inp)
    error_message = f"expected {expected} for {fn_name}(...{file_path}), got {result}"
    assert expected == result, error_message

    file_path = TEST_PATH_3
    inp = report.read_data(file_path)
    expected = {"unlicensed": 1, "pending": 1, "exempt": 2, "licensed": 1}
    result = report.get_license_status(inp)
    error_message = f"expected {expected} for {fn_name}(...{file_path}), got {result}"
    assert expected == result, error_message

    file_path = TEST_PATH_4
    inp = report.read_data(file_path)
    expected = {"unlicensed": 1, "pending": 1, "exempt": 1, "licensed": 10}
    result = report.get_license_status(inp)
    error_message = f"expected {expected} for {fn_name}(...{file_path}), got {result}"
    assert expected == result, error_message

    print(f"tests for {fn_name} passed")


def test_count_multi_listings():
    """
    Test cases for count_multi_listings
    """

    fn_name = "count_multi_listings"

    file_path = TEST_PATH_1
    inp = report.read_data(file_path)
    expected = 0
    result = report.count_multi_listings(inp)
    error_message = f"expected {expected} for {fn_name}(...{file_path}), got {result}"
    assert expected == result, error_message

    file_path = TEST_PATH_2
    inp = report.read_data(file_path)
    expected = 5
    result = report.count_multi_listings(inp)
    error_message = f"expected {expected} for {fn_name}(...{file_path}), got {result}"
    assert expected == result, error_message

    file_path = TEST_PATH_3
    inp = report.read_data(file_path)
    expected = 2
    result = report.count_multi_listings(inp)
    error_message = f"expected {expected} for {fn_name}(...{file_path}), got {result}"
    assert expected == result, error_message

    file_path = TEST_PATH_4
    inp = report.read_data(file_path)
    expected = 12
    result = report.count_multi_listings(inp)
    error_message = f"expected {expected} for {fn_name}(...{file_path}), got {result}"
    assert expected == result, error_message

    print(f"tests for {fn_name} passed")


def test_count_listings_by_host_count():
    """
    Test cases for count_listings_by_host_count
    """

    fn_name = "count_listings_by_host_count"

    file_path = TEST_PATH_1
    inp = report.read_data(file_path)
    expected = [2, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    result = report.count_listings_by_host_count(inp)
    error_message = f"expected {expected} for {fn_name}(...{file_path}), got {result}"
    assert expected == result, error_message

    file_path = TEST_PATH_2
    inp = report.read_data(file_path)
    expected = [1, 2, 3, 0, 0, 0, 0, 0, 0, 0]
    result = report.count_listings_by_host_count(inp)
    error_message = f"expected {expected} for {fn_name}(...{file_path}), got {result}"
    assert expected == result, error_message

    file_path = TEST_PATH_3
    inp = report.read_data(file_path)
    expected = [3, 2, 0, 0, 0, 0, 0, 0, 0, 0]
    result = report.count_listings_by_host_count(inp)
    error_message = f"expected {expected} for {fn_name}(...{file_path}), got {result}"
    assert expected == result, error_message

    file_path = TEST_PATH_4
    inp = report.read_data(file_path)
    expected = [1, 2, 0, 0, 0, 0, 0, 0, 0, 10]
    result = report.count_listings_by_host_count(inp)
    error_message = f"expected {expected} for {fn_name}(...{file_path}), got {result}"
    assert expected == result, error_message

    print(f"tests for {fn_name} passed")


def test_get_prices():
    """
    Test cases for get_prices
    """

    fn_name = "get_prices"

    file_path = TEST_PATH_1
    inp = report.read_data(file_path)
    expected = [5.0, 7.0]
    result = report.get_prices(inp)
    error_message = f"expected {expected} for {fn_name}(...{file_path}), got {result}"
    assert expected == result, error_message

    assert isinstance(result[0], float), "Prices must be returned as floats"

    file_path = TEST_PATH_2
    inp = report.read_data(file_path)
    expected = [1215.0, 12798.0, 2374.0, 37263.0]
    room_type = "Entire home/apt"
    result = report.get_prices(inp, room_type)
    error_message = f"expected {expected} for {fn_name}(...{file_path}, {room_type}), got {result}"
    assert expected == result, error_message

    file_path = TEST_PATH_3
    inp = report.read_data(file_path)
    expected = [150.0, 80.0, 60.0, 200.0]
    result = report.get_prices(inp)
    error_message = f"expected {expected} for {fn_name}(...{file_path}), got {result}"
    assert expected == result, error_message

    file_path = TEST_PATH_4
    inp = report.read_data(file_path)
    room_type = "Private room"
    expected = [75.0, 85.0]
    result = report.get_prices(inp, room_type)
    error_message = f"expected {expected} for {fn_name}(...{file_path}, {room_type}), got {result}"
    assert expected == result, error_message

    print(f"tests for {fn_name} passed")


def test_listings_per_host_with_type():
    """
    Test cases for listings_per_host_with_type
    """

    fn_name = "listings_per_host_with_type"

    file_path = TEST_PATH_1
    inp = report.read_data(file_path)
    expected = {"172632": 1, "329038": 1}
    result = report.listings_per_host_with_type(inp)
    error_message = f"expected {expected} for {fn_name}(...{file_path}), got {result}"
    assert expected == result, error_message

    file_path = TEST_PATH_2
    inp = report.read_data(file_path)
    expected = {"182736": 2, "127377": 1, "126357": 1}
    room_type = "Entire home/apt"
    result = report.listings_per_host_with_type(inp, room_type)
    error_message = f"expected {expected} for {fn_name}(...{file_path}, {room_type}), got {result}"
    assert expected == result, error_message

    file_path = TEST_PATH_3
    inp = report.read_data(file_path)
    expected = {"111": 1, "222": 2, "333": 1, "444": 1}
    result = report.listings_per_host_with_type(inp)
    error_message = f"expected {expected} for {fn_name}(...{file_path}), got {result}"
    assert expected == result, error_message

    file_path = TEST_PATH_4
    inp = report.read_data(file_path)
    room_type = "Entire home/apt"
    expected = {"9001": 10, "9002": 0, "9003": 0}
    result = report.listings_per_host_with_type(inp, room_type)
    error_message = f"expected {expected} for {fn_name}(...{file_path}, {room_type}), got {result}"
    assert expected == result, error_message

    print(f"tests for {fn_name} passed")


def test_all():
    test_read_data()
    test_get_host_name_by_id()
    test_count_short_term_rentals()
    test_count_listings_by_type()
    test_get_license_status()
    test_count_multi_listings()
    test_count_listings_by_host_count()
    test_get_prices()
    test_listings_per_host_with_type()
    print("All tests passed!")


if __name__ == "__main__":
    test_all()
