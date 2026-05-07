-----------------------------------------------
SIMULASI PORTAL PENDAFTARAN CALON PERSENDIRIAN SIJIL PELAJARAN MALAYSIA (SPM)
----------------------------------------------------
Simulation of the registeration portal of Sijil Pelajaran Malaysia (SPM) for private candidates
--------------------------------------------------
A command-line interface (CLI) application built in Python that simulates the official registration portal for private candidates sitting for the Sijil Pelajaran Malaysia (SPM) examination. The simulator replicates a realistic registration workflow from candidate verification and subject selection to payment calculation and persistent application storage.

This simulator was developed to strengthen my understanding of Python dictionaries, functions, JSON-based databases and structured validation systems. At the same time, the project introduced me to more advanced concepts such as the "re" module.

---------------------------------------------------------
Key features of the code:
-----------------------------------------------------
1. Dictionary-Driven Examination Subject Management:

- I implemented large-scale dictionaries to map user input digits to official SPM subject codes, subject names, and examination fees. This approach creates an efficient system that handles over 30 examination subjects without relying on excessively long "if-else" chains. The dictionary structure also simplifies fee calculations and subject retrieval throughout the registration process.

2. Realistic Candidate Verification System:

- The simulator validates Malaysian identification card numbers (Kad Pengenalan/MyKad) by extracting the birth year, month, and date directly from the IC number itself by using the "string slicing" method. I also used Python’s "datetime" module to verify whether the generated birth date is valid while also implementing age restrictions to prevent underage registrations. This mirrors how real government registration systems validate candidate identity data.

3. Separate Workflows for New and Repeat Candidates:

- I designed two independent registration paths: one for first-time candidates (Calon Baharu) and another for repeat candidates (Calon Mengulang) . Each workflow applies different validation rules and subject requirements. For example, repeat candidates may register fewer subjects, while new candidates must meet the minimum six-subject requirement enforced by the system logic.

4. Advanced Rule-Based Subject Validation:

- One of the most complex parts of the simulator is the subject validation engine. I implemented logical restrictions that prevent candidates from selecting conflicting subjects simultaneously. For example:

** (a) Science (1511) and Physics (4531) cannot be registered together.

** (b) Pendidikan Islam (Islamic Studies --- 1223) and Pendidikan Moral (Moral Studies --- 1225) cannot be taken together under certain conditions.

** (c) Sains Tulen (Pure Science) combinations are strictly controlled.

** (d) Maximum and minimum subject registration limits are enforced automatically.


This rule-based system simulates real-world examination registration policies while demonstrating complex conditional programming and logical validation techniques.

5. Flexible User Input Parsing with Regular Expressions:

- To improve usability, I used Python’s "re" (regular expression) module to allow users to enter multiple subject choices in a single line using flexible formatting. The system automatically extracts all valid numerical inputs and converts them into a clean selection list for processing. This creates a more professional and user-friendly CLI experience.

6. Dynamic Examination Centre Allocation:

- I implemented a location-based school selection system where candidates may choose examination centres from Kuala Lumpur or Selangor. Each state contains its own dictionary-driven list of schools, creating a modular and expandable structure that can easily support additional states and examination centres in future updates.

7. Automated Payment Calculation System:

- The simulator automatically calculates examination fees by combining the registration fee with the accumulated cost of all selected subjects. Using list comprehension and the "sum()" function, the system dynamically generates the total payment amount without requiring manual calculations. This closely resembles a real online payment summary system used in actual registration portals.

8. Persistent Data Storage via JSON:

- I implemented a JSON-based database system to simulate long-term application storage. Using "json.load()" and "json.dump()", the simulator permanently stores candidate records, payment information, selected subjects, examination centres, and timestamps even after the application is closed. This transforms the project from a temporary script into a persistent registration management system.

---------------------------------------------------
IMPORTANT NOTE:
---------------------------------------------------

1. This simulator does not currently implement the official “Mata Pelajaran Tambahan” (Additional Subject) requirement, where candidates registering for 11 or 12 subjects must take at least one additional subject.

2. The simulator currently only supports two states/territories when selecting examination centres, and each state contains only five randomly selected schools. The school selections were entirely random and were included solely for simulation purposes.

3. Candidate information is stored locally using a JSON file-based database system. This simulator does not use a real encrypted production database and should not be considered secure for handling actual personal information.

4. Some validation rules and examination policies were simplified to keep the simulator manageable and focused on learning core programming concepts.

5. This simulator was developed strictly for educational and learning purposes only. It is NOT an official registration system and should not be used for actual SPM registration.

6. This project is NOT affiliated with:
- Lembaga Peperiksaan Malaysia (Malaysian Examination Syndicate)
- Kementerian Pendidikan Malaysia (Malaysia’s Ministry of Education)

7. The project was designed to simulate the overall workflow and structure of an examination registration portal rather than perfectly replicate the official Malaysian SPM registration system.

---------------------------------------------
To use this simulator:
-------------------------------------------
- python3 spm | cat -e

OR

 - chmod +x spm.py (To ensure this program is executable)
 - ./spm.py (To run this program)
----------------------------------------
Image Demonstration:
------------------------------
<img width="1920" height="1040" alt="pendaftaran_spm json - Visual Studio Code 07_05_2026 21_22_51" src="https://github.com/user-attachments/assets/a99f6f6f-5230-48a1-a043-2dfc75bf5133" />

<img width="562" height="338" alt="MINGW64__c_Users_Matthew Kam_Desktop_R 07_05_2026 21_22_09" src="https://github.com/user-attachments/assets/af653062-1aa1-436e-b983-d794908d18ec" />
<img width="562" height="338" alt="MINGW64__c_Users_Matthew Kam_Desktop_R 07_05_2026 21_24_07" src="https://github.com/user-attachments/assets/a25cd85c-39ea-4f11-8025-a61f38d37945" />

