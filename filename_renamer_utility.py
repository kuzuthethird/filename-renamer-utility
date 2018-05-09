import sys
import os

def main():
    print("This program will help you change filenames for all files in this directory and every subdirectory that is recursively reachable from here!")

    path = input("\nWhat's the path of the directory that you would like to recursively traverse?(just press ENTER for the directory this program is located in)\nPATH: ")
    replace = input("\nWhat sequence of characters would you like to replace in filenames: ")
    replace_with = input("With what sequence of characters would you like to replace that with: ")
    quit_or_continue = input("\nCAUTION, all filenames in the specified directory and its subdirectories containing '" + replace + "' will have that replaced with sequence '" + replace_with + "'.\nType 'c' to continue, any other character to quit, then press ENTER: ")

    if(quit_or_continue != 'c'):
        print("\nExiting")
        sys.exit(0)

    #if the user doesn't want to stay in the current directory, change to what they designated
    if(path != ""):
        #if user gives invalid path, exit
        if(os.path.isdir(path) == False):
            print("\nBAD PATH NAME!\nExiting")

            sys.exit(1)

        #change the directory to what the user wanted
        os.chdir(path)

    #update the path to what directory we're currently in
    path = os.path.abspath("")

    #does nothing, just for better formatting
    print()

    #recursively traverse the current directory and all its subdirectories
    for cur_dir, sub_dirs, files in os.walk('.', topdown=False, followlinks=False):
        #cur_dir has a '.' at the beginning and is missing a '/' at the end, so we add those
        absolute_path = path + cur_dir[1:] + '/'

        #let the user know what directory we're working in 
        print("\nIn directory: " + absolute_path)

        #loop through all the files in the current directory that have the matching sequence
        for file_name_with_sequence in (file_name for file_name in files if replace in file_name):
            #replaces the sequence in the filename with the one the user wants to replave with
            old_file_name = absolute_path + file_name_with_sequence
            new_file_name = absolute_path + file_name_with_sequence.replace(replace, replace_with)

            #catch errors if we can't change the filename
            try:
                os.rename(old_file_name, new_file_name)
            except OSError:
                #print to stderr to let the user know of error
                print("--Error: couldn't change '" + old_file_name + "' to '" + new_file_name, file=sys.stderr)
            else:
                #let the user know that we had a successful file change
                print(old_file_name + "  changed to  " + new_file_name)

if __name__ == "__main__":
    main()
