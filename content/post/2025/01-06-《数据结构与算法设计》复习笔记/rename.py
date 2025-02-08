import os

def rename_index_files(directory='.'):
    # Walk through directory and subdirectories
    for root, dirs, files in os.walk(directory):
        # Check each file
        for filename in files:
            if filename == 'index.md':
                # Create full file paths
                old_path = os.path.join(root, filename)
                new_path = os.path.join(root, 'index_.md')
                
                try:
                    # Rename the file
                    os.rename(old_path, new_path)
                    print(f'Renamed: {old_path} -> {new_path}')
                except Exception as e:
                    print(f'Error renaming {old_path}: {e}')

if __name__ == '__main__':
    # Start from current directory
    rename_index_files()
    print('Renaming complete!')
