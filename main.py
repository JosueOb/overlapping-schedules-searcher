import app

if __name__ == '__main__':
    try:
        response = app.overlapping_schedules_searcher(file_path="./data/schedules.txt")
        print("\n".join(response))
    except app.OverlappingSchedulesError as error:
        print(str(error))
