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

def search_by_subject(subject):
    matching_records = []
    searched_subject = subject.strip().casefold()

    for record in study_records:
        recorded_subject = record["subject"].strip().casefold()

        if recorded_subject == searched_subject:
            matching_records.append(record)

    print(f"\n***** SEARCH: {subject.upper()} *****")

    if not matching_records:
        print("No study session matches that subject.")
        return

    total_minutes = 0

    for number, record in enumerate(matching_records, start=1):
        total_minutes += record["duration"]
        session_type = classify_session(record["duration"])

        print(f"\nResult {number}")
        print(f"Topic: {record['topic']}")
        print(f"Date/Day: {record['date']}")
        print(f"Duration: {record['duration']:g} minutes")
        print(f"Session type: {session_type}")

    print("\nSearch summary")
    print(f"Sessions found: {len(matching_records)}")
    print(f"Total minutes: {total_minutes:g}")
    print(f"Total hours: {total_minutes / 60:.2f}")

def study_statistics():
    print("\n***** STUDY ACTIVITY SUMMARY *****")

    if not study_records:
        print("No statistics can be calculated without study sessions.")
        return

    subject_totals = {}
    display_names = {}
    total_minutes = 0

    for record in study_records:
        subject_key = record["subject"].strip().casefold()

        display_names[subject_key] = record["subject"].title()

        subject_totals[subject_key] = (
            subject_totals.get(subject_key, 0)
            + record["duration"]
        )

        total_minutes += record["duration"]

    weakest_key = min(
        subject_totals,
        key=subject_totals.get
    )

    longest_record = max(
        study_records,
        key=lambda record: record["duration"]
    )

    print(f"Total sessions: {len(study_records)}")
    print(f"Total study time: {total_minutes:g} minutes")
    print(f"Total study hours: {total_minutes / 60:.2f} hours")

    print("\nTime spent on each subject:")

    for subject_key, minutes in subject_totals.items():
        subject_name = display_names[subject_key]

        print(
            f"* {subject_name}: "
            f"{minutes:g} minutes "
            f"or {minutes / 60:.2f} hours"
        )

    weakest_minutes = subject_totals[weakest_key]

    print("\nStudy observations:")

    print(
        f"Subject needing more attention: "
        f"{display_names[weakest_key]} "
        f"({weakest_minutes:g} minutes)"
    )

    print(
        f"Longest study session: "
        f"{longest_record['subject'].title()} - "
        f"{longest_record['topic'].title()} "
        f"({longest_record['duration']:g} minutes)"
    )

def save_sessions():
    try:
        with open(LOG_FILE, "w", encoding="utf-8") as file:
            for record in study_records:
                subject = record["subject"].replace(";", ",")
                topic = record["topic"].replace(";", ",")
                study_date = record["date"].replace(";", ",")
                duration = record["duration"]

                file.write(
                    f"{subject};{topic};{study_date};{duration}\n"
                )

        print(f"{len(study_records)} study record(s) saved.")

    except OSError:
        print("The study records could not be saved.")

def load_sessions():
    study_records.clear()
    loaded_records = 0

    try:
        with open(LOG_FILE, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                if line == "":
                    continue

                details = line.split(";")

                if len(details) != 4:
                    continue

                subject = details[0]
                topic = details[1]
                study_date = details[2]

                try:
                    duration = float(details[3])
                except ValueError:
                    continue

                record = {
                    "subject": subject,
                    "topic": topic,
                    "date": study_date,
                    "duration": duration
                }

                study_records.append(record)
                loaded_records += 1

        print(f"{loaded_records} saved record(s) loaded.")

    except FileNotFoundError:
        print("No previous study log exists. Starting with an empty planner.")

    except OSError:
        print("The study log could not be opened.")

def show_menu():
    print("\n" + "#" * 50)
    print("          SMART STUDY PLANNER")
    print("#" * 50)
    print("1 - Record a new study session")
    print("2 - Show all study sessions")
    print("3 - Find sessions for a subject")
    print("4 - Show study activity summary")
    print("5 - Save information and close")
    print("#" * 50)

def main():
    load_sessions()

    program_running = True

    while program_running:
        show_menu()

        choice = input("Select an action (1-5): ").strip()

        if choice == "1":
            add_session()

        elif choice == "2":
            view_sessions()

        elif choice == "3":
            subject = input(
                "Which subject would you like to find? "
            ).strip()

            search_by_subject(subject)

        elif choice == "4":
            study_statistics()

        elif choice == "5":
            save_sessions()
            print("Study information saved. Program closed.")
            program_running = False

        else:
            print(
                "Unknown menu option. "
                "Please choose a number between 1 and 5."
            )

if __name__ == "__main__":
    main()
