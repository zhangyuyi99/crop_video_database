import os
import mysql.connector
from moviepy.editor import VideoFileClip
from datetime import datetime

# Connect to the database
cnx = mysql.connector.connect(user='root', password='dronevideos', host='localhost', database='wheat_videos')
cursor = cnx.cursor()

# Create the 'video' table if it does not already exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS video (
        filename VARCHAR(255),
        location VARCHAR(255),
        create_date DATE,
        create_time TIME,
        duration FLOAT,
        format VARCHAR(50),
        frame_width INT,
        frame_height INT,
        frame_rate FLOAT,
        color_space VARCHAR(50)
    )
""")

# Directory containing the video files
video_dir = "//sf3.bss.phy.private.cam.ac.uk/cicutagroup/yz655/wheat_videos/2023.05.30.Nottingham.UK/video"

# Iterate over all video files in the directory
for filename in os.listdir(video_dir):
    if filename.endswith((".MP4", ".AVI", ".MOV", ".mp4", ".avi", ".flv", ".mov", ".wmv")):  # Add or remove file extensions as needed
        filepath = os.path.join(video_dir, filename)
        
        # Check if video already exists in the database
        cursor.execute("SELECT filename FROM video WHERE filename = %s", (filename,))
        result = cursor.fetchone()
        
        # If the video already exists, skip this iteration
        if result is not None:
            continue


        clip = VideoFileClip(filepath)

        # Get video metadata
        create_timestamp = os.path.getctime(filepath)
        create_date = datetime.fromtimestamp(create_timestamp).date()
        create_time = datetime.fromtimestamp(create_timestamp).time()
        duration = clip.duration
        format = filename.split('.')[-1]
        frame_width, frame_height = clip.size
        frame_rate = clip.fps
        color_space = clip.color_space if hasattr(clip, 'color_space') else None
        
        clip.close()

        # Insert video metadata into the database
        cursor.execute("""
            INSERT INTO video (filename, location, create_date, create_time, duration, format, frame_width, frame_height, frame_rate, color_space)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (filename, filepath, create_date, create_time, duration, format, frame_width, frame_height, frame_rate, color_space))

# Commit changes and close connection
cnx.commit()
cursor.close()
cnx.close()
