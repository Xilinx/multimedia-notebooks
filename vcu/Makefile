#VCU notebooks target installs
install_vcu_notebooks:
	install -d ${D}/${JUPYTER_DIR}/vcu-notebooks
	install -d ${D}/${JUPYTER_DIR}/vcu-notebooks/pictures
	install -m 0755 gstreamer-vcu-notebooks/pictures/*.png ${D}/${JUPYTER_DIR}/vcu-notebooks/pictures
	install -m 0755 gstreamer-vcu-notebooks/common.py ${D}/${JUPYTER_DIR}/vcu-notebooks/common.py
	install -m 0755 gstreamer-vcu-notebooks/*.ipynb ${D}/${JUPYTER_DIR}/vcu-notebooks
	
#VCU examples target installs
install_vcu_examples:
	install -d ${D}/${bindir}
	install -d ${D}/${datadir}/applications
	install -m 0755 gstreamer-vcu-examples/4K_AVC_Decode.desktop ${D}/${datadir}/applications
	install -m 0755 gstreamer-vcu-examples/4K_HEVC_Decode.desktop ${D}/${datadir}/applications
	install -m 0755 gstreamer-vcu-examples/VCU_Examples_ReadMe.desktop ${D}/${datadir}/applications
	install -m 0755 gstreamer-vcu-examples/VCU-Examples-ReadMe.txt ${D}/${bindir}
	install -m 0755 gstreamer-vcu-examples/vcu-demo-camera-decode-display.sh ${D}/${bindir}
	install -m 0755 gstreamer-vcu-examples/vcu-demo-camera-encode-decode-display.sh ${D}/${bindir}
	install -m 0755 gstreamer-vcu-examples/vcu-demo-camera-encode-file.sh ${D}/${bindir}
	install -m 0755 gstreamer-vcu-examples/vcu-demo-camera-encode-streamout.sh ${D}/${bindir}
	install -m 0755 gstreamer-vcu-examples/vcu-demo-decode-display.sh ${D}/${bindir}
	install -m 0755 gstreamer-vcu-examples/vcu-demo-streamin-decode-display.sh ${D}/${bindir}
	install -m 0755 gstreamer-vcu-examples/vcu-demo-transcode-to-file.sh ${D}/${bindir}
	install -m 0755 gstreamer-vcu-examples/vcu-demo-transcode-to-streamout.sh ${D}/${bindir}
	install -m 0755 gstreamer-vcu-examples/vcu-demo-videotestsrc-hdr-to-file.sh ${D}/${bindir}
	install -m 0755 gstreamer-vcu-examples/vcu-demo-functions.sh ${D}/${bindir}
