import app

if __name__ == '__main__':
    response = app.overlapping_schedules_searcher(file_path="./data/schedules.txt")
    print("\n".join(response))
