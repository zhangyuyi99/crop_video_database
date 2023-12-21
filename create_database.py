import mysql.connector

# Connect to the MySQL server
cnx = mysql.connector.connect(user='root', password='dronevideos', host='localhost')

# Create a cursor object to execute SQL statements
cursor = cnx.cursor()

# Create the 'crop_videos' database
cursor.execute("CREATE DATABASE IF NOT EXISTS crop_videos")

# Use the 'crop_videos' database
cursor.execute("USE crop_videos")

# Create the tables

# Devices table
cursor.execute("""
CREATE TABLE devices (
    device_id INT AUTO_INCREMENT PRIMARY KEY,
    device_type VARCHAR(255),
    lens_properties TEXT
)
""")

# Operators table
cursor.execute("""
CREATE TABLE operators (
    operator_id INT AUTO_INCREMENT PRIMARY KEY,
    operator_name VARCHAR(255)
)
""")

# Wind Data table
cursor.execute("""
CREATE TABLE wind_data (
    wind_data_id INT AUTO_INCREMENT PRIMARY KEY,
    wind_speed_avg FLOAT,
    wind_direction_avg FLOAT,
    detailed_wind_change_table TEXT
)
""")

# Wind Change Details table
cursor.execute("""
CREATE TABLE wind_change_details (
    wind_change_id INT AUTO_INCREMENT PRIMARY KEY,
    wind_data_id INT,
    flight_time TIME,
    altitude FLOAT,
    home_distance FLOAT,
    wind_direction FLOAT,
    wind_speed FLOAT,
    FOREIGN KEY (wind_data_id) REFERENCES wind_data(wind_data_id)
)
""")

# Wheat Data table
cursor.execute("""
CREATE TABLE wheat_data (
    wheat_data_id INT AUTO_INCREMENT PRIMARY KEY,
    wheat_type VARCHAR(255),
    wheat_location TEXT,
    date DATE,
    wheat_height_avg FLOAT
)
""")

# Detailed Wheat Data table
cursor.execute("""
CREATE TABLE detailed_wheat_data (
    detailed_wheat_data_id INT AUTO_INCREMENT PRIMARY KEY,
    wheat_data_id INT,
    wheat_section VARCHAR(255),
    wheat_section_weight FLOAT,
    FOREIGN KEY (wheat_data_id) REFERENCES wheat_data(wheat_data_id)
)
""")

# Video Group table
cursor.execute("""
CREATE TABLE video_group (
    video_group_id INT AUTO_INCREMENT PRIMARY KEY,
    group_name VARCHAR(255),
    creator VARCHAR(255)
)
""")

# Video table
cursor.execute("""
CREATE TABLE video (
    video_id INT AUTO_INCREMENT PRIMARY KEY,
    filename VARCHAR(255),
    location VARCHAR(255),
    create_date DATE,
    create_time TIME,
    duration TIME,
    format VARCHAR(50),
    frame_width INT,
    frame_height INT,
    frame_rate FLOAT,
    frame_number INT,
    color_space VARCHAR(50),
    drone_id INT,
    camera_height FLOAT,
    processed_versions TEXT,
    major_wavelength FLOAT,
    wind_data_id INT,
    wheat_data_id INT,
    video_group_id INT,
    FOREIGN KEY (drone_id) REFERENCES devices(device_id),
    FOREIGN KEY (wind_data_id) REFERENCES wind_data(wind_data_id),
    FOREIGN KEY (wheat_data_id) REFERENCES wheat_data(wheat_data_id),
    FOREIGN KEY (video_group_id) REFERENCES video_group(video_group_id)
)
""")

# Processed Videos table
cursor.execute("""
CREATE TABLE processed_videos (
    processed_video_id INT AUTO_INCREMENT PRIMARY KEY,
    video_id INT,
    filename VARCHAR(255),
    location TEXT,
    create_date DATE,
    create_time TIME,
    duration FLOAT,
    format VARCHAR(50),
    frame_width INT,
    frame_height INT,
    frame_rate FLOAT,
    color_space VARCHAR(50),
    processing_type VARCHAR(255),
    FOREIGN KEY (video_id) REFERENCES video(video_id)
)
""")

# DDM Data table
cursor.execute("""
CREATE TABLE DDM_data (
    DDM_data_id INT AUTO_INCREMENT PRIMARY KEY,
    video_id INT,
    processed_video_id INT,
    DDM_data_file_location TEXT,
    DDM_data_nonAvgIqtau_file_location TEXT,
    DDM_data_nonAvgIqtau_angle_Iqtau_file_location TEXT,
    MedianFrequencyVec FLOAT,
    Major_q FLOAT,
    Major_q_amplitude FLOAT,
    Major_q_frequency FLOAT,
    Major_q_damping FLOAT,
    Major_q_offset FLOAT,
    Major_q_gof FLOAT,
    FOREIGN KEY (video_id) REFERENCES video(video_id),
    FOREIGN KEY (processed_video_id) REFERENCES processed_videos(processed_video_id)
)
""")

# Commit the changes and close the connection
cnx.commit()
cursor.close()
cnx.close()
