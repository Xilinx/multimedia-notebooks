#   Copyright (C) 2023, Advanced Micro Devices, Inc. All rights reserved.
#   SPDX-License-Identifier: MIT

class common_vdu_demo_decode_display:
    def cmd_line_args_generator(INPUT_FILE_PATH, INPUT_URL, CODEC_TYPE, AUDIO_CODEC, DISPLAY_DEVICE, SHOW_FPS, LOOP_VIDEO, INTERNAL_ENTROPY_BUFFERS, PROXY_SERVER_URL, AUDIO_SINK, AUDIO_OUTPUT, SINK_NAME, DEC_INSTANCE):
        CMD_LINE_ARGS = []
        if(len(INPUT_FILE_PATH) != 0):
        	CMD_LINE_ARGS.append('-i')
        	CMD_LINE_ARGS.append(INPUT_FILE_PATH)
        if(len(INPUT_URL) != 0):
        	CMD_LINE_ARGS.append('-u')
        	CMD_LINE_ARGS.append(INPUT_URL)
        if(len(INPUT_FILE_PATH) == 0 and len(INPUT_URL) == 0):
        	CMD_LINE_ARGS.append('-i')
        	CMD_LINE_ARGS.append("/usr/share/movies/bbb_sunflower_2160p_30fps_normal.mp4")
        if(len(CODEC_TYPE) != 0):
        	CMD_LINE_ARGS.append('-c')
        	CMD_LINE_ARGS.append(CODEC_TYPE)
        if(AUDIO_CODEC != 'none'):
        	CMD_LINE_ARGS.append('-a')
        	CMD_LINE_ARGS.append(AUDIO_CODEC)
        if(DISPLAY_DEVICE == 'DP'):
            CMD_LINE_ARGS.append('-d')
            DISPLAY_DEVICE = 'fd4a0000.display'
            CMD_LINE_ARGS.append(DISPLAY_DEVICE)
        elif(DISPLAY_DEVICE == 'HDMI'):
            CMD_LINE_ARGS.append('-d')
            DISPLAY_DEVICE = 'a0070000.v_mix'
            CMD_LINE_ARGS.append(DISPLAY_DEVICE)
        if(SHOW_FPS == 1):
        	CMD_LINE_ARGS.append('-f')
        if(LOOP_VIDEO == 1):
        	CMD_LINE_ARGS.append('-l')
        if(INTERNAL_ENTROPY_BUFFERS != '5'):
        	CMD_LINE_ARGS.append('-e')
        	CMD_LINE_ARGS.append(INTERNAL_ENTROPY_BUFFERS)
        if(len(PROXY_SERVER_URL) != 0):
        	CMD_LINE_ARGS.append('-p')
        	CMD_LINE_ARGS.append(PROXY_SERVER_URL)
        if(AUDIO_SINK == 'pulsesink'):
        	CMD_LINE_ARGS.append('--use-pulsesink')
        elif(AUDIO_SINK == 'alsasink'):
        	CMD_LINE_ARGS.append('--use-alsasink')
        if(len(AUDIO_OUTPUT) != 0):
        	CMD_LINE_ARGS.append('--audio-output')
        	CMD_LINE_ARGS.append(AUDIO_OUTPUT)
        if(SINK_NAME != 'kmssink'):
        	CMD_LINE_ARGS.append('-o')
        	CMD_LINE_ARGS.append(SINK_NAME)
        if(len(DEC_INSTANCE) != 0):
                CMD_LINE_ARGS.append('-z')
                CMD_LINE_ARGS.append(DEC_INSTANCE)
        CMD_LINE_ARGS = " ".join(CMD_LINE_ARGS)
        print("sh common_vdu_demo_decode_display.sh", CMD_LINE_ARGS)
        return CMD_LINE_ARGS

class common_vdu_demo_streamin_decode_display:
    def cmd_line_args_generator(PORT_NUMBER, CODEC_TYPE, AUDIO_CODEC, DISPLAY_DEVICE, KERNEL_RECV_BUFFER_SIZE, SINK_NAME, INTERNAL_ENTROPY_BUFFERS, SHOW_FPS, AUDIO_SINK, DEC_INSTANCE):
        CMD_LINE_ARGS = []
        if(len(PORT_NUMBER) != 0):
                CMD_LINE_ARGS.append('-p')
                CMD_LINE_ARGS.append(PORT_NUMBER)
        if(len(CODEC_TYPE) != 0):
                CMD_LINE_ARGS.append('-c')
                CMD_LINE_ARGS.append(CODEC_TYPE)
        if(AUDIO_CODEC != 'none'):
                CMD_LINE_ARGS.append('-a')
                CMD_LINE_ARGS.append(AUDIO_CODEC)
        if(DISPLAY_DEVICE == 'DP'):
            CMD_LINE_ARGS.append('-d')
            DISPLAY_DEVICE = 'fd4a0000.display'
            CMD_LINE_ARGS.append(DISPLAY_DEVICE)
        elif(DISPLAY_DEVICE == 'HDMI'):
            CMD_LINE_ARGS.append('-d')
            DISPLAY_DEVICE = 'a0070000.v_mix'
            CMD_LINE_ARGS.append(DISPLAY_DEVICE)
        if(len(KERNEL_RECV_BUFFER_SIZE) != 0):
                CMD_LINE_ARGS.append('-b')
                CMD_LINE_ARGS.append(KERNEL_RECV_BUFFER_SIZE)
        if(SINK_NAME != 'kmssink'):
                CMD_LINE_ARGS.append('-o')
                CMD_LINE_ARGS.append(SINK_NAME)
        if(INTERNAL_ENTROPY_BUFFERS != '5'):
                CMD_LINE_ARGS.append('-e')
                CMD_LINE_ARGS.append(INTERNAL_ENTROPY_BUFFERS)
        if(SHOW_FPS == 1):
                CMD_LINE_ARGS.append('-f')
        if(AUDIO_SINK == 'pulsesink'):
                CMD_LINE_ARGS.append('--use-pulsesink')
        elif(AUDIO_SINK == 'alsasink'):
                CMD_LINE_ARGS.append('--use-alsasink')
        if(len(DEC_INSTANCE) != 0):
                CMD_LINE_ARGS.append('-z')
                CMD_LINE_ARGS.append(DEC_INSTANCE)
        CMD_LINE_ARGS = " ".join(CMD_LINE_ARGS)
        print("sh common_vdu_demo_streamin_decode_display.sh", CMD_LINE_ARGS)
        return CMD_LINE_ARGS
