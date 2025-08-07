# this is same yutube video manager with db sqlite

import sqlite3
conn= sqlite3.connect("Youtube_manager.db")
cur = conn.cursor()

cur.execute(''' 
        CREATE TABLE IF NOT EXISTS videos(
                id INTEGER PRIMARY KEY ,
                name TEXT NOT NULL,
                time TEXT NOT NULL
                )
  ''')



def list_of_videos():
    print("* " * 70)
    print("list: ")
    cur.execute(''' 
        SELECT * FROM videos
     ''')
    for row in cur.fetchall():
        print(row)
    
    conn.commit()



def add_videos(name, time):
    cur.execute(''' 
        INSERT INTO videos( name , time ) VALUES (? , ?)
    ''' , (name, time))

    conn.commit()



def update_videos(name, time, index):
    cur.execute('''  
        UPDATE videos SET name= ? , time= ? WHERE id= ?
    ''',(name, time, index))
    conn.commit()

def delete_videos(index):
    cur.execute(''' 
        DELETE FROM videos WHERE id= ?
    ''', (index,) )

    conn.commit()


def main():
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
                list_of_videos()
            case 2:
                name = input("Add video name: ")
                time = input("Add time of video: ")
                add_videos(name, time)
            case 3:
                name = input("Add new video name: ")
                time = input("Add new time of video: ")
                index = int(input("Give me the index wwhich u want to update: "))
                update_videos(name, time, index)
            case 4:
                index = int(input("Give me the index wwhich u want to Delete: "))
                delete_videos(index)
            case 5:
                break
            case _:
                print("Enter valid choice !")
        conn.close

if __name__ == "__main__":
    main()