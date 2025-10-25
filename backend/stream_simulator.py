import random

# We'll simulate a slowly changing value with noise
current_value = random.randint(60, 90)

def generate_mock_stream_data():
    """
    Simulates real-time sensor/prediction/compression-like data.
    - original value changes slightly over time (like temperature/traffic load/etc)
    - predicted tries to follow closely (like a model)
    - delta shows compression/prediction difference
    """
    global current_value

    # Add small noise to create continuous change
    current_value += random.randint(-3, 3)

    # Limit the value range to avoid going too low or too high
    current_value = max(50, min(current_value, 100))

    original_value = current_value
    predicted_value = original_value - random.randint(0, 3)  # Slight offset
    delta = original_value - predicted_value  # Difference (simulating delta)

    return {
        "original": original_value,
        "predicted": predicted_value,
        "delta": delta
    }
