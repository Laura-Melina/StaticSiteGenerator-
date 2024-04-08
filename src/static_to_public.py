import os,shutil


def copy_static_to_public(source_dir_path, dest_dir_path):
    
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)
    for file in os.listdir(source_dir_path):
        from_path = os.path.join(source_dir_path,file)
        dest_path = os.path.join(dest_dir_path,file)
        print(f" * {from_path} -> {dest_path}")
        if os.path.isfile(from_path):
            shutil.copy(from_path,dest_path)
        else: 
            copy_static_to_public(from_path,dest_path)