[![Python application](https://github.com/federicoparisella/batch-traceability-mock-recall/actions/workflows/python-app.yml/badge.svg)](https://github.com/federicoparisella/batch-traceability-mock-recall/actions) ![Mock Recall](https://img.shields.io/badge/Mock%20Recall-Ready-success) ![Python Version](https://img.shields.io/badge/python-3.9%20%7C%203.10%20%7C%203.11-blue) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

\## Author \& Acknowledgment

This project was developed by the repository owner.



An AI-based assistant was used as a learning and productivity support tool

to refine the project structure, improve code quality, and align the solution

with regulatory and audit-oriented best practices.



\## Integration with Data Integrity (ALCOA+)



This project is designed to operate \*\*after data integrity validation\*\*.



Before executing any traceability analysis or mock recall, datasets

(e.g. production, batches, shipments) should be validated against

\*\*ALCOA+ data integrity principles\*\* to ensure they are:



\- Attributable

\- Legible

\- Contemporaneous

\- Original

\- Accurate

\- Complete

\- Consistent

\- Enduring

\- Available



An external \*\*ALCOA+ Checker\*\* can be used as a validation gate.

If critical data integrity violations are detected, the mock recall

should not be executed, as traceability results would not be reliable.



This separation reflects real-world QA system design, where data

integrity validation and operational analytics are independent but

logically connected processes.



\## Example Workflow



1\. Execute ALCOA+ data integrity checks on operational datasets

2\. Review and resolve any critical violations

3\. Approve datasets for operational use

4\. Execute batch traceability and mock recall

5\. Generate recall evidence and KPIs





# 

