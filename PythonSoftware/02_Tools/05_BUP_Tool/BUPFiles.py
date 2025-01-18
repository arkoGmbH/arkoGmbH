
import shutil
import os
from datetime import datetime




def create_folder_with_timestamp(base_path):
    """
    Creates a folder with the current date and time in the specified base path.
    
    :param base_path: The directory where the folder should be created.
    """
    # Get current date and time in a formatted string
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    folder_name = f"BUP_{timestamp}"
    folder_path = os.path.join(base_path, folder_name)
    
    try:
        # Create the folder
        os.makedirs(folder_path, exist_ok=True)
        print(f"Folder created: {folder_path}")
        return folder_path
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def copy_folder(src, dst):
    """
    Copies a folder from src to dst. Overwrites the destination folder if it exists.
    
    :param src: Source folder path
    :param dst: Destination folder path
    """
    try:
        # Check if source exists
        if not os.path.exists(src):
            print(f"Source folder '{src}' does not exist!")
            return
        
        # Copy the folder
        shutil.copytree(src, dst, dirs_exist_ok=True)
        print(f"Folder '{src}' successfully copied to '{dst}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

    # Example usage
    # source_folder = r"C:\path\to\source\folder"
    # destination_folder = r"C:\path\to\destination\folder"

    # copy_folder(source_folder, destination_folder)



def main():
    
    base_directory = "/Volumes/BUPSSD"  
    Path=create_folder_with_timestamp(base_directory)



    # 00_All
    folder_name = f"00_All"
    folder_path = os.path.join(Path, folder_name)
    source_folder = r"/Users/newmini/Documents/00_All"
    destination_folder = folder_path
    copy_folder(source_folder, destination_folder)

    


    

if __name__ == "__main__":
    main()
