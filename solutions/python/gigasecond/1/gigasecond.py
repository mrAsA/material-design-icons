def add(moment):
    from datetime import datetime, timedelta
    giga_secs = 1e9

    added_giga = moment + timedelta(seconds = giga_secs)

    return added_giga