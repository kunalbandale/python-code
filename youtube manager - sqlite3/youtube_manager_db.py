import sqlite3

# database connection
conn = sqlite3.connect('youtube_videos.db')
cursor = conn.cursor()

# database table creation 
cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
              id INTEGER PRIMARY KEY,
              name TEXT NOT NULL,
              time TEXT NOT NULL
               )
 ''')

# functionalities 

# list all the videos
def list_videos():
    cursor.execute("SELECT id, name, time FROM videos")
    # Fetch and print the results
    for row in cursor.fetchall():
        index, name, time = row
        print(f"{index}. {name} - {time}")
    

# add videos 
def add_video(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    conn.commit()

# update video
def update_video(video_id, name, time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (name, time, video_id))
    conn.commit()

# delete video
def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
    conn.commit()

# driver function | entry point of the project
def main():
    while True:
        print('\nYoutube Manager APP!!')
        print('1. List Videos')
        print('2. Add Videos')
        print('3. Update Videos')
        print('4. Delete Videos')
        print('5. Exit app')
        choice = input("Enter your choice: ")

        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            add_video(name, time)
        elif choice == '3':
            video_id = int(input("Enter video ID: "))
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            update_video(video_id, name, time)
        elif choice == '4':
            video_id = int(input("Enter video ID to delete: "))
            delete_video(video_id)
        elif choice == '5':
            print('See you again!!!!')
            conn.close()
            exit(0)
        else:
            print("Invalid Choice | Try Again!!!!!")

if __name__ == "__main__":
    main()
