# CampusLibraryAssistant

CampusLibraryAssistant is a library and student assistant bot project, designed to help campus communities—students, faculty, and staff—access information and resources efficiently. This repository is a fork of [StudentAssistantBot](https://github.com/rohit20001221/StudentAssistantBot), adapted and extended to fit campus library needs.

## Features

- **Library Book Search**: Search for available books and resources in the campus library.
- **Loan & Due Management**: Manage your borrowed books, keep track of due dates and renewals.
- **Syllabus Reference**: Reference course material and syllabus (see `Syllabus(list).xlsx`).
- **Bot Integration**: The assistant bot can answer common library and academic queries.
- **Database Support**: Uses SQLite (`db.sqlite3`) to store data such as user information and book records.

## Repository Structure

```
CampusLibraryAssistant/
│
├── StudentAssistant/         # Main source code for the assistant
├── bot/                     # Bot-related scripts and modules
├── Syllabus(list).xlsx       # Syllabus and reference materials
├── db.sqlite3                # SQLite database
├── manage.py                 # Management script (likely Django or similar)
└── .gitignore
```

## Technology Stack

- **Language**: Python
- **Database**: SQLite
- **Framework**: (Likely Django or similar, based on `manage.py`—see code for specifics)
- **Bot Framework**: Custom or third-party integration (see `bot/` directory)

## Getting Started

1. **Clone the repository:**
   ```bash
   git clone https://github.com/jadepossum/CampusLibraryAssistant.git
   cd CampusLibraryAssistant
   ```

2. **Install dependencies:**  
   *(Check within the project for a requirements file or dependency list, e.g. `requirements.txt`)*

3. **Database setup:**  
   The project uses an SQLite database file (`db.sqlite3`), which should work out-of-the-box.  
   If you need to reset, delete this file and re-run the setup/migrations.

4. **Run the project:**  
   If using Django, try:
   ```bash
   python manage.py runserver
   ```
   *(See the code for more specific instructions.)*

## Contributing

Contributions, suggestions, and bug reports are welcome! Please fork the repo and submit a pull request, or open an issue for any feedback.

## License

*No license information is specified—please consult the repository owner for licensing details.*

---

*CampusLibraryAssistant: Making campus library resources accessible, searchable, and manageable for everyone!*
```
