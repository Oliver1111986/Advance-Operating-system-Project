SYSINFO PRO - Operating Systems Semester Project 1
==================================================
Team: Oliver D. Toe (Project Lead), Princeton R. Zahnmie (Systems Developer), Prince Gbolon (File Systems Developer)
Course: Advance Operating Systems | Tubman University, Dept. of Computer Science
Academic Year: 2025-2026 | SDLC Model: Incremental Development
Version: 1.0 | Submission Date: May 7, 2026

DESCRIPTION:
SysInfo Pro is a Windows command-line utility that:
1. Displays a formatted system information report (OS, CPU, RAM, Page File, Disk).
2. Automatically organizes files in a specified directory into categorized subfolders.
Built with Python 3.x using only approved standard libraries + psutil.

PREREQUISITES:
- Windows 10/11 (64-bit)
- Python 3.8 or higher
- Internet connection (for initial psutil installation)

INSTALLATION:
1. Open Command Prompt or PowerShell.
2. Navigate to the project root directory:
   cd path\to\SysInfoPro
3. Install the required dependency:
   pip install psutil

HOW TO RUN:
1. Ensure you are in the project root folder.
2. Launch the application:
   python src\main.py
3. Follow the on-screen menu prompts.

USAGE GUIDE:
[1] System Information Report -> Displays OS, CPU, RAM, Page File, and Disk metrics.
[2] Organize Files           -> Prompts for a folder path, then sorts files into categories.
[3] Exit                     -> Closes the application gracefully.

SAFETY & BEHAVIOR:
- Files are NEVER deleted. Only moved.
- Duplicate filenames are automatically renamed (e.g., report_2.pdf).
- Invalid paths, permission errors, or locked files trigger clear warnings and continue safely.
- No administrative privileges required for standard operations.

TROUBLESHOOTING:
- "ModuleNotFoundError: No module named 'psutil'" -> Run: pip install psutil
- "PermissionError" during organization -> Ensure read/write access to the target folder.
- "Invalid choice" -> Enter only 1, 2, or 3. Non-numeric inputs are safely rejected.

PROJECT STRUCTURE:
SysInfoPro/
├── src/
│   ├── main.py          (Integration & CLI Menu)
│   ├── sysinfo.py       (System Information Module)
│   └── organizer.py     (File Organizer Module)
├── tests/               (Unit & integration test scripts)
├── docs/                (SRS, Project Plan, Report)
├── README.txt           (This file)
└── requirements.txt

CREDITS & CONTACT:
- Oliver D. Toe: Project Lead, Integration, Documentation, Demo Coordination
- Princeton R. Zahnmie: System Information Module Development
- Prince Gbolon: File Organizer Module Development
For academic use only. Tubman University, Dept. of Computer Science.
