import json


def get_meta_data(systemName: str) -> str:
    response = [{"metadata": "Unknown metadata"}]
    with open(r"data/meta_data.json") as meta_data_file:
        meta_data = json.load(meta_data_file)
    systemName = remove_system_prefix(systemName)

    if systemName == "A":
        response = meta_data[0]
    elif systemName == "B":
        response = meta_data[1]
    return response


def get_lineage_data(systemName: str) -> str:
    response = [{"lineagedata": "Unknown lineage data"}]
    with open(r"data/lineage_data.json") as lineage_data_file:
        lineage_data = json.load(lineage_data_file)
    systemName = remove_system_prefix(systemName)
    if systemName == "A":
        response = lineage_data[0]
    elif systemName == "B":
        response = lineage_data[1]
    return response


# def get_data_change_logic(systemName):


def get_entity_data(systemName: str) -> str:
    response = [{"entityData": "Unknown data"}]
    with open(r"data/entity_data.json") as entity_data_file:
        entity_data = json.load(entity_data_file)
    systemName = remove_system_prefix(systemName)
    if systemName == "A":
        response = entity_data[0]
    elif systemName == "B":
        response = entity_data[1]
    return response


def remove_system_prefix(input_string):
    prefix1 = "System "
    prefix2 = "system "

    if input_string.startswith(prefix1):
        return input_string[len(prefix1) :]
    elif input_string.startswith(prefix2):
        return input_string[len(prefix2) :]
    else:
        return input_string
