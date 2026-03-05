def validate_block(prev_state, new_state):

    if new_state["level"] - prev_state["level"] > 1:
        return False, "Invalid level jump detected"

    if new_state["money"] - prev_state["money"] > 5000:
        return False, "Suspicious money gain detected"


    return True, "Valid"
