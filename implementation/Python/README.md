This material appears in sections 5 to 7.

## Subdirectories:
- `evaluation`: contains files that are produced in the `notebooks/textmining.ipynb` notebook that required manual annotation or evaluation.
- `files`: contains files that are used as an input to the notebooks in `notebooks/`
- `notebooks`: contains all Python scripts that were created in sections 5-7
- `output`: contains the output files that were generated in the `notebooks/textmining.ipynb` notebook


## Scripts:
- `notebooks/preprocessing.ipynb`: Section 5.1.1
- `notebooks/textmining.ipynb`: Section 5.3 and Section 6
- `notebooks/definitions.ipynb`: Section 7
- `notebooks/json.ipynb`: Section 7 


## Files:

In `files/`:
- `compounds_info:csv`: output of the `notebooks/preprocessing.ipynb` notebook. Contains the list of compounds and the associated word forms and lemmas
- `wordlist.txt`: list of glossary terms 

In `evaluation/`:
- `compounds_sentiment.csv`: manual annotation of the sentiment scores which were used to obtain the connotation of terms
- `con_sentiment_diff_manual.csv`: manual annotation of the C2022 compounds that obtained different sentiment scores from the two sentiment models
- `pro_sentiment_diff_manual.csv`: manual annotation of the P2022 compounds that obtained different sentiment scores from the two sentiment models
- `concept_manual`: manual annotation of the categories for the `persons` and `group` compounds (see paper section 5.3.4.1)
- `attr_manual.csv`: manual annotation of attribution for a sample of compounds (see section 6)
- `declension_forms.csv`: manual annotated declension forms, used for `notebooks/preprocessing.ipynb` notebook. 
- - `persons_cleaned.csv`: table of unique person entities that were cleaned manually
- `organisations_cleaned.csv`: table of unique organisation entities that were cleaned manually


In `output/`:
- `knowledge_base.csv`: final knowledge base of all glossary terms
- `con_info.csv`: contains the contexts of all compounds occuring in the C2022 corpus and the output of the text mining methods that were applied to it. 
- `pro_info.csv`: contains the contexts of all compounds occuring in the P2022 corpus and the output of the text mining methods that were applied to it. 
- `nouns_sim.csv`: contains the matrix of compound nouns and the similarity scores computed via `PATH` metric (see paper section 5.3.4.2)
- `nouns_wup.csv`: contains the matrix of compound nouns and the similarity scores computed via `PATH` metric (see paper section 5.3.4.2)



put to evaluation: 

- full_sample_manual --> attr_manual 


TO DELETE:
- `con_sentiment.csv`: contains the compounds of C2022 for which we manually evaluate the polarity labels (see paper section 5.3.3)
- `pro_sentiment.csv`: contains the compounds of P2022 for which we manually evaluate the polarity labels (see paper section 5.3.3)
- `persons.txt`: list of unique person entities that were cleaned manually
- `organisations.txt`: list of unique organisation entities that were cleaned manually