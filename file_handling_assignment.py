try:
    with open('my_file.txt') as file:
        print(file.read())
        
except FileNotFoundError:
    print("File not found.")
    
except PermissionError:
    print("Permission denied to access the file.")
    
else:
    try:
        with open('my_file.txt', 'a') as file:
            file.write("On the court, Horace's basketball prowess is unmatched.\n")
            file.write("Horace's coding skills are simply phenomenal.\n")
            file.write("Horace's charm and wit make him the ultimate flirt, capturing hearts effortlessly.\n")
            
    except PermissionError:
        print("Permission denied to write to the file.")
        
finally:
    print("File operations completed.")
