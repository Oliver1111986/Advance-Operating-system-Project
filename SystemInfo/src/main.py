"""
main.py - Integration Module (MAIN) with Enhanced UI
Project Lead: Oliver D. Toe
UI Enhancement: Princeton
SRS Alignment: Section 3.3 (MAIN-MENU-01 to MAIN-VAL-03, MAIN-INT-01 to MAIN-INT-04)
Allowed Libraries: os, sys, time
"""
import os
import sys
import time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))) 
# ============================================================================
# ANSI COLOR CODES & FORMATTING (No external libraries needed!)
# ============================================================================
class Colors:
    """ANSI escape codes for terminal colors and formatting"""
    # Colors
    CYAN = '\033[96m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    MAGENTA = '\033[95m'
    WHITE = '\033[97m'
    GRAY = '\033[90m'
    
    # Formatting
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================
def clear_screen():
    """Clears the terminal screen (MAIN-MENU-04)"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_box(title, content_lines, color=Colors.CYAN, width=70):
    """
    Print content inside a styled box with borders
    Args:
        title: Box title (displayed at top)
        content_lines: List of strings to display inside box
        color: ANSI color code for borders
        width: Total width of the box
    """
    # Top border with title
    print(color + "╔" + "═" * width + "╗" + Colors.RESET)
    print(color + "║" + Colors.BOLD + f" {title} ".center(width - 2) + Colors.RESET + color + "║" + Colors.RESET)    
    
    # Content
    for line in content_lines:
        # Handle empty lines
        if not line:
            print(color + "║" + " " * width + "║" + Colors.RESET)
        else:
            # Truncate if too long
            if len(line) > width - 2:
                line = line[:width - 5] + "..."
            print(color + "║" + Colors.RESET + f" {line}".ljust(width - 1) + color + "║" + Colors.RESET)
    
    # Bottom border
    print(color + "╚" + "═" * width + "╝" + Colors.RESET)

def display_header():
    """
    Display the application header with dynamic styling (Safe from Syntax Errors!)
    """
    clear_screen()
    width = 60
    
    # Print top border
    print(Colors.CYAN + "╔" + "═" * width + "╗" + Colors.RESET)
    
    # Print Title Line
    print(Colors.CYAN + "║" + Colors.RESET + Colors.BOLD + Colors.WHITE + "  SYSINFO PRO v1.0".center(width) + Colors.RESET + Colors.CYAN + "║" + Colors.RESET)
    
    # Print Subtitle Line
    print(Colors.CYAN + "║" + Colors.RESET + Colors.BOLD + Colors.WHITE + "  System Information & File Organizer".center(width) + Colors.RESET + Colors.CYAN + "║" + Colors.RESET)
    
    # Print University Line
    print(Colors.CYAN + "║" + Colors.RESET + Colors.GRAY + "  Operating Systems Project | Tubman University".center(width) + Colors.RESET + Colors.CYAN + "║" + Colors.RESET)
    
    # Print bottom border
    print(Colors.CYAN + "╚" + "═" * width + "╝" + Colors.RESET)
    print()

def display_fancy_menu():
    """
    Display the professional-looking menu with enhanced UI (MAIN-MENU-01)
    Returns: User's menu choice as string
    """
    display_header()
    
    menu_options = [
        "",
        Colors.BOLD + Colors.WHITE + "[1] Show System Information Report" + Colors.RESET,
        "",        Colors.BOLD + Colors.WHITE + "[2] Organize Files in a Folder" + Colors.RESET,
        "",
        Colors.BOLD + Colors.WHITE + "[3] Exit Application" + Colors.RESET,
        ""
    ]
    
    print_box("MAIN MENU", menu_options, Colors.CYAN, width=60)
    print()
    
    # Get user input with styled prompt
    try:
        choice = input(Colors.CYAN + Colors.BOLD + "  └─ Enter your choice (1-3): " + Colors.RESET).strip()
        return choice
    except EOFError:
        return '3'  # Exit on EOF

# ============================================================================
# MAIN APPLICATION LOGIC
# ============================================================================
def main():
    """Main application loop and module integrator (MAIN-MENU-03, MAIN-INT-02)"""
    
    # Initial loading screen
    display_header()
    print(Colors.CYAN + "  Initializing SysInfo Pro..." + Colors.RESET)
    print(Colors.GRAY + "  Loading modules... Please wait." + Colors.RESET)
    time.sleep(1.5)
    
    # Main application loop (MAIN-MENU-03)
    while True:
        try:
            # Display menu and get choice
            choice = display_fancy_menu()
            
            if choice == '1':
                # MAIN-INT-01 & MAIN-INT-02: Import & route to sysinfo
                display_header()
                print(Colors.CYAN + Colors.BOLD + "  ══ SYSTEM INFORMATION REPORT ══" + Colors.RESET)
                print()
                
                try:
                    import sysinfo
                    sysinfo.display_report()
                except ImportError:
                    # MAIN-INT-03: Handle missing module gracefully
                    print(Colors.RED + "\n  [ERROR] Module 'sysinfo.py' not found." + Colors.RESET)
                    print(Colors.GRAY + "  Please ensure sysinfo.py is in the same directory." + Colors.RESET)
                except Exception as e:
                    print(Colors.RED + f"\n  [ERROR] System report failed: {str(e)}" + Colors.RESET)
                input(Colors.CYAN + "\n  [Press Enter to return to menu...]" + Colors.RESET)

            elif choice == '2':
                # MAIN-INT-01 & MAIN-INT-02: Import & route to organizer
                display_header()
                print(Colors.CYAN + Colors.BOLD + "  ══ FILE ORGANIZER ══" + Colors.RESET)
                print()
                
                try:
                    import organizer
                    organizer.start()
                except ImportError:
                    # MAIN-INT-03: Handle missing module gracefully
                    print(Colors.YELLOW + "\n  [NOTICE] Module 'organizer.py' not found." + Colors.RESET)
                    print(Colors.GRAY + "  This module is currently under development." + Colors.RESET)
                    print(Colors.GRAY + "  Please check back later." + Colors.RESET)
                except AttributeError as ae:
                    print(Colors.RED + "\n  [ERROR] 'organizer.py' found but entry function mismatch." + Colors.RESET)
                    print(Colors.GRAY + f"  Details: {str(ae)}" + Colors.RESET)
                except Exception as e:
                    print(Colors.RED + f"\n  [ERROR] File organizer failed: {str(e)}" + Colors.RESET)
                
                input(Colors.CYAN + "\n  [Press Enter to return to menu...]" + Colors.RESET)

            elif choice == '3':
                # MAIN-MENU-03: Exit gracefully
                display_header()
                print()
                print(Colors.GREEN + Colors.BOLD + "  Thank you for using SysInfo Pro!" + Colors.RESET)
                print(Colors.GRAY + "  Developed by: Oliver, Princeton, and Prince" + Colors.RESET)
                print(Colors.GRAY + "  Tubman University - Department of Computer Science" + Colors.RESET)
                print(Colors.GRAY + "  Academic Year 2025-2026" + Colors.RESET)
                print(Colors.GRAY + "  We're the Future Billioners 🧑🏽‍💻💰💷🏧💳" + Colors.RESET)
                print()
                time.sleep(7)
                clear_screen()
                sys.exit(0)

            else:
                # MAIN-VAL-02: Invalid range handling
                display_header()
                print(Colors.YELLOW + "\n  ⚠️  WARNING: Invalid choice!" + Colors.RESET)
                print(Colors.GRAY + "  Please enter 1, 2, or 3." + Colors.RESET)
                time.sleep(2)

        except KeyboardInterrupt:
            # MAIN-VAL-03: Handle Ctrl+C gracefully
            display_header()
            print(Colors.YELLOW + "\n  ⚠️  Operation cancelled by user (Ctrl+C)." + Colors.RESET)
            print(Colors.GRAY + "  Returning to main menu..." + Colors.RESET)
            time.sleep(1.5)
if __name__ == "__main__":
    main() 