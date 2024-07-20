import os
import pandas as pd
import glob

drive_directory = 'Z:\\' # Specify the drive directory to search
file_extensions = ['*.STL', '*.3mf', '*.SLDPRT', '*.gcode'] # Specify the file extensions to search for

file_locations = pd.DataFrame(columns=['File Path', 'File Name'])

def find_files(file_extensions, drive_directory):
    for ext in file_extensions:
        for file in glob.glob(os.path.join(drive_directory, '**', ext), recursive=True):
            file_locations.loc[len(file_locations)] = [file, os.path.basename(file)]
            print(file)

find_files(file_extensions, drive_directory)

# Extract the first character or two of the drive directory
drive_prefix = drive_directory[:2] if len(drive_directory) > 1 else drive_directory

# Save the file locations to a CSV file with the drive prefix in the filename
file_locations.to_csv('File_Locations_' + drive_prefix + '.csv', index=False)