APPNAME = cdi_track
TGTDIR = /usr/local/bin

MAIN = main.py
OTHERS = cdi_tracker.py cdi_tracker_utils.py

install: $(OTHERS)
	pip install -r requirements.txt
	chmod +x src/$(MAIN)
	cp src/$(MAIN) $(TGTDIR)/$(APPNAME)

cdi_tracker.py:
	cp src/cdi_tracker.py $(TGTDIR)

cdi_tracker_utils.py:
	cp src/cdi_tracker_utils.py $(TGTDIR)


uninstall:
	rm $(TGTDIR)/$(APPNAME)
	rm $(TGTDIR)/cdi_tracker.py
	rm $(TGTDIR)/cdi_tracker_utils.py
	echo "CDI_Track has been uninstalled."
