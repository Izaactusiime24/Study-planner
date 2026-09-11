study_records = []

LOG_FILE_FILE = "study_log.txt"


def classify_session(duration):
    if duration < 30:
        session_type = "Short"
    elif duration <= 90:
        session_type = "Medium"
    else:
        session_type = "Long"

    return session_type