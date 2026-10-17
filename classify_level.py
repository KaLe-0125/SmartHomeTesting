def classify_level(value:float)->str:
    if value>30:
        return "alert"
    elif value>20:
        return "warning"
    return "normal"