### INITIATE STRING BASES FOR EACH CATEGORY

str_base_info = """{COMPOUND}, {ARTICLE}\n"""

str_base_pers = """Der Begriff '{COMPOUND}' bezeichnet eine Person, die in einer gewissen Beziehung zum Klimawandel steht. '{COMPOUND}' wird in unserem Korpus {CON_FREQ} Mal von den Klimaforschungsskeptikern und {PRO_FREQ} Mal von den Klimaforschungsvertretern verwendet. Auf den gesamten Korpus gesehen entspricht das einer relativen Häufigkeit (TF-IDF) von {CON_TFIDF} für die Skeptiker und {PRO_TFIDF} für die Vertreter.""" 

str_base_loc = """Der Begriff '{COMPOUND}' wird in unserem Korpus {CON_FREQ} Mal von den Klimaforschungsskeptikern und {PRO_FREQ} Mal von den Klimaforschungsvertretern verwendet. Auf den gesamten Korpus gesehen entspricht das einer relativen Häufigkeit (TF-IDF) von {CON_TFIDF} für die Skeptiker und {PRO_TFIDF} für die Vertreter.""" 

str_base_action = """Der Begriff '{COMPOUND}' wird in unserem Korpus {CON_FREQ} Mal von den Klimaforschungsskeptikern und {PRO_FREQ} Mal von den Klimaforschungsvertretern verwendet. Auf den gesamten Korpus gesehen entspricht das einer relativen Häufigkeit (TF-IDF) von {CON_TFIDF} für die Skeptiker und {PRO_TFIDF} für die Vertreter.""" 

str_base_abstract = """Der Begriff '{COMPOUND}' wird in unserem Korpus {CON_FREQ} Mal von den Klimaforschungsskeptikern und {PRO_FREQ} Mal von den Klimaforschungsvertretern verwendet. Auf den gesamten Korpus gesehen entspricht das einer relativen Häufigkeit (TF-IDF) von {CON_TFIDF} für die Skeptiker und {PRO_TFIDF} für die Vertreter.""" 

str_base_group = """Der Begriff '{COMPOUND}' bezeichnet einen Zusammenschluss von Personen im Bezug auf den Klimawandel. '{COMPOUND}' wird in unserem Korpus {CON_FREQ} Mal von den Klimaforschungsskeptikern und {PRO_FREQ} Mal von den Klimaforschungsvertretern verwendet. Auf den gesamten Korpus gesehen entspricht das einer relativen Häufigkeit (TF-IDF) von {CON_TFIDF} für die Skeptiker und {PRO_TFIDF} für die Vertreter.""" 

# INITIATE STRINGS THAT ARE EQUAL FOR ALL CATEGORIES

str_sent =  """ In unserem Korpus Sample ist der Begriff tendenziell {SENTIMENT} konnotiert."""

str_attr = """ Verwendet wird '{COMPOUND}' hierbei im Sinne einer {ATTRIBUTION}"""

str_sarcasm = """ Die Verwendung wird {SARCASM} als sarkastisch eingestuft."""

str_mods_pro = """ Im Subdiskurs der Klimaforschungsvertreter wird der Begriff von Wörtern wie {PRO_MODS} modifiziert.""" 
str_mods_con = """ Wörter wie {CON_MODS} treten auf, um den Begriff im Subdiskurs der Klimaforschungsskeptiker näher zu beschreiben.""" 

str_pers = """ Im Zusammenhang mit dem Begriff erwähnt"""
str_pers_con = """ der Skeptiker Korpus die Person(en) {CON_PERS}"""
str_pers_pro = """ der Vertreter Korpus die Person(en) {PRO_PERS}"""

str_org = """ Im Kontext von '{COMPOUND}' erfolgt die Nennung folgender Organisation(en):"""

str_org_con = """ {CON_ORG} (Skeptiker Korpus)"""
str_org_pro = """ {PRO_ORG} (Vertreter Korpus)"""  

str_colls = """\n\nKollokationen: {CON_COLLS}{PRO_COLLS}"""
str_simwords = """\n\nSiehe auch: {SIMILAR_WORDS}"""