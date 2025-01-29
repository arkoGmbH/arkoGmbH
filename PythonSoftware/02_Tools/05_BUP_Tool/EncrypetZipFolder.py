import subprocess
import os


def create_encrypted_zip(folder_path, output_path, password):
    """
    Creates an encrypted zip file from a folder on macOS.

    :param folder_path: Path to the folder to be encrypted
    :param output_path: Path to save the zip file (should end in .zip)
    :param password: Password for encryption
    """
    try:
        command = [
            "zip", "-er", output_path, folder_path
        ]

        process = subprocess.run(command, input=f"{password}\n".encode(), check=True)
        if process.returncode == 0:
            print(f"Encrypted zip file '{output_path}' created successfully from folder '{folder_path}'.")
    except subprocess.CalledProcessError as e:
        print(f"Error creating encrypted zip file: {e}")


if __name__ == "__main__":
    folder_path = os.path.expanduser("~/Documents/Temp")  # Replace with the actual folder path
    password = "Man"  # Replace with a strong password
    output_path = os.path.expanduser("~/Desktop/SecureFolder.zip")

    create_encrypted_zip(folder_path, output_path, password)
