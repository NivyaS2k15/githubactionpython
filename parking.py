
def should_open_barrier(distance_cm):
    if distance_cm is None or distance_cm < 0:
        return False

    return distance_cm >10

