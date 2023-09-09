from os import startfile


def run_programs(application_dict):
    # Attempts to run every application in a dictionary. Key is name, value is file path
    errors = 0

    for key in application_dict.keys():
        app_path = application_dict[key]
        # tries to run every application then notes if it fails
        try:
            startfile(app_path)
        except FileNotFoundError:
            print(f"Failed to run {key}")
            errors += 1

    # Reports of how many errors occurred
    if errors >= 1:
        print(f"{errors} errors")
        input("Enter to continue")


def define_applications_dict(file):
    # Takes the applications and filepaths from input csv and returns it as a dictionary
    try:
        with open(file, 'r') as application_csv:
            # Puts first column into `app_name` and second column into `filepath`
            applications_dict = {}
            for csv_row in application_csv:
                app_name = str(csv_row.split(',')[0])
                filepath = str(csv_row.split(',')[1]).strip()
                applications_dict[app_name] = filepath
        return applications_dict
    except FileNotFoundError:
        print(f"Failed to find find '{file}'")
        exit()


def main():
    input_applications_csv = 'application_list.csv'
    run_programs(define_applications_dict(input_applications_csv))


if __name__ == '__main__':
    main()
