def initial_connection_retry_delay(refresh_period: float) -> float:
    """Clamp the retry delay so startup failures do not hammer the inverter."""
    try:
        delay = float(refresh_period)
    except (TypeError, ValueError):
        delay = 15.0
    return max(5.0, min(delay, 60.0))
