# Channels of Inequality: Unpacking the SES-Achievement Gradient Across PISA 2022 Countries

## Overview
This repository contains the full source materials for the computational social science project analyzing international socioeconomic inequality in student achievement. The project uses PISA 2022 data to explicitly decompose the SES-achievement gradient into its key constituent components: Parental Education, Parental Occupational Status, and Household Resources.

The goal is to move beyond composite measures (like the standard PISA ESCS index) to compare the separate effects of these factors on performance across countries and subjects, providing a nuanced account intended to inform educational policy.


## Repository Structure

## Repository Structure

| Folder/File | Description | Purpose |
| :--- | :--- | :--- |
| `report/` | Contains the LaTeX source, bibliography (`.bib`), and the final compiled PDF (`sample-sigconf.pdf`). | Source for the academic paper and final output. |
| `scripts/` | **Primary code source.** All files (e.g., R or Python scripts) used for data cleaning, statistical modeling, and figure generation. | Reproducibility of all quantitative results. |
| `data/` | Root directory for all data, including PISA microdata downloads and external files (e.g., World Bank API). | Standard location for all inputs (excludes large PISA files via `.gitignore`). |
| `analysis/` | *(Likely legacy folder or housing helper functions)*. | Secondary code/model outputs or helper scripts. |
| `talk/` | Contains the presentation slides or materials related to the project. | Communication and presentation of research findings. |
| `figures/` | Contains all final, generated visuals (e.g., `figure1.png`, `table1.png`) inserted into the report. | Final assets for publication. |
| `requirements.txt` | Lists the necessary software packages and dependencies (e.g., Python packages or R libraries). | Environment setup and dependency management. |
| `.gitignore` | Specifies which files (e.g., LaTeX compilation artifacts, temp data) Git should ignore. | Keeps the repository clean and focused on source code. |


---

## Data Sourcing and Setup (Crucial Step)

Due to copyright and size limitations, the PISA microdata is **not included** in this repository. To fully reproduce the analysis, you must manually download the required files from the official OECD PISA website and place them in the correct sub-directories.

### A. PISA Microdata Files

The analysis relies on the PISA 2022 student and school questionnaire data.

1.  **Download:** Obtain the PISA 2022 Public Use Data from the OECD website.
2.  **Placement:** Extract the relevant Stata/SAV files and place them into the sub-directory: `data/PISA2022_Stata_PublicCodes/`

The primary files required, based on the repository's internal structure, are:

| File Type | Expected File Name | Purpose |
| :--- | :--- | :--- |
| Student Questionnaire Data | `CY08MSP_STU_QQQ.SAV` | Contains all achievement PVs, SES components, and student weights. |
| School Questionnaire Data | `CY08MSP_SCH_QQQ.SAV` | Used to extract school-level variables, if needed (e.g., tracking age). |

### B. Required SES and Achievement Variables

[cite_start]The following key variables are extracted and utilized in the analysis[cite: 1]:

| Variable | Description | Role in Analysis |
| :--- | :--- | :--- |
| **Achievement** | `PV1MATH` to `PV10SCIE` | [cite_start]Plausible Values (PVs) for achievement in Mathematics, Reading, and Science[cite: 1]. |
| **SES - Resources** | `ESCS` | Household Wealth/Resources component (Composite PISA Index). |
| **SES - Education** | `PAREDINT` | Parental Education component. |
| **SES - Occupation** | `HISEI` | Parental Occupational Status component. |
| **Weights** | `W_FSTUWT` | [cite_start]Student Final Weights, used for WLS estimation[cite: 1]. |

### C. External Data (GDP)

The analysis includes external country-level economic data.

* The World Bank API data used (e.g., GDP per capita) is located in: `data/API_NY/`

---

## Reproducibility: Compiling the Report

Once the data is correctly structured in the `data/` folder: execute the main `/analysis` notebooks and `/scripts` notebooks to generate the results and figures. Files will be saved to and read from `/temp` as a form of checkpointing because the SAS7BDAT files are large and take a long time to read and parse. 

Once the analysis and scripts are complete, ensure that the figures generated have been moved to the report folder and labeled appropriately. There are three figures in total. 

Navigate to the `report` folder and use the classic $\text{LaTeX}$ sequence (as the project uses $\text{BibTeX}$):

```bash
# 1. Generate the .aux file
pdflatex sample-sigconf.tex 

# 2. Process citations and bibliography
bibtex sample-sigconf 

# 3. Final two passes to resolve references, page counts, and links
pdflatex sample-sigconf.tex
pdflatex sample-sigconf.tex
```
The final output, sample-sigconf.pdf, will be located in the report/ folder.
