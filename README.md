# README- multimedia-notebooks


This README provides step-by-step instructions on how to start a server, client, and an example for `gstreamer-vcu` and `gstreamer-vdu` notebooks.
 

## Getting Started 

1. After booting the board with images containing `gstreamer-vcu` notebooks and examples, and `gstreamer-vdu` notebooks and examples, open a terminal window.

2. To start the JUPYTER notebooks UI, run the following script in the terminal:

    -$ /sbin/start-jupyter.sh

3. The script's output will include information about the notebook server, including a URL. Copy the URL displayed in the terminal.

4. Open a web browser and paste the copied URL into the address bar.


## Accessing Notebooks

1. In the browser, you will see two folders:

- `vcu-notebooks`

- `vdu-notebooks`

2. Open the desired folder and click on the `.ipynb` file to access and interact with the notebooks. 

## Example Usage

### VDU Notebooks

1. Inside the `vdu-notebooks` folder, you will find the following files:

- `vdu-demo-decode-display.ipynb`

- `vdu-demo-streamin-decode-display.ipynb`

- `common.py`
 

**Note: VDU currently supports two use cases:**

- File playback use case

- Streaming decode display use case


**Eg:**

1. To run a specific use case:

   a. Open the `vdu-notebooks` folder.

   b. Click on the `.ipynb` file corresponding to the desired use case (e.g., `vdu-demo-decode-display.ipynb`).

2. The notebook will open with the selected use case, such as "DECODE -> FAKESINK UI."

3. In the notebook:

   - Explore the Video Decode Unit (VDU) Demo Example: DECODE -> FAKESINK UI.

   - Review the board setup and implementation details of functionalities.

   - Click on the "Restart kernel" button to prepare for running the demo. 

4. Run the demo:

   a. Provide the appropriate path for the file/URL.

   b. Select the Video Codec settings, including codec type (avc/hevc), Video Sink, Display, and Decoder Instance.

   c. To add multiple instances, click "Add more decoder" and repeat the steps for Video Codec settings.

5. Advanced options are available to select the Entropy Buffer, show FPS, and enable Repeat play.

6. After configuring the settings, click "click to start vdu-decode-display demo" to initiate the demo.

   - The pipeline and running status of the use case will be displayed.

   - To clear the output, click "Clear output."

 
### VCU Notebooks

1. Similar to VDU, inside the `vcu-notebooks` folder, you will find various `.ipynb` files for different VCU use cases.

2. Some of the advanced settings available in VCU notebooks include resolutions settings in Video Codec, audio codec settings, and more advanced options settings.


## Additional Information

Examples and further details can be found inside the `vdu/Readme.txt` file for VDU, and the `vcu/Readme.txt` file for VCU.


