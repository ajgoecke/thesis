### INITIATE STRING BASES FOR EACH CATEGORY

str_base_info = """{COMPOUND}, {ARTICLE}\n"""

str_base_pers = """Der Begriff {COMPOUND} bezeichnet eine Person, die eine Haltung zum Klimawandel einnimmt. Der Begriff wird in unserem Korpus {CON_FREQ} Mal von den Klimaforschungsskeptikern und {PRO_FREQ} Mal von den Klimaforschungsvertretern verwendet. Auf den gesamten Korpus gesehen entspricht das einer relativen Häufigkeit (TF-IDF) von {CON_TFIDF} für die Skeptiker und {PRO_TFIDF} für die Vertreter.""" 

str_base_loc = """Der Begriff {COMPOUND} bezeichnet eine Lokalität im Bezug auf den Klimawandel. Der Begriff wird in unserem Korpus {CON_FREQ} Mal von den Klimaforschungsskeptikern und {PRO_FREQ} Mal von den Klimaforschungsvertretern verwendet. Auf den gesamten Korpus gesehen entspricht das einer relativen Häufigkeit (TF-IDF) von {CON_TFIDF} für die Skeptiker und {PRO_TFIDF} für die Vertreter.""" 

str_base_action = """Der Begriff {COMPOUND} bezeichnet eine Aktion im Bezug auf den Klimawandel. Der Begriff wird in unserem Korpus {CON_FREQ} Mal von den Klimaforschungsskeptikern und {PRO_FREQ} Mal von den Klimaforschungsvertretern verwendet. Auf den gesamten Korpus gesehen entspricht das einer relativen Häufigkeit (TF-IDF) von {CON_TFIDF} für die Skeptiker und {PRO_TFIDF} für die Vertreter.""" 

str_base_abstract = """Der Begriff {COMPOUND} bezeichnet ein Konzept in Relation zum Klimawandel. Der Begriff wird in unserem Korpus {CON_FREQ} Mal von den Klimaforschungsskeptikern und {PRO_FREQ} Mal von den Klimaforschungsvertretern verwendet. Auf den gesamten Korpus gesehen entspricht das einer relativen Häufigkeit (TF-IDF) von {CON_TFIDF} für die Skeptiker und {PRO_TFIDF} für die Vertreter.""" 

str_base_group = """Der Begriff {COMPOUND} bezeichnet einen Zusammenschluss von Personen im Bezug auf den Klimawandel. Der Begriff wird in unserem Korpus {CON_FREQ} Mal von den Klimaforschungsskeptikern und {PRO_FREQ} Mal von den Klimaforschungsvertretern verwendet. Auf den gesamten Korpus gesehen entspricht das einer relativen Häufigkeit (TF-IDF) von {CON_TFIDF} für die Skeptiker und {PRO_TFIDF} für die Vertreter.""" 

# INITIATE STRINGS THAT ARE EQUAL FOR ALL CATEGORIES

str_sent =  """ In unserem Korpus Sample ist der Begriff tendenziell {SENTIMENT} konnotiert."""

#str_attr_con = """ Hierbei wird „{COMPOUND}“ von Seiten der Skeptiker im Sinne einer {CON_ATTRIBUTION}""" #(verwendet)
#str_attr_pro = """ und von Vertretern als {PRO_ATTRIBUTION} verwendet."""

str_attr = """ Verwendet wird "{COMPOUND}" hierbei im Sinne einer {ATTRIBUTION}"""
str_sarcasm = """ In {SARCASM}"""

str_mods_pro = """ Im Subdiskurs der Klimaforschungsvertreter wird der Begriff von Wörtern wie {PRO_MODS} modifiziert.""" 
str_mods_con = """ Modifizierer wie {CON_MODS} treten häufig auf, um den Begriff im Subdiskurs der Klimaforschungsskeptiker näher zu beschreiben.""" 

str_pers = """ Im Zusammenhang mit dem Begriff erwähnt der Skeptiker Korpus die Person(en)"""
str_pers_con = """ {CON_PERS}"""
str_pers_pro = """ der Vertreter Korpus {PRO_PERS}"""
#str_pers_con = """ Im Zusammenhang mit dem Begriff erwähnt der Skeptiker Korpus die Person(en) {CON_PERS}"""
#str_pers_pro = """ und der Vertreter Korpus die Person(en) {PRO_PERS}."""

str_org = """ Außerdem werden im Kontext von "{COMPOUND}" folgende Organisationen genannt: """
str_org_con = """ {CON_ORG} (Skeptiker Korpus)"""
#str_org_con = """ Außerdem werden im Kontext von "{COMPOUND}" folgende Organisationen genannt: {CON_ORG} (Skeptiker Korpus)"""
str_org_pro = """ {PRO_ORG} (Vertreter Korpus)"""  
#str_org_pro2 = """ Außerdem werdem im Kontext von "{COMPOUN

str_colls = """\nHäufige Kollokationen: {CON_COLLS}{PRO_COLLS}"""
str_simwords = """\n\nSiehe auch: {SIMILAR_WORDS}"""