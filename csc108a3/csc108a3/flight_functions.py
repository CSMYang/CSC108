"""Starter code for CSC108 Assignment 3"""

from typing import Dict, List, Set, Tuple
from flight_reader import AirportDict, RouteDict, AIRPORT_DATA_INDEXES

def get_airport_info(airports: AirportDict, iata: str, info: str) -> str:
    """Return the airport information for airport with IATA code iata for
    column info from AIRPORT_DATA_INDEXES.

    >>> get_airport_info(TEST_AIRPORTS_DICT, 'AA1', 'Name')
    'Apt1'
    >>> get_airport_info(TEST_AIRPORTS_DICT, 'AA4', 'IATA')
    'AA4'
    """
    return airports[iata][AIRPORT_DATA_INDEXES[info]]

    # Complete the function body

def is_direct_flight(iata_src: str, iata_dst: str, routes: RouteDict) -> bool:
    """Return whether there is a direct flight from the iata_src airport to
    the iata_dst airport in the routes dictionary. iata_src may not
    be a key in the routes dictionary.

    >>> is_direct_flight('AA1', 'AA2', TEST_ROUTES_DICT_FOUR_CITIES)
    True
    >>> is_direct_flight('AA2', 'AA1', TEST_ROUTES_DICT_FOUR_CITIES)
    False
    """
    if iata_src in routes:
        return iata_dst in routes[iata_src]
    else:
        return False
    # Complete the function body

def is_valid_flight_sequence(iata_list: List[str], routes: RouteDict) -> bool:
    """Return whether there are flights from iata_list[i] to iata_list[i + 1]
    for all valid values of i. IATA entries may not appear anywhere in routes.

    >>> is_valid_flight_sequence(['AA3', 'AA1', 'AA2'], TEST_ROUTES_DICT_FOUR_CITIES)
    True
    >>> is_valid_flight_sequence(['AA3', 'AA1', 'AA2', 'AA1', 'AA2'], TEST_ROUTES_DICT_FOUR_CITIES)
    False
    """
    if len(iata_list) <= 1:
        return False
    for i in range(len(iata_list) - 1):
        if iata_list[i] not in routes:
            return False
        elif not iata_list[i + 1] in routes[iata_list[i]]:
            return False
    return True

    # Complete the function body

# Write the rest of the data analysis functions + your helper functions here
def count_outgoing_flights(iata_code: str, routes: RouteDict) -> int:
    """Return an int representing the number of outgoning flights for the 
    airport with given iata_code in given route information.
    
    >>> count_outgoing_flights('AA3', TEST_ROUTES_DICT_FOUR_CITIES)
    2
    >>> count_outgoing_flights('AA2', TEST_ROUTES_DICT_FOUR_CITIES)
    1
    """
    return len(routes[iata_code])

def count_incoming_flights(iata_code: str, routes: RouteDict) -> int:
    """Return a number representing the number of incoming flights for the
    airport with given iata_code in given route information.
    
    >>> count_incoming_flights('AA3', TEST_ROUTES_DICT_FOUR_CITIES)
    1
    >>> count_incoming_flights('AA1', TEST_ROUTES_DICT_FOUR_CITIES)
    2
    """
    number = 0
    for iata in routes:
        if iata != iata_code and iata_code in routes[iata]:
            number += 1
    return number
    
def reachable_destinations(iata_code: str, allowed_flights: int, routes: \
                           RouteDict) -> List[Set[str]]:
    """Return a list of set of IATA codes corresponding to its airports that is
    reachable for an airport with iata_code under a number of allowed_flights
    flights.
    
    >>> reachable_destinations('AA1', 2, TEST_ROUTES_DICT_FOUR_CITIES)
    [{'AA1'}, {'AA2', 'AA4'}, {'AA3'}]
    """
    reachable_list = [{iata_code}]
    for i in range(allowed_flights):
        reachable_list.append(set())
        for item in reachable_list[i]:
            if item in routes:
                for item2 in routes[item]:
                    new_set = collect_sets(reachable_list)
                    if item2 not in new_set:
                        reachable_list[i + 1].add(item2)                    
    return reachable_list

def collect_sets(new_list: List[Set[str]]) -> set:
    """Return a new set that collects all elements from a list of sets.
    
    >>> collect_sets([{1,2,3}, {2,3,4}])
    {1, 2, 3, 4}
    """
    set1 = set()
    for sets in new_list:
        set1.update(sets)
    return set1
        
def find_busiest_airports(routes: RouteDict, limit: int) -> List[Tuple \
                                                                 [str, int]]:
    """Return a list of first limit busiest airports in given informations 
    routes.
    
    >>> find_busiest_airports(TEST_ROUTES_DICT_FOUR_CITIES, 3)
    [('AA1', 4), ('AA3', 3), ('AA4', 3)]
    >>> find_busiest_airports(TEST_ROUTES_DICT_FOUR_CITIES, 2)
    [('AA1', 4)]
    >>> find_busiest_airports(TEST_ROUTES_DICT_FOUR_CITIES, 1)
    [('AA1', 4)]
    """
    new_list = []
    for airport in routes:
        num = count_incoming_flights(airport, routes) + \
            count_outgoing_flights(airport, routes)
        new_tuple = (airport, num)
        new_list.append(new_tuple)
    sort_list(new_list)
    if new_list[limit - 1][1] == new_list[limit][1]:
        return new_list[: limit - 1]
    else:
        return new_list[: limit]

def sort_list(new_list: List[Tuple[str, int]]) -> None:
    """Return a sorted version of new_list from greatest to smallest regarding
    to the int of each tuple.
    
    >>> new = [('a', 1), ('b', 3), ('c', 2)]
    >>> sort_list(new)
    >>> new
    [('b', 3), ('c', 2), ('a', 2)]
    """
    for _ in new_list:
        for i in range(len(new_list) - 1):
            if new_list[i][1] < new_list[i + 1][1]:
                new_list[i], new_list[i + 1] = new_list[i + 1], new_list[i]
        
    

if __name__ == '__main__':
    """Uncommment the following as needed to run your doctests"""
    #from flight_types_constants_and_test_data import TEST_AIRPORTS_DICT
    #from flight_types_constants_and_test_data import TEST_AIRPORTS_SRC
    #from flight_types_constants_and_test_data import TEST_ROUTES_DICT_FOUR_CITIES
    #from flight_types_constants_and_test_data import TEST_ROUTES_SRC

    #import doctest
    #doctest.testmod()
