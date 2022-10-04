def create_a_dict_for_query(data):
    """
    :param data: list of tuple
    :return: jsonify
    """

    py_dict = {'title': data[0][0].strip(),
               'country': data[0][1].strip(),
               'release_year': data[0][2],
               'genre': data[0][3].strip(),
               'description': data[0][4].strip()}

    return py_dict


def create_list_for_years(data):
    """
    :param data: list of tuples
    :return: list
    """
    list_of_dicts = []

    for element in data:
        new_dict = {'title': element[0], 'release_year': element[1]}
        list_of_dicts.append(new_dict)

    return list_of_dicts


def create_list_for_rating(data):
    list_of_dicts = []

    for element in data:
        new_dict = {'title': element[0], 'rating': element[1], 'release_year': element[2]}
        list_of_dicts.append(new_dict)

    return list_of_dicts


def create_list_for_genres(data):
    list_of_dicts = []

    for element in data:
        new_dict = {'title': element[0].strip(), 'description': element[1].strip()}
        list_of_dicts.append(new_dict)

    return list_of_dicts


def create_list_for_actors(data):
    list_of_lists = [[x for x in ''.join(y).split(', ')] for y in data]
    appearance_count = {}
    suitable_actors = []

    for cast in list_of_lists:
        for actor in cast:
            appearance_count[actor] = appearance_count.get(actor, 0) + 1

    for key, value in appearance_count.items():
        if value > 2:
            suitable_actors.append(key)

    return suitable_actors