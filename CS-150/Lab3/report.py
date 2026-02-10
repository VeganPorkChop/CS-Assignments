"""
Author: Graham Gilbert-Schroeer
Starting Date: 2/10/26

Initial creation by Dietrich Geisler on 10/23/2025
Reviewed by: Anastasia Kurdia on 02/04/2026

Implementations of functions for a report on Chicago area listings
"""

# Import necessary modules
import csv
import os
import statistics

IDX_HOST_ID = 2
IDX_HOST_NAME = 3
IDX_ROOM_TYPE = 8
IDX_PRICE = 9
IDX_MIN_NIGHTS = 10
IDX_LICENSE = 17

# Your code for constant definitions goes here


def read_data(path_to_csv: str) -> list[list[str]]:
    """Converts the data in the given CSV file to a table of strings

    In this result, each row of the data is represented as a list
      and each column in a given row is represented as a string

    The data header (the first row of the data) is _not_ included
    This function assumes that the given file has a header row
    
    This function errors if the given path does not exist

    Arguments:
        path_to_csv: the relative path of a CSV file

    Returns:
        the data contained in the CSV as a table
    """
    # Hint: consider using read_data from utils.py in lab1 as a starting point
    # Automate the Boring Stuff also has a longer article on CSV files that is quite helpful:
    #  https://automatetheboringstuff.com/3e/chapter18.html
    file = open(path_to_csv, "r",  encoding = "utf-8")
    reader = csv.reader(file)
    return_list = list(reader)
    file.close()
    
    return return_list[1:][:]


def get_host_name_by_id(data: list[list[str]], host_id: str) -> str:
    """Retrieves the host name associated with host_id
         or "Name not found" if there is no host with the given host_id

    Arguments:
      data: an Inside Airbnb dataset
      host_id: the id of the host to retrieve

    Returns:
      the host name associated with host_id
    """
    for row in data:
        if host_id == row[IDX_HOST_ID]:
            return row[IDX_HOST_NAME]
    return "Name not found"


def count_short_term_rentals(data: list[list[str]]) -> int:
    """Counts the number of short-term rentals in data

    A short-term rental is one where the MINIMUM number of nights is
      strictly less than 30 nights

    Arguments:
      data: an Inside Airbnb dataset

    Returns:
      the number of short-term rentals as a non-negative integer
    """
    count = 0
    for row in data:
        if int(row[IDX_MIN_NIGHTS]) < 30:
            count+=1
    return count


def count_listings_by_type(data: list[list[str]]) -> dict[str, int]:
    """Creates a dictionary mapping room types to the number of such rooms

    Concretely returns a dictionary mapping a room type to
      the number of times that room type appears in data

    Any entry with an empty room type (that is, an empty string) should be ignored
    Room types are not hardcoded, but instead worked out from the given data

    Arguments:
      data: an Inside Airbnb dataset

    Returns:
      a dictionary mapping room types (as strings) to the non-negative
        number of times that given room type appears
    """
    return_dict = {}
    
    for row in data:
        key = row[IDX_ROOM_TYPE]
        if key not in return_dict:
            return_dict[key] = 1
        else:
            return_dict[key] += 1

    return return_dict


def get_license_status(data: list[list[str]]) -> dict[str, int]:
    """Creates a dictionary mapping license type to the number of listings of that type

    Each listing is categorized as one of four types,
      "unlicensed", "pending", "exempt", and "licensed",
      using the rules as follows:

    1. An entry that is empty is considered unlicensed
    2. An entry that has 'pending' anywhere in the license is considered pending (case insensitive)
    3. An entry that has one of '32+', '32-', '32 +', or '32 -' in the license is considered exempt
    4. Anything that is neither pending nor exempt nor unlicensed is considered licensed

    If there are no listings of a type of a license, 
        that license type maps to 0 in the resulting dictionary

    Arguments:
      data: an Inside Airbnb dataset

    Returns:
      a dictionary mapping license types (as strings) to the non-negative
        number of times that given license type appears
    """
    # Note: Some of your values might be different from those included on Inside Airbnb
    #   This is due to how we simplified searching for license status in this function
    return_dict = {}
    return_dict["unlicensed"] =0
    return_dict["pending"] =0
    return_dict["exempt"] =0
    return_dict["licensed"] =0
        
    for row in data:
        if row[IDX_LICENSE] == 'n/a' or row[IDX_LICENSE] == '' or row[IDX_LICENSE] == 'N/A':
            return_dict['unlicensed'] +=1
        elif 'pending' in row[IDX_LICENSE].lower():
            return_dict['pending'] +=1
        elif '32+' in row[IDX_LICENSE] or '32-' in row[IDX_LICENSE] or '32 +' in row[IDX_LICENSE] or '32 -' in row[IDX_LICENSE]:
            return_dict['exempt'] +=1
        else:
            return_dict['licensed'] +=1
        
    return return_dict


def count_multi_listings(data: list[list[str]]) -> int:
    """Counts the total number of listings made by hosts with multiple listings

    A host has multiple listings if they have posted at least 2 listings
    A host is uniquely identified by their HOST ID

    Refer to the "Listings Per Hosts" section on https://Inside Airbnb.com/chicago/
    To compare your result with Inside Airbnb, we are calculating
      what is referred to as the number of multi-listings

    Arguments:
      data: an Inside Airbnb dataset

    Returns:
      the total number of "multiple listings"
    """
    # To compare your result with Inside Airbnb, refer to the
    #   number of "multi-listings" on https://Inside Airbnb.com/chicago.

    # Hint: consider using two for loops in sequence for this problem
    host_counts = {}
    for row in data:
        host_id = row[IDX_HOST_ID]
        if host_id not in host_counts:
            host_counts[host_id] = 0
        host_counts[host_id] += 1
    
    total = 0
    for host_id, count in host_counts.items():
        if count >= 2:
            total += count

    return total


def count_listings_by_host_count(data: list[list[str]]) -> list[int]:
    """Creates a list containing the number of listings by hosts of a fixed number of listings

    Concretely, this list is organized where each index 'i+1' contains the 
      number of listings by hosts with exactly 'i+1' listings, up to 9 listings
    Additionally, the 9th index of this list contains the number of
      listings by hosts with _at least_ 10 listings
    A host is uniquely identified by their HOST ID

    For example, if we have lst = count_listings_by_host_count(data)
      then lst[0] is how many listings are by hosts with exactly 1 listing
      and  lst[4] is how many listings are by hosts with exactly 5 listings
      and  lst[9] is how many listings are by hosts with at least 10 listings

    Arguments:
      data: an Inside Airbnb dataset

    Returns:
      a list of how many listings are listed for every host providing i listings
    """
    # To compare your result with Inside Airbnb, refer to the bar diagram titled
    #   "Listings Per Host" on https://Inside Airbnb.com/chicago.

    # TODO: Implement me!

    # Hint: this line of code makes a list of 10 zeros,
    #   which may be helpful when implementing this function
    listing_counts = [0] * 10
    for row in data:
        host_id = row[IDX_HOST_ID]
        count = 0
        for row2 in data:
            if host_id == row2[IDX_HOST_ID]:
                count +=1
        if count >= 10:
            listing_counts[9] +=1
        else:
            listing_counts[count-1] +=1

    return listing_counts


def get_prices(data: list[list[str]], room_type: str = "") -> list[float]:
    """Creates a list containing listing prices, excluding empty prices

    Room type is an optional parameter to filter listings

    If room type is an empty string (the default value), all non-empty listings are returned
    If room type is non-empty, only include listed prices with that room type

    If the price is not listed (i.e. it's an empty string), 
      it is not included in the returned list

    Arguments:
      data: an Inside Airbnb dataset

    Returns:
      a list of all filtered listing prices
    """
    prices = []
    for row in data:
        if row[IDX_PRICE] != "":
            if room_type == "" or row[IDX_ROOM_TYPE] == room_type:
                prices.append(float(row[IDX_PRICE]))
    return prices


