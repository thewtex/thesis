# makefile for rendering documents from ReStructured Text
#

BIB4TXT=bib4txt.py
IMGMATHHACK=formatting/imgmathhack.py
RST2ODT=rst2odt.py
UNOCONV=unoconv

STYLESODT=styles.odt
STYLESODTPATH=formatting/$(STYLESODT)

BACK_PRE=introduction/background_and_significance

all: $(BACK_PRE).odt

$(BACK_PRE)_w_math.rst: $(BACK_PRE).rst 
	$(IMGMATHHACK) $(BACK_PRE).rst $(BACK_PRE)_w_math.rst

# add '-s example_numbered' for numbered references instead of last names
$(BACK_PRE)_w_cite.rst: $(BACK_PRE)_w_math.rst $(BACK_PRE).bib
	PYTHONPATH='./formatting' $(BIB4TXT) --all -i $(BACK_PRE)_w_math.rst -no $(BACK_PRE)_w_cite.rst $(BACK_PRE).bib

$(BACK_PRE).odt: $(BACK_PRE)_w_cite.rst $(STYLESODTPATH)
	$(RST2ODT) --stylesheet=$(STYLESODTPATH) $(BACK_PRE)_w_cite.rst $(BACK_PRE).odt

$(BACK_PRE).doc: $(BACK_PRE).odt
	$(UNOCONV) -f doc $(BACK_PRE).odt

clean:
	rm -f $(shell find . -name '*.doc' -or -name '*.odt' -not -name $(STYLESODT) -or -name '*_w_cite.rst' -or -name '*_w_math.rst') mti* imgmath/*
