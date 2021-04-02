def weekday_name(day_of_week):
    Days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    
        >>> weekday_name(1)
        'Sunday'
        
        >>> weekday_name(7)
        'Saturday'
        
    
    if day_of_week < 1 or day_of_week > 7:
        return None

    return DAYS[day_of_week - 1]
    