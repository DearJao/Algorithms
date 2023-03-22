def study_schedule(permanence_period, target_time):
    try:
        count = 0
        for period in permanence_period:
            if target_time >= period[0] and target_time <= period[1]:
                count += 1
        return count
    except Exception:
        return None
