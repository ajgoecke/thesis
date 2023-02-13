# Implementation in Python

This material appears in sections 5 to 7.

## Subdirectories:
- `evaluation`: contains files that are produced in the `notebooks/textmining.ipynb` notebook that required manual annotation or evaluation.
- `files`: contains files that are used as an input to the notebooks in `notebooks/`.
- `notebooks`: contains all Python scripts that were created in sections 5-7.
- `output`: contains the output files that were generated in the `notebooks/textmining.ipynb` notebook.


## Scripts:
- `notebooks/preprocessing.ipynb`: notebook containing the implementation of the preprocessing of the compound words (see paper section 5.1.1).
- `notebooks/textmining.ipynb`: notebook containing the implementation of the text mining methods (see paper section 5.3 and section 6).
- `notebooks/definitions.ipynb`: notebook containing the implementation of the definition phrasing (see paper section 7).
- `notebooks/json.ipynb`: notebook containing the implementation of the final definitions into the json file of the glossary (see paper section 7).
- `notebooks/definition_strings.py`: Python script that contains the definition strings that are used to phrase the final definitions (see paper section 7).


## Files:

In `files/`:
- `compounds_info:csv`: output of the `notebooks/preprocessing.ipynb` notebook. Contains the list of compounds and the associated word forms and lemmas.
- `wordlist.txt`: list of glossary terms.

In `evaluation/`:
- `compounds_sentiment.csv`: manual annotation of the sentiment scores which were used to obtain the connotation of terms.
- `con_sentiment_diff_manual.csv`: manual annotation of the C2022 compounds that obtained different sentiment scores from the two sentiment. models
- `pro_sentiment_diff_manual.csv`: manual annotation of the P2022 compounds that obtained different sentiment scores from the two sentiment. models
- `concept_manual`: manual annotation of the categories for the `persons` and `group` compounds (see paper section 5.3.4.1).
- `attr_manual.csv`: manual annotation of attribution for a sample of compounds (see section 6)
- `declension_forms.csv`: manual annotated declension forms, used for `notebooks/preprocessing.ipynb` notebook. 
- `persons_cleaned.csv`: table of unique person entities that were cleaned manually.
- `organisations_cleaned.csv`: table of unique organisation entities that were cleaned manually.
- `sentiment_comparison.csv`: table of sentiment labels for each model and discourse group and comparison of the results.

In `output/`:
- `knowledge_base.csv`: final knowledge base of all glossary terms.
- `info.zip`: zip file that contains `con_info.csv` and `pro_info.csv` (since those files were to big to be pushed onto GitHub. Please unzip first to be able to fully run all Python notebooks in `notebooks`. 
- `con_info.csv`: contains the contexts of all compounds occuring in the C2022 corpus and the output of the text mining methods that were applied to it. 
- `pro_info.csv`: contains the contexts of all compounds occuring in the P2022 corpus and the output of the text mining methods that were applied to it. 
- `nouns_sim.csv`: contains the matrix of compound nouns and the similarity scores computed via `PATH` metric (see paper section 5.3.4.2).
- `nouns_wup.csv`: contains the matrix of compound nouns and the similarity scores computed via `PATH` metric (see paper section 5.3.4.2).


## Requirements
To be able to fully run all the notebooks, please make sure the following libraries are installed:
- `pandas`: version 1.3.4 https://pandas.pydata.org/docs/
- `german-nouns`: version 1.2.1 https://github.com/gambolputty/german-nouns
- `wordnet`: version 0.9.1 https://wn.readthedocs.io/en/latest/
- `spacy`: version 3.3.1 https://spacy.io
- `german bert`: version 1.0.7 https://huggingface.co/oliverguhr/german-sentiment-bert
- `numpy`: version 1.23.1 https://numpy.org
- `textblob-de`: version 0.4.3 https://textblob-de.readthedocs.io/en/latest/ 
- `requests`: version 2.26.0 https://requests.readthedocs.io/en/latest/
- `wn`: version 0.9.1 https://wn.readthedocs.io/en/latest/
- `tabulate`: version 0.8.10 https://github.com/astanin/python-tabulate
- `pathlib2`: version 2.3.6 https://github.com/jazzband/pathlib2
- `matplotlib`: version 3.4.3 https://matplotlib.org
- `nltk`: version 3.6.5 https://www.nltk.org