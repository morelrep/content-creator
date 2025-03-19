# import sys
# sys.path.append('scripts/')

import morel_generate
import compress_output
import cleanup_output

def main():
    print("Starting content generation...")

    # print("Compressing output...")  # Comment this out if skipping compression
    # compress_output.create_zip()    # Comment this out to disable compression

    print("Cleaning up generated files...")
    cleanup_output.delete_generated_files()

    print("Process complete.")

if __name__ == "__main__":
    main()
