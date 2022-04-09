import subprocess
import os

# The operations provided by user shall be seperated by comma
# which is followed by a space ', '. Example provided below:
# Change Bitrate, Convert MP4 to HLS, Change Frame Rate, Trimming

# Operations that can be entered in the command line:
# Trimming, Reverse Video, Change aspect ratio,Change Bitrate, Change Frame Rate,
# Change Frame Size, Mute Audio, Get Details, Remove Video, Convert MP4 to HLS


ffmpeg_path = r"C:\Users\bokad\Downloads\ffmpeg-n5.0-latest-win64-lgpl-5.0\bin\ffmpeg.exe"
input_file_path = r"D:\Xunison\xuni\samplevideo.mp4"
output_path = f'{os.path.dirname(os.path.abspath(input_file_path))}'
# check_input = os.path.exists(input_file_path) # alternative to check input file
ffprobe_path = r"C:\Users\bokad\Downloads\ffmpeg-n5.0-latest-win64-lgpl-5.0\bin\ffprobe.exe"

class Processing():
    """This class uses ffmpeg to transcode the input video as required.

    The input file provided to the methods should be a mp4 video file.

    Every method of this class creates a new transcoded video file as
    output according to it's respective functionality. The transcoded
    file is created as .mp4 which is a common container format for video
    files that allows you to store video and audio information.

    -y added after ffmpeg path to overwrite an existing file having
    same name as that of the output file.

    Methods
    -------
    trim_video()
        Generates a trimmed subpart of the input video
    change_aspect_ratio()
        Creates a new video file with aspect ratio 1:1 
    change_bitrate()
        Makes a new video file having birate of video-118kB/s and audio-250kB/s
    change_frame_rate()
        Creates a new video file having frame rate of 13 fps
    change_frame_size()
        Creates a new video file maintaining frame size of 180x120 px
    mute_audio()
        Generates a new muted video file
    remove_video()
        Makes a new video file containingno video 
    mp4_to_HLS()
        Creates a HTTP live stream file (.m3u8) along with the segment file(s)
    reverse_audio_video()
        Produces a copy of input file in reversed manner
    get_video_details()
        Prints detailed meta data of the input file.
    """

    # Added exception handling to each method as they can be executed individually

    @staticmethod
    def trim_video():
        """Trims the input so that the output contains one continuous subpart
        of the input. The trimming starts at 30 seconds of the input video.
        The duration of subpart (video) obtained is 1 minute.
        retuns message on completion of the transcoding.
        """
        output_file = output_path + '\\trimmed_video.mp4'

        # subprocess module allows to connect with the input and output files.
        # Popen takes string as a command to be executed in the command prompt.
        # stdout specifies the executed programs' standard output and
        # stderr specifies the standard error file handles.
        try:
            p1 = subprocess.Popen(
                f'{ffmpeg_path} -y -i {input_file_path} -ss 00:00:30 -t 00:01:00 -c:v copy -c:a copy {output_file}',
                stderr=subprocess.STDOUT, stdout=subprocess.PIPE)

        # improper ffmpeg path will throw FileNotFoundError
        except FileNotFoundError:   
            return("Could not locate ffmpeg. Make sure the path is correct")

        print("Processing...")

        # Checking for "No such file or directory" message from cmd
        # in case the input_file_path is invalid.
        check_error = p1.stdout.readlines()[10].decode("utf-8")     
        if "No such file or directory" in check_error:
            return "Unable to locate the file or directory"
        return "Video trimmed successfully!"


    @staticmethod
    def change_aspect_ratio():
        """Changes the aspect ratio of the input video file. The output frames
        will always have a aspect ratio of 1:1.
        retuns message on completion of the transcoding.
        """
        output_file = output_path + '\\changed_aspect_ratio_video.mp4'

        try:
            p1 = subprocess.Popen(
                f'{ffmpeg_path} -y -i {input_file_path} -aspect 1:1 {output_file}',
                stderr=subprocess.STDOUT, stdout=subprocess.PIPE)
        except FileNotFoundError:
            return("Could not locate ffmpeg. Make sure the path is correct")
        print("Processing...")
        check_error = p1.stdout.readlines()[10].decode("utf-8")
        if "No such file or directory" in check_error:
            return "Unable to locate the file or directory"
        return "Aspect ratio changed successfully!"


    @staticmethod
    def change_bitrate():
        """Changes the bitrate of the input video to 118 kB/s and the audio
        to 250 kB/s. Bitrate affects the quality of the video and audio.
        -b:v Specifies the average target output bitrate of the video
        -b:a Specifies the average target output bitrate of the audio
        """
        output_file = output_path + '\\changed_bitrate_video.mp4'
        try:
            p1 = subprocess.Popen(
                f'{ffmpeg_path} -y -i {input_file_path} -b:v 118K -b:a 250K {output_file}',
                stderr=subprocess.STDOUT, stdout=subprocess.PIPE)
        except FileNotFoundError:
            return("Could not locate ffmpeg. Make sure the path is correct")
        print("Processing...")
        check_error = p1.stdout.readlines()[10].decode("utf-8")
        if "No such file or directory" in check_error:
            return "Unable to locate the file or directory"
        return "Bitrate changed successfully!"



    @staticmethod
    def change_frame_rate():
        """Creates a new video file by changing the frame rate of input video.
        Frame rate of the new video which is created is 13 fps.
        """
        output_file = output_path + '\\changed_frame_rate_video.mp4'
        try:
            p1 = subprocess.Popen(
                f'{ffmpeg_path} -y -i {input_file_path} -r 13 {output_file}',
                stderr=subprocess.STDOUT, stdout=subprocess.PIPE)
        except FileNotFoundError:
            return("Could not locate ffmpeg. Make sure the path is correct")
        print("Processing...")
        check_error = p1.stdout.readlines()[10].decode("utf-8")
        if "No such file or directory" in check_error:
            return "Unable to locate the file or directory"        
        return "Frame rate changed successfully!"

    @staticmethod
    def change_frame_size():
        """Creates a new video file by changing the frame size of input video.
        Frame size of the new video which is created is 180x120 pixel.
        """
        output_file = output_path + '\\changed_frame_size_video.mp4'
        try:
            p1 = subprocess.Popen(
                f'{ffmpeg_path} -y -i {input_file_path} -vf scale=180:120 {output_file}',
                stderr=subprocess.STDOUT, stdout=subprocess.PIPE)
        except FileNotFoundError:
            return("Could not locate ffmpeg. Make sure the path is correct")
        print("Processing...")
        check_error = p1.stdout.readlines()[10].decode("utf-8")
        if "No such file or directory" in check_error:
            return "Unable to locate the file or directory"
        return "Frame size changed successfully!"


    @staticmethod
    def mute_audio():
        """This method duplicates the input video in a new video file but
        mutes the audio. The existence of audio is not altered i.e audio
        is not removed.
        """
        output_file = output_path + '\\muted_video.mp4'          
        try:
            p1 =subprocess.Popen(
                f'{ffmpeg_path} -y -i {input_file_path} -filter:a "volume=0" {output_file}',
                stderr=subprocess.STDOUT, stdout=subprocess.PIPE)
        except FileNotFoundError:
            return("Could not locate ffmpeg. Make sure the path is correct")
        print("Processing...")
        check_error = p1.stdout.readlines()[10].decode("utf-8")
        if "No such file or directory" in check_error:
            return "Unable to locate the file or directory"
        return "The video is muted successfully!"


    @staticmethod
    def remove_video():
        """Removes the video from the provided input file and creates an
        audio-only file.
        """
        output_file = output_path + '\\removed_video.mp4'
        try:
            p1 = subprocess.Popen(
                f'{ffmpeg_path} -y -i {input_file_path} -vn {output_file}',
                stderr=subprocess.STDOUT, stdout=subprocess.PIPE)
        except FileNotFoundError:
            return("Could not locate ffmpeg. Make sure the path is correct")
        print("Processing...")
        check_error = p1.stdout.readlines()[10].decode("utf-8")
        if "No such file or directory" in check_error:
            return "Unable to locate the file or directory"
        return "Video Removed successfully!"

    @staticmethod
    def mp4_to_HLS():
        """ Works by creating a HTTP Live Streaming (HLS) Master playlist
        as well as one or more segment files for the given input file. The
        name specified for the output file will be the name of the playlist
        (or .m3u8 file) while the .ts files will also be named after the
        playlist followed by a sequential number.

        The segment files created are of maximum duration of 25 seconds.
        """
        output_file = output_path + '\\http_live_stream.m3u8'
        try:
            p1 = subprocess.Popen(
                f'{ffmpeg_path} -y -i {input_file_path} -codec: copy -start_number 0 -hls_time 25 -hls_list_size 0 -f hls {output_file}',
                stderr=subprocess.STDOUT, stdout=subprocess.PIPE)
        except FileNotFoundError:
            return("Could not locate ffmpeg. Make sure the path is correct")
        print("Processing...")
        check_error = p1.stdout.readlines()[10].decode("utf-8")
        if "No such file or directory" in check_error:
            return "Unable to locate the file or directory"
        return "Converted to HLS successfully!"

    
    @staticmethod
    def reverse_audio_video():
        """This method reverses the input file and creates a new video.
        Both audio and video in the input file are reversed.
        """
        output_file = output_path + '\\reversed_video.mp4'          
        try:
            p1 = subprocess.Popen(
                f'{ffmpeg_path} -y -i {input_file_path} -vf reverse -af areverse {output_file}',
                stderr=subprocess.STDOUT, stdout=subprocess.PIPE)
        except FileNotFoundError:
            return("Could not locate ffmpeg. Make sure the path is correct")
        print("Processing...")
        check_error = p1.stdout.readlines()[10].decode("utf-8")
        if "No such file or directory" in check_error:
            return "Unable to locate the file or directory"
        return "The video is reversed successfully!"

    @staticmethod
    def get_video_details():
        """This method retrieves all the meta data from the input video file.
        It prints a detailed version of information in the command prompt.
        """

        try:
            p1 = subprocess.Popen(
                f'{ffprobe_path} -i {input_file_path}',
                stderr=subprocess.STDOUT, stdout=subprocess.PIPE)
        # improper ffprobe path will throw FileNotFoundError
        except FileNotFoundError:
            return("Could not locate ffprobe. Make sure the path is correct")
        print("Processing...")
        details = p1.stdout.read().decode("utf-8")
        return details

# Implementation of Switch case by using dictionary
operations_dict = {
    "trimming": Processing.trim_video,
    "change aspect ratio": Processing.change_aspect_ratio,
    "change bitrate": Processing.change_bitrate,
    "change frame rate": Processing.change_frame_rate,
    "change frame size": Processing.change_frame_size,
    "mute audio": Processing.mute_audio,
    "remove video": Processing.remove_video,
    "convert mp4 to hls": Processing.mp4_to_HLS,
    "reverse video": Processing.reverse_audio_video,
    "get details": Processing.get_video_details,
}

# obtaining keys to get a list of operations
operation_keys = operations_dict.keys()

# To take inut from the user and obtain single/multiple operation(s).
operations_to_perform = input(
    "Please enter comma seperated operations (space followed by comma required): "
    ).split(',')

# For loop that iterates over every operation passed by user
for operation in operations_to_perform:
    user_input_key = operation.lower().strip()
    if user_input_key in operation_keys:  # checks for user input in list of keys

        # obtaining the value of the associated key
        func_reference = operations_dict.get(user_input_key)
        print(func_reference()) # calling the method for the respective key
    else:
        print(
            f"---Unable to perform: {operation}, it is not a valid operation.")


