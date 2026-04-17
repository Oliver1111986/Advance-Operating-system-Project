"""
main.py - Integration Module (MAIN)
Project Lead: Oliver D. Toe
SRS Alignment: Section 3.3 (MAIN-MENU-01 to MAIN-VAL-03, MAIN-INT-01 to MAIN-INT-04)
Allowed Libraries: os, sys, time
"""
import os
import sys
import time

# Add current directory to Python path for module imports
# This fixes the import issue when running from different directories
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def clear_screen():
    """Clears the terminal screen (MAIN-MENU-04)"""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu():
    """Displays the main menu with 3 options (MAIN-MENU-01)"""
    print("\n" + "="*45)
    print("          SYSINFO PRO - MAIN MENU ")
    print("="*45)
    print("[1] System Information Report ")
    print("[2] Organize Files in a Folder ")
    print("[3] Exit Application ")
    print("="*45)

def main():
    """Main application loop and module integrator (MAIN-MENU-03, MAIN-INT-02)"""
    clear_screen()
    print("SYSINFO PRO v1.0 | Operating Systems Project 1")
    print("Loading modules... Please wait.")
    time.sleep(1.5)
    
    while True:
        clear_screen()
        display_menu()

        try:
            choice = input("Enter your choice (1-3): ").strip()

            if choice == '1':
                try:
                    import sysinfo
                    sysinfo.display_report()
                except ImportError:
                    print("\n[ERROR] Module 'sysinfo.py' not found.")
                    print("Please ensure sysinfo.py is in the same directory.")
                except Exception as e:
                    print(f"\n[ERROR] System report failed: {e}")
                input("\n[Press Enter to return to menu...] ")

            elif choice == '2':
                try:
                   import organizer
                   organizer.start()
                except ImportError:
                    print("\n[ERROR] Module 'organizer.py' not found.")
                    print("Please ensure organizer.py is in the same directory.")
                except Exception as e:
                    print(f"\n[ERROR] File organizer failed: {e}")
                input("\n[Press Enter to return to menu...] ")

            elif choice == '3':
                print("\nThank you for using SysInfo Pro. Goodbye!")
                time.sleep(1)
                clear_screen()
                sys.exit(0)

            else:
                print("\n[WARNING] Invalid choice. Please enter 1, 2, or 3.")
                time.sleep(1.5)

        except KeyboardInterrupt:
            print("\n\n[WARNING] Operation cancelled by user (Ctrl+C).")
            print("Returning to main menu...")
            time.sleep(1.5)

# Fixed entry point syntax
if __name__ == "__main__":
    main()