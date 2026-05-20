# 🔐 Secure Coding Review

A Python security audit performed as part of the **CodeAlpha Cybersecurity Internship – Task 3**.

---

## 📌 About

This project demonstrates how to identify and fix security vulnerabilities in Python code using static analysis tools.

---

## 📂 Files

- `vulnerable_app.py` — Intentionally vulnerable Python script
- `secure_app.py` — Fixed and secured version
- `report.txt` — Raw Bandit scan output

---

## 🛠️ Tool Used

- **Bandit** — Python static security analyzer

---

## 📊 Vulnerabilities Found & Fixed

| Severity | Count |
|---|---|
| 🔴 High | 3 |
| 🟡 Medium | 2 |
| 🟢 Low | 4 |
| **Total** | **9** |

---

## 🚀 How to Run the Scan

```bash
pip install bandit
bandit -v vulnerable_app.py -o report.txt -f txt
```

---

## ⚠️ Disclaimer

The vulnerable script is created for **educational purposes only**.

---

## 👤 Author

- **Internship:** CodeAlpha Cybersecurity Internship
- **Task:** Task 3 – Secure Coding Review
