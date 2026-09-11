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

