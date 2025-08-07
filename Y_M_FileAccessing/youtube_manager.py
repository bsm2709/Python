import json

def save_files(videos):
    with open('youtube_Manager.txt', 'w') as file:
        json.dump(videos, file)

def load_data():
    try:
        with open('youtube_Manager.txt', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
        
def list_of_videos(videos):
    print("List of videos added:")
    print("*" * 45)
    for index, video in enumerate(videos, start=1 ):
        print(f"{index}. name : {video['name']}, time : {video['time']}")

def add_videos(videos):
    name = input("Enter file name to add: ")
    time = input("Enter time duration to add: ")
    videos.append({"name" : name, "time" : time})
    save_files(videos)


def update_videos(videos):
    name = input("Enter new video name: ")
    time = input("Enter new videos time: ")
    list_of_videos(videos)
    index = int(input("Video number you want to update: "))
    if 1<= index <= len(videos):
        videos[index - 1] = {"name" : name, "time" : time}
    else:
        print("Enter valid number ")
    save_files(videos)

def delete_videos(videos):
    list_of_videos(videos)
    index = int(input("Enter video number to delete: "))
    del videos[index - 1] 
    save_files(videos)

def main():
    videos=load_data()
    while True:
        print("*" * 45)
        print("Youtube Manager !")
        print("1. List of videos added")
        print("2. Add videos to list")
        print("3. Update videos list")
        print("4. Delete the videos")
        print("5. Exit the manager")
        choice = int(input("Enter your choice: "))

        match choice:
            case 1:
                list_of_videos(videos)
            case 2:
                add_videos(videos)
            case 3:
                update_videos(videos)
            case 4:
                delete_videos(videos)
            case 5:
                break
            case _:
                print("Enter valid choice !")

if __name__ == "__main__":
    main()