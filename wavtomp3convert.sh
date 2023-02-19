# converts all .wav files in a folder to .mp3
# Set the path to the folder containing the .WAV files
input_folder="INSERT FOLDER PATH HERE"

# Set the path to the output folder for the converted .mp3 files
output_folder="OUTPUT FOLDER PATH"

# Loop through all .WAV files in the input folder
for wav_file in "$input_folder"/*.wav; do
    # Extract the filename (without extension) from the input file path
    filename=$(basename "$wav_file" .wav)
    
    # Set the output file path with the same name, but with .mp3 extension
    mp3_file="$output_folder/$filename.mp3"
    
    # Use ffmpeg to convert the .WAV file to .mp3
    ffmpeg -i "$wav_file" -codec:a libmp3lame -qscale:a 2 "$mp3_file"
    
    echo "Converted $filename.wav to $filename.mp3"
done
