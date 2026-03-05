def validate_block(prev_state, new_state):

    # detect level jump
    if new_state["level"] - prev_state["level"] > 1:
        return False, "Invalid level jump detected"

    # detect suspicious money gain
    if new_state["money"] - prev_state["money"] > 5000:
        return False, "Suspicious money gain detected"

    return True, "Valid"