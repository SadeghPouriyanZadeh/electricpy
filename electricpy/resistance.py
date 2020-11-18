# TODO:
def equivalent_resistance(resistance_list: list, parallel=None) -> float:
    """The total resistance for resistors fully connected in series or parallel

    Parameters
    ----------
    resistance_list : list
        list of resistors fully connected in series or parallel
    
    Returns
    -------
    float
        The total resistance for resistors fully connected in series or parallel
    """
    assert parallel != None, "No Connection Selected" # no connection type is selected

    if parallel:
        equivalent_resistance = 0
        for i in range(len(resistance_list)):
            equivalent_resistance += 1/(resistance_list[i])
        equivalent_resistance = 1/equivalent_resistance

    if not parallel:
        equivalent_resistance = 0
        for i in range(len(resistance_list)):
            equivalent_resistance += resistance_list[i]

    return equivalent_resistance

res_list = [5, 7]

print(equivalent_resistance(res_list, False))