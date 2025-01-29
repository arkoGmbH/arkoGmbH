import subprocess
import os


def create_encrypted_disk_image_from_folder(folder_path, output_path, password):
    """
    Creates an encrypted disk image from a folder on macOS.

    :param folder_path: Path to the folder to be encrypted
    :param output_path: Path to save the disk image (should end in .dmg)
    :param password: Password for encryption
    """
    try:
        command = [
            "hdiutil", "create",
            "-srcfolder", folder_path,
            "-encryption", "AES-256",
            "-stdinpass",
            "-fs", "APFS",
            "-format", "UDRW",
            output_path
        ]

        process = subprocess.run(command, input=password.encode(), check=True)
        if process.returncode == 0:
            print(f"Encrypted disk image '{output_path}' created successfully from folder '{folder_path}'.")
    except subprocess.CalledProcessError as e:
        print(f"Error creating disk image: {e}")


if __name__ == "__main__":
    folder_path = os.path.expanduser("~/Documents/SecureFolder")  # Replace with the actual folder path
    password = "your-secure-password"  # Replace with a strong password
    output_path = os.path.expanduser("~/Desktop/SecureFolder.dmg")

    create_encrypted_disk_image_from_folder(folder_path, output_path, password)
