# QA USA Python Automation Framework (Sprint 7)

This repository represents **Sprint 7** of my QA Engineering journey—setting up the **foundation** for test automation using **Python**, **Pytest**, and **Selenium**.

##  What’s Inside

- **`data.py`** — central location for test data constants (e.g., URLs, addresses, phone numbers)
- **`helpers.py`** — reusable helper functions (e.g., URL connectivity check, phone confirmation code retrieval)
- **`main.py`** — structured with placeholder test methods (`test_set_route`, `test_select_plan`, etc.) using `setup_class` for early validation
- **`requirements.txt`** — listing `pytest` and `selenium` dependencies
- Clean code conventions and naming guidelines followed for ease of review

---

##  Sprint 7 Highlights

| Feature                        | Details                                               |
|--------------------------------|-------------------------------------------------------|
| **Scope**                      | Prep work for automation: modular file structure, placeholders, helper utilities |
| **Tech Stack**                 | Python 3.13, Pytest, Selenium, POM-ready structure    |
| **Next Steps (Sprint 8)**      | Fill in automation logic with Selenium (page objects, end-to-end flow) |
| **Repo Navigation**            | - `data.py`: test data constants <br> - `helpers.py`: helper utilities <br> - `main.py`: test structure setup |

---

##  How to Work Locally

1. Set up a new Python virtual environment:
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate  # or `.venv\Scripts\activate` on Windows
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run pytest to confirm placeholders pass (they won’t fail):
    ```bash
    pytest -q
    ```

---

##  Related Sprints & Portfolio

- See the full QA journey (Sprints 1–9) in my main portfolio: [Projects.md in profile repo](https://github.com/CelestRW/CelestRW)
- The **Sprint 8 automation project** with completed Selenium tests is here: [urban-routes-project](https://github.com/CelestRW/urban-routes-project)

---

Thank you for reviewing! I’m excited to extend this foundation into full end-to-end automation in Sprint 8.  
