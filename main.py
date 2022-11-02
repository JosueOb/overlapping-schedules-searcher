import app

if __name__ == '__main__':
    response = app.search_overlapping_schedules(file_path="./data/schedules.txt")
    print("\n".join(response))
