# import
import json

# functionalities 
# ----------------
# load functionality 
def load_data():
    try:
        with open('youtube.txt' , 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# helper functionality 
def save_data_hepler(videos):
    with open('youtube.txt' , 'w') as file:
        json.dump(videos, file)



# list functionality  
def list_all_videos(videos):
    for index , video in enumerate(videos , start = 1):
        print(f"{index}.  {video['name']}, Duration: {video['time']} ")


# add functionality 
def add_youtube_video(videos):
    name = input("Enter Youtube Video Name:")
    time = input("Enter Youtube Video Time:")
    videos.append({'name': name , 'time': time})
    save_data_hepler(videos)

# update functionality 
def update_youtube_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to update"))
    if 1<= index <= len(videos):
        name = input('Enter the new video name')
        time = input('Enter the new video time')
        videos[index - 1] = {'name': name , 'time':time}
        save_data_hepler(videos)
    else:
        print("Invalid Index Selected")

# delete functionality 
def delete_youtube_video(videos):
      list_all_videos(videos)
      index = int(input("Enter the video number to delete"))

      if 1<= index <= len(videos):
          del videos[index - 1]
          save_data_hepler(videos)
      else:
         print("Invalid Index Selected")
  

# main | entry point
def main():
    videos = load_data()
    while True:
        print("\n| Youtube Manager | Choose an option | ")
        print('-' * 50)
        print("1. List all youtube videos ")
        print("2.Add a youtube video ")
        print("3.Update a youtube video details ")
        print("4.Delete a youtube video ")
        print("5.Exit ")
        choice = input("Enter your choice")
        
        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_youtube_video(videos)
            case '3':
                update_youtube_video(videos)
            case '4':
                delete_youtube_video(videos)
            case '5':
                print("See You Again!!!!")
                break
            case _:
                print("Invalid Choice")

if __name__ == "__main__":
    main()