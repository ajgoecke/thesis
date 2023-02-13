# Implementation in R

This material appears in Section 5 `Implementation`.

## Subdirectories:
- `workspace`: contains the R workspace (and all variables) that is created within the notebooks in `notebooks/`, this can be loaded into R to run the code without waiting periods.
- `notebooks`: contains all R scripts that were created in section 5
- `output`: contains the output files that were generated in the `notebooks/thesis_corpusmethods.Rmd` notebook
- `corpora`: contains the current version of the corpora of both subdiscourses in .rds format


## Scripts:
- `notebooks/thesis_corpusmethods.Rmd`: Section 5.2 
- `notebooks/thesis_preprocessing.Rmd`: Section 5.1.2

## Files:

In `output/`:
- `con_context.csv`: contains the concordances for each compound word for the C2022 corpus, this file is used as input for most text mining techniques (see paper section 5.2.3)
- `pro_context.csv`: contains the concordances for each compound word for the C2022 corpus, this file is used as input for most text mining techniques (see paper section 5.2.3)
- `tf_complete.csv`: contains the term frequencies for all compound words and both corpora (see paper section 5.2.1)
- `tfidf_complete.csv`: contains the TF-IDF scores for all compound words and both corpora (see paper section 5.2.1)
- `top_collocations_con.csv`: contains the "uncleaned" version of the collocations for the C2022 corpus (see paper section 5.2.2)
- `top_collocations_pro.csv`: contains the "uncleaned" version of the collocations for the P2022 corpus (see paper section 5.2.2)
- `top_colls_con_cleaned.csv`: contains the manually cleaned collocations for the C2022 corpus
- `top_colls_pro_cleaned.csv`: contains the manually cleaned collocations for the P2022 corpus

In `workspace/`: 
- `corpus_methods.RData`: R workspace for the notebook `notebooks/thesis_corpusmethods.Rm`
- `preprocessing.RData`: R workspace for the notebook `notebooks/thesis_preprocessing.Rmd`

## Requirements
To be able to fully run all the notebooks, please make sure the following libraries are installed:
- `quanteda`: version 3.2.1 http://quanteda.io
- `readtext`: version 0.81 https://cran.r-project.org/web/packages/readtext/vignettes/readtext_vignette.html
- `tidyverse`: version 1.3.1 https://www.tidyverse.org
- `spacyr`: verison 1.2.1 https://spacyr.quanteda.io
- `data.table`: version 1.14.2 https://cran.r-project.org/web/packages/data.table/vignettes/datatable-intro.html
- `textcat`: version 1.0-7 https://rdrr.io/cran/textcat/
- `plyr`: version 1.8.7 http://had.co.nz/plyr/
- `ggplot2`: version 3.3.5