# import sys
# sys.path.append('scripts/')
import subprocess
# import compress_output
import cleanup_output

def main():
    print("Starting content generation...")
    subprocess.run(["python", "assets/env/src/morel-generate.py"], check=True)

    # print("Compressing output...") # Comment this out if skipping compression
    # compress_output.create_zip() # Comment this out to disable compression

    print("Cleaning up generated files...")
    cleanup_output.delete_generated_files()

    print("Process complete.")

if __name__ == "__main__":
    main()
