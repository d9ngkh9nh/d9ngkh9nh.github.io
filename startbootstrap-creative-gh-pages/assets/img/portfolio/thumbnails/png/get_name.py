import os

def list_files(folder_path):
    # Create a list to store file names
    file_names = []

    # Iterate over files in the folder
    for filename in os.listdir(folder_path):
        # Check if the file has the desired extension
        if filename.endswith(('.jpg', '.jpeg', '.png', '.gif')):
            # Create a formatted file name and add it to the list
            file_names.append(f'"{filename}"')

    return file_names

if __name__ == "__main__":
    # Specify the folder path
    folder_path = "startbootstrap-creative-gh-pages/assets/img/portfolio/thumbnails/png"

    # Get the list of file names
    file_names = list_files(folder_path)

    # Print the result
    print(', '.join(file_names))
