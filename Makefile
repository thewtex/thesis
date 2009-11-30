# makefile for rendering documents from ReStructured Text
#

BIB4TXT=bib4txt.py
IMGMATHHACK=formatting/imgmathhack.py
ODTRESPACE=odt-respace
RST2ODT=rst2odt.py
UNOCONV=unoconv

STYLESODT=styles.odt
STYLESODTPATH=formatting/$(STYLESODT)

BACK_PRE=introduction/background_and_significance

all: $(BACK_PRE).doc

$(BACK_PRE)_w_math.rst: $(BACK_PRE).rst 
	$(IMGMATHHACK) $(BACK_PRE).rst $(BACK_PRE)_w_math.rst

# add '-s example_numbered' for numbered references instead of last names
$(BACK_PRE)_w_cite.rst: $(BACK_PRE)_w_math.rst $(BACK_PRE).bib
	PYTHONPATH='./formatting' $(BIB4TXT) --all -i $(BACK_PRE)_w_math.rst -no $(BACK_PRE)_w_cite.rst $(BACK_PRE).bib

# this is a hack for something broken in bibstuff, maybe in the ebnf grammar in
# bibgrammar.py.  No time to fix it now.
$(BACK_PRE)_w_cite_fix.rst: $(BACK_PRE)_w_cite.rst
	sed -e 's/AmericanHeartAssociation/American Heart Association/g' -e "s/AmericanAlzheimer'sAssociation/American Alzheimer's Association/g" $(BACK_PRE)_w_cite.rst > $(BACK_PRE)_w_cite_fix.rst

$(BACK_PRE).odt: $(BACK_PRE)_w_cite_fix.rst $(STYLESODTPATH)
	$(RST2ODT) --stylesheet=$(STYLESODTPATH) $(BACK_PRE)_w_cite_fix.rst $(BACK_PRE).odt

$(BACK_PRE)_double_spaced.odt: $(BACK_PRE).odt
	$(ODTRESPACE) $(BACK_PRE).odt $(BACK_PRE)_double_spaced.odt

$(BACK_PRE).doc: $(BACK_PRE)_double_spaced.odt
	$(UNOCONV) -f doc $(BACK_PRE)_double_spaced.odt 
	mv $(BACK_PRE)_double_spaced.doc $(BACK_PRE).doc

clean:
	rm -f $(shell find . -name '*.doc' -or -name '*.odt' -not -name $(STYLESODT) -or -name '*_w_cite.rst' -or -name '*_w_math.rst' | grep -v doc_edits ) mti* imgmath/*
