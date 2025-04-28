from pydub import AudioSegment
import sys


def convert_m4a_to_wav(input_file, output_file):
    """
    Converts an M4A file to WAV format using pydub's AudioSegment.

    Args:
        input_file (str): Path to the input M4A file.
        output_file (str): Path to the output WAV file.
    """
    try:
        # Load the M4A file
        audio = AudioSegment.from_file(input_file, format="m4a")

        # Export the audio as WAV
        audio.export(output_file, format="wav")
        print(f"Conversion successful: {output_file}")
    except Exception as e:
        print(f"Error during conversion: {e}")


# Example usage
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python towav.py <input_path> <output_path>")
        sys.exit(1)

    input_path = sys.argv[1]  # Get input file path from command-line argument
    output_path = sys.argv[2]  # Get output file path from command-line argument

    convert_m4a_to_wav(input_path, output_path)