def listings_per_host_with_type(data: list[list[str]], room_type: str = "") -> dict[str, int]:
    """Creates a dictionary mapping host ids to listing counts for that host

    In other words, returns the number of listings per host

    The room type is an optional parameter to filter listings (similar to get_prices):
    * If room type is empty, consider all listings
    * If room type is non-empty (e.g. "Entire home/apt"), 
        then consider only listings with that room type

    If a host has no listings of the given room type, 
        then the dictionary contains that host id mapping to 0
        rather than skipping the host id entirely

    Arguments:
      data: an Inside Airbnb dataset
      room_type: the type of room to filter

    Returns:
      A dictionary where the keys are strings denoting host ids 
        and the values are integers denoting each host's listing count
    """
    host_counts = {}
    for row in data:
        host_id = row[IDX_HOST_ID]
        if host_id not in host_counts:
            host_counts[host_id] = 0
        if room_type == "" or row[IDX_ROOM_TYPE] == room_type:
            host_counts[host_id] += 1

    return host_counts


# --------------------------------------------------------------------------
# The following functions generate the report and are implemented for you


# constants used for the file names of our report
FILE_NAME_INPUT = "chicago_listings.csv"
FILE_NAME_OUTPUT = "report.txt"


def generate_report():
    """Produces a report in the current working directory and prints to the terminal

    If a function is unimplemented or the produced data is not validated
    Then this function will crash rather than writing the report
    """
    # Recall that "working directory" is wherever we run this code from

    assert FILE_NAME_INPUT in os.listdir(
    ), "make sure chicago_listings.csv is in this directory"

    print("-" * 60)
    print("Validating code and generating report for " + FILE_NAME_INPUT)

    with open(FILE_NAME_OUTPUT, "w") as f:
        f.write("*" * 31)
        f.write(f"\nREPORT FOR {FILE_NAME_INPUT}\n")
        f.write("(Data as of September 22, 2025)\n")
        f.write("*" * 31)

        # Validation and report for read_data
        # Note: read_data() already skips the header row, so we do not slice [1:] here.
        listings = read_data(FILE_NAME_INPUT)
        n = len(listings)
        assert isinstance(
            listings[0], list), "listings should be a list of lists"
        assert isinstance(
            listings[0][1], str), "listings should be a list of lists of strings"
        assert n > 0, "listings should have at least one entry"
        f.write(f"\n\nTotal listings: {n:,}\n")

        # Validation and report for count_short_term_rentals
        strs = count_short_term_rentals(listings)
        assert isinstance(
            strs, int), "count_short_term_rentals() should return an integer"
        f.write("\nListings that are:")
        f.write(
            f"\nShort-term rentals : {strs:,} ({round(((strs/n)*100), 1)}%)"
            f"\nLonger-term rentals: {n-strs:,} ({round((((n-strs)/n)*100), 1)}%)\n\n"
        )

        # Validation and report for count_listings_by_type
        listings_type = count_listings_by_type(listings)
        assert isinstance(
            listings_type, dict), "count_listings_by_type should return a dictionary"
        assert "Private room" in listings_type, "count_listings_by_type should include string keys 'Private room'"
        assert sum(list(listings_type.values())) == len(
            listings), "all listings should be accounted for"
        f.write("Listings with room type:\n")
        for listing, count in sorted(listings_type.items(), key=lambda item: -item[1]):
            f.write(f"{listing:<15}: {count:,} ({round(((count/n)*100), 1)}%)\n")

        # Validation and report for get_license_status
        license_status = get_license_status(listings)
        assert isinstance(
            license_status, dict), "get_license_status should return a dictionary"
        assert "exempt" in license_status, "get_license_status should have string keys 'licensed', 'unlicensed', 'exempt',and 'pending'"
        assert sum(list(license_status.values())) == len(
            listings), "check the values returned by get_license_status"
        unlicensed = license_status["unlicensed"] + license_status["pending"]
        f.write(
            f"\nNumber of unlicensed current listings, at least {unlicensed:,} ({round(((unlicensed/n)*100), 1)}%); "
            f"including {license_status['unlicensed']:,} with missing license and {license_status['pending']:,} pending\n"
        )

        for status, count in sorted(license_status.items(), key=lambda item: -item[1]):
            f.write(f"{status:<10}: {count:,}\n")

        # Validation and report for count_multi_listings
        multihosts = count_multi_listings(listings)
        assert isinstance(
            multihosts, int), "count_multi_listings should return an integer"
        f.write(
            f"\nNumber of listings by hosts with multiple listings: {multihosts:,} out of {n:,} total listings "
            f"({round(((multihosts/n)*100), 1)}%)\n\n"
        )

        # Validation and report for count_listings_by_host_count
        counts = count_listings_by_host_count(listings)
        print(counts)
        print(len(listings))
        print(count_multi_listings(listings))
        assert counts[0] == len(listings) - count_multi_listings(listings), \
            "Single listing count incorrect"

        assert sum(counts) == len(listings), \
            "Number of listings per host doesn't sum to the total number of listings"
        for i in range(len(counts) - 1):
            f.write(
                f"Listings by hosts with {i+1} listings  : {counts[i]:,}\n")
        f.write(f"Listings by hosts with 10+ listings: {counts[9]:,}\n")

        # Validation and report for get_prices
        prices = get_prices(listings)
        assert isinstance(prices, list), "get_prices should return a list"
        assert isinstance(
            prices[0], float), "get_prices should return a list of floats"

        f.write("\n-----Analyzing prices-----\n")

        f.write(f"{len(prices):,} prices in the list\n")
        if len(prices) > 0:  # Avoiding division by 0
            average = sum(prices) / len(prices)
            f.write(f"Average listing price ${average:.02f}\n")
            f.write(
                f"Median listing price  ${statistics.median(prices):.02f}\n")

        f.write("\n")
        home_prices = get_prices(listings, "Entire home/apt")
        f.write(f"{len(home_prices):,} prices for Entire home/apt\n")
        if len(home_prices) > 0:  # Avoiding division by 0
            average = sum(home_prices) / len(home_prices)
            f.write(f"Average entire apt price ${average:.02f}\n")
            f.write(
                f"Median entire apt price  ${statistics.median(home_prices):.02f}\n")

        # Validation and report for listings_per_host_with_type
        listing_counts = listings_per_host_with_type(listings)
        assert sum(list(listing_counts.values())) == len(
            listings), "Number of listings per host computed incorrectly"
        # Get top ten listing counts
        top_hosts = sorted(listing_counts.items(),
                           key=lambda item: item[1], reverse=True)[:10]
        f.write(
            f"\n-----Top {len(top_hosts)} hosts with the largest number of listings-----\n")
        for host_id, count in top_hosts:
            f.write(f"{get_host_name_by_id(listings, host_id):<17} has {count}\n")

        listing_counts = listings_per_host_with_type(
            listings, "Entire home/apt")
        top_hosts = sorted(listing_counts.items(),
                           key=lambda item: item[1], reverse=True)[:10]
        f.write(
            f"\n-----Top {len(top_hosts)} hosts with largest number of entire home listings-----\n")
        for host_id, count in top_hosts:
            f.write(f"{get_host_name_by_id(listings, host_id):<17} has {count}\n")

    # If successfully validated and file written, display report to the user
    print("-" * 60)
    print("Report has been written to", FILE_NAME_OUTPUT)
    print("-" * 60 + "\n")
    with open(FILE_NAME_OUTPUT, "r") as file:
        print(file.read())


# Skip the report generation if we are running this as a *module* (e.g. when we run test cases)
# Otherwise, generate the report!
if __name__ == "__main__":
    generate_report()
