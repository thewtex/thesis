# makefile for rendering documents from ReStructured Text
#

BIB4TXT=bib4txt.py
RST2ODT=rst2odt.py
UNOCONV=unoconv

all: background_odt


BACK_PRE=introduction/background_and_significance
background: $(BACK_PRE).rst
	$(BIB4TXT) --all -i $(BACK_PRE).rst -no $(BACK_PRE)_w_cite.rst $(BACK_PRE).bib

background_odt: background
	$(RST2ODT) --stylesheet=styles.odt $(BACK_PRE)_w_cite.rst $(BACK_PRE).odt

background_doc: background_odt
	$(UNOCONV) -f doc $(BACK_PRE).odt
