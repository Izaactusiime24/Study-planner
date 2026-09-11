study_records = []

LOG_FILE = "study_log.txt"


def classify_session(duration):
    if duration < 30:
        session_type = "Short"
    elif duration <= 90:
        session_type = "Medium"
    else:
        session_type = "Long"

    return session_type

def request_text(prompt):
    while True:
        value = input(prompt).strip()

        if value != "":
            return value

        print("This field cannot be empty. Please enter the information.")


def request_duration():
    while True:
        entered_value = input("How many minutes did you study? ").strip()

        try:
            duration = float(entered_value)

            if duration > 0:
                return duration

            print("The duration must be greater than zero.")

        except ValueError:
            print("Please enter the duration as a number.")


def add_session():
    print("\n***** RECORD NEW STUDY SESSION *****")

    subject_name = request_text("Subject name: ")
    topic_name = request_text("Topic covered: ")
    day_label = request_text("Date or day: ")
    duration = request_duration()

    record = {
        "subject": subject_name,
        "topic": topic_name,
        "date": day_label,
        "duration": duration
    }

    study_records.append(record)

    session_type = classify_session(duration)

    print("\nThe study session has been recorded.")
    print(f"Session type: {session_type}")

def view_sessions():
    print("\n***** ALL STUDY SESSIONS *****")

    if len(study_records) == 0:
        print("There are no study sessions to display.")
        return

    border = "=" * 100

    print(border)
    print(
        f"{'#':<5}"
        f"{'SUBJECT':<27}"
        f"{'TOPIC':<27}"
        f"{'DATE/DAY':<17}"
        f"{'TIME':<12}"
        f"{'TYPE':<10}"
    )
    print(border)

    for position, record in enumerate(study_records, start=1):
        session_type = classify_session(record["duration"])

        print(
            f"{position:<5}"
            f"{record['subject']:<27}"
            f"{record['topic']:<27}"
            f"{record['date']:<17}"
            f"{record['duration']:<12g}"
            f"{session_type:<10}"
        )

    print(border)
    print(f"Number of sessions: {len(study_records)}")

