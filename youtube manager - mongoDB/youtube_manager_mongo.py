from pymongo import MongoClient
from bson import ObjectId

# add your user and pass 
# directly pushing in the code is not good practice 
client = MongoClient() # copy the string inside here 

db = client["ytmanager"]
video_collection = db["videos"]

print(video_collection)

# functionalities 
def add_video(name , time):
    video_collection.insert_one({"name":name , "time":time})

def list_videos():
    for video in video_collection.find():
        print(f"ID: {video['_id']}\n , Name: {video['name']}\n , Time: {video['time']}")

def update_video(video_id,new_name,new_time):
    video_collection.update_one(
        {'_id': ObjectId(video_id)},
        {'$set': {'name': new_name , "time": new_time}}
    )

def delete_video(video_id):
    video_collection.delete_one({"_id": ObjectId(video_id)})

def main():
    while True:
        print("\n Youtube Mananger App")
        print("1. List all videos")
        print("2. Add new video")
        print("3. Update video")
        print("4. Delete a video")
        print("5. Exit App")
        choice = input("Enter your choice: ")

        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter Video Name: ")
            time = input("Enter Video Time: ")
            add_video(name,time)
        elif choice == '3':
            video_id = input("Enter Video ID: ")
            name = input("Enter Updated Video Name: ")
            time = input("Enter Updated Video Time: ")
            update_video(video_id , name,time)
        elif choice == '4':
            video_id = input("Enter Video ID: ")
            delete_video(video_id)
        elif choice == '5':
            print("See You Again!!!!!!!!!")
            break
        else:
            print("Invalid Choice")



if __name__ == "__main__":
    main()