# Crop video database

## Introduction
Hi! This project involves managing a SQL database of the crop video files, wind data and their DDM results. The database is manipulated and updated through a series of Python scripts and Jupyter Notebooks.

## File Descriptions
### Files you are most likely to use to update the database:
- `update_database.ipynb`: A Jupyter Notebook that includes scripts for general updates to the database.
- `update_database_add_video.ipynb`: A Jupyter Notebook focused on updating the database specifically with new video data.
### Files for downloading the wind data from the airdata.com, assign them to each video according to the media table, and upload them to the database: 
- `download_wind_data.ipynb`: A Jupyter Notebook that is responsible for downloading wind data automatically from the airdata.com.
- `load_wind_data.ipynb`: A Jupyter Notebook for loading wind data into the database. It is likely the first part of a two-step process.
- `load_wind_data2.ipynb`: A Jupyter Notebook that continues the process started in 'load_wind_data.ipynb', possibly handling additional or more complex wind data loading tasks.
### Other files:
- `connect.py`: Establishes a connection to the SQL database. It is a utility script used by other scripts to connect to the database.
- `create_database.py`: Contains the script to create the initial structure of the database. It defines tables and their relationships.
- `check_updates.ipynb`: A Jupyter Notebook that checks for updates in the dataset or the structure of the database.
- `load_videos.py`: A Python script used to load video data into the database.
- `read_kml.py`: A Python script for reading KML (Keyhole Markup Language) files. KML files are used for geographic data.

## Notes
- Always back up the database before performing major updates or structural changes.
- The actual database structure and data types should be reviewed in `create_database.py`.
- Adjust the connection settings in `connect.py` as per your database server configuration.
