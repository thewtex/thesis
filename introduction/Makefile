# makefile for rendering documents from ReStructured Text
#

BIB4TXT=bib4txt.py
IMGMATHHACK=../formatting/imgmathhack.py
ODTRESPACE=odt-respace
RST2ODT=rst2odt.py
UNOCONV=unoconv

STYLESODT=styles.odt
STYLESODTPATH=../formatting/$(STYLESODT)

PAPER=background_and_significance

all: $(PAPER).doc

$(PAPER)_w_math.rst: $(PAPER).rst
	$(IMGMATHHACK) $(PAPER).rst $(PAPER)_w_math.rst

# add '-s example_numbered' for numbered references instead of last names
$(PAPER)_w_cite.rst: $(PAPER)_w_math.rst $(PAPER).bib
	PYTHONPATH='../formatting' $(BIB4TXT) -s my_numbered --all -i $(PAPER)_w_math.rst -no $(PAPER)_w_cite.rst $(PAPER).bib

# this is a hack for something broken in bibstuff, maybe in the ebnf grammar in
# bibgrammar.py.  No time to fix it now.
$(PAPER)_w_cite_fix.rst: $(PAPER)_w_cite.rst
	sed -e 's/AmericanHeartAssociation/American Heart Association/g' -e "s/AmericanAlzheimer'sAssociation/American Alzheimer's Association/g" $(PAPER)_w_cite.rst > $(PAPER)_w_cite_fix.rst

$(PAPER).odt: $(PAPER)_w_cite_fix.rst $(STYLESODTPATH)
	$(RST2ODT) --stylesheet=$(STYLESODTPATH) $(PAPER)_w_cite_fix.rst $(PAPER).odt

$(PAPER)_double_spaced.odt: $(PAPER).odt
	$(ODTRESPACE) $(PAPER).odt $(PAPER)_double_spaced.odt

$(PAPER).doc: $(PAPER)_double_spaced.odt
	$(UNOCONV) -f doc $(PAPER)_double_spaced.odt
	mv $(PAPER)_double_spaced.doc $(PAPER).doc

clean:
	rm -f $(shell find . -name '*.doc' -or -name '*.odt' -not -name $(STYLESODT) -or -name '*_w_cite.rst' -or -name '*_w_math.rst' | grep -v doc_edits ) mti* imgmath/*
