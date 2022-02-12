def default_typelist(keyList: list) -> list:
    typeList = ["varchar(255) not null"]
    for i in range(0, len(keyList) - 1):
        typeList.append("varchar(255)")
    return typeList
