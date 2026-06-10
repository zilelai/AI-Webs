import os
import time

def run_menu():

    all_files = os.listdir('.')
    py_files = [f for f in all_files if f.endswith('.py') and f != 'main.py']
    
    if not py_files:
        print("Source failed")
        return False

    print("\nAvailable AIs:")
    for index, filename in enumerate(py_files, 1):
        print(f" {index} {filename}")
        
    
    


    user_choice = input("\nType the file name/number to open:").strip()

    

    if user_choice.isdigit():
        idx = int(user_choice) - 1
        if 0 <= idx < len(py_files):
            target_file = py_files[idx]

    else:
        if user_choice in py_files:
            target_file = user_choice
        elif f"{user_choice}.py" in py_files:
            target_file = f"{user_choice}.py"


    if target_file:
        print(f"\n{target_file}...\n")
        try:
            with open(target_file, "r", encoding="utf-8") as file:

                file_code = file.read()
                exec(file_code, {"__name__": "__main__"})
            
            print(f" {target_file} ")
            time.sleep(1)
        except Exception as e:
            print(f"\n❌ Error running {target_file}: {e}")
    else:
        print("\nSource not found")
        time.sleep(1)
        
    return True


if __name__ == "__main__":
    loop_alive = True
    while loop_alive:
        loop_alive = run_menu()
