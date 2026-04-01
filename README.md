# pisa-ses-gradient-decomposition

**pisa-ses-gradient-decomposition** is a computational social science project that studies how socioeconomic status relates to student achievement across countries using **PISA 2022** microdata. Instead of treating socioeconomic status as a single composite index, the repository separates the gradient into three interpretable components: **parental education**, **parental occupational status**, and **household resources**.

The project is designed as a reproducible research repository: the analysis code, report source, and presentation materials live together so that the empirical pipeline can be inspected end to end.

| Repository focus | Description |
|---|---|
| Research domain | International educational inequality and computational social science |
| Core question | Which components of socioeconomic status drive achievement differences across countries and subjects? |
| Main data source | PISA 2022 student- and school-level microdata |
| Analytical approach | Decompose the SES–achievement gradient rather than relying only on the aggregate ESCS index |
| Portfolio value | Shows policy-facing quantitative research, data handling, and reproducible reporting |

## Research question

The repository asks a straightforward but important question: when we observe a socioeconomic gradient in test performance, what is actually carrying that signal? Rather than stopping at a broad composite SES measure, the project compares the separate roles of parental education, occupational status, and household resources. This makes the resulting analysis easier to interpret and more useful for policy discussion.

From a portfolio perspective, the value of the project is not only the substantive question. It also demonstrates the ability to work with large international survey data, organize a reproducible empirical workflow, and connect statistical analysis to a clearly framed policy narrative.

## Repository structure

| Path | Role |
|---|---|
| `analysis/` | Primary code for cleaning, modeling, and figure generation |
| `data/` | Inputs for PISA data and external country-level data |
| `scripts/` | Supporting scripts and helper workflows |
| `report/` | LaTeX paper source, bibliography, and compiled output |
| `talk/` | Slides or presentation material derived from the analysis |
| `requirements.txt` | Environment dependencies |

## Data requirements

Because the underlying PISA microdata is large and distributed separately, the repository does **not** include the raw survey files. To reproduce the analysis, you need to download the official PISA 2022 public-use files and place them in the expected directory structure.

| Data source | Expected location | Purpose |
|---|---|---|
| PISA 2022 student questionnaire data | `data/PISA2022_Stata_PublicCodes/CY08MSP_STU_QQQ.SAV` | Achievement values, SES-related covariates, and student weights |
| PISA 2022 school questionnaire data | `data/PISA2022_Stata_PublicCodes/CY08MSP_SCH_QQQ.SAV` | School-level covariates and contextual information |
| World Bank or related country data | `data/API_NY/` | Country-level controls such as GDP-related indicators |

## Main variables used in the analysis

The decomposition centers on a small set of core PISA variables that make the empirical design legible.

| Variable group | Variable(s) | Role |
|---|---|---|
| Achievement | `PV1MATH` to `PV10SCIE` | Plausible values for mathematics, reading, and science outcomes |
| Household resources | `ESCS` | Household wealth/resources component used in the comparison set |
| Parental education | `PAREDINT` | Education-based SES component |
| Parental occupation | `HISEI` | Occupational-status SES component |
| Student weights | `W_FSTUWT` | Weighting for weighted estimation |

## Reproducibility workflow

Once the required files are placed under `data/`, the typical workflow is to run the analysis code to regenerate the cleaned data products, intermediate outputs, and figures, and then compile the final report from the LaTeX source. The repository uses temporary checkpointing because the raw education datasets are large and slow to parse repeatedly.

| Step | Purpose |
|---|---|
| Run `analysis/` notebooks or scripts | Clean and model the data |
| Run supporting `scripts/` | Generate intermediate outputs and figures |
| Move final figures into `report/` as needed | Prepare the paper build |
| Compile the LaTeX report | Produce the final write-up |

To compile the paper:

```bash
cd report
pdflatex sample-sigconf.tex
bibtex sample-sigconf
pdflatex sample-sigconf.tex
pdflatex sample-sigconf.tex
```

The compiled PDF will be written to the `report/` directory.

## Reading this repository as a portfolio piece

If you are viewing this repository from the GitHub profile, the intended takeaway is that it represents a complete empirical research workflow rather than only a final paper. The code, data assumptions, and reporting assets are all visible, which makes the project legible both as a substantive investigation of educational inequality and as an example of careful quantitative research practice.

In that sense, **pisa-ses-gradient-decomposition** showcases data-intensive analysis, social-science framing, and reproducible technical communication in one place.
