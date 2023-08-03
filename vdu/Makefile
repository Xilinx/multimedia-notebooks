#VDU notebooks target installs
install_vdu_notebooks:
	install -d ${D}/${JUPYTER_DIR}/vdu-notebooks
	install -d ${D}/${JUPYTER_DIR}/vdu-notebooks/pictures
	install -m 0755 gstreamer-vdu-notebooks/pictures/*.png ${D}/${JUPYTER_DIR}/vdu-notebooks/pictures
	install -m 0755 gstreamer-vdu-notebooks/common.py ${D}/${JUPYTER_DIR}/vdu-notebooks/common.py
	install -m 0755 gstreamer-vdu-notebooks/*.ipynb ${D}/${JUPYTER_DIR}/vdu-notebooks

#VDU examples target installs
install_vdu_examples:	
	install -d ${D}/${bindir}
	install -d ${D}/${datadir}/applications
	install -m 0755 gstreamer-vdu-examples/VDU_Examples_ReadMe.desktop ${D}/${datadir}/applications
	install -m 0755 gstreamer-vdu-examples/VDU-Examples-ReadMe.txt ${D}/${bindir}
	install -m 0755 gstreamer-vdu-examples/vdu-demo-decode-display.sh ${D}/${bindir}
	install -m 0755 gstreamer-vdu-examples/vdu-demo-functions.sh ${D}/${bindir}
	install -m 0755 gstreamer-vdu-examples/vdu-demo-streamin-decode-display.sh ${D}/${bindir}
