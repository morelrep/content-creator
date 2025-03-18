import pandas as pd
from slugify import slugify

# Create a DataFrame from the CSV file
data = pd.read_csv("../../../_data/books.csv", sep=',', engine='python', encoding="utf-8").fillna('')

# Convert the DataFrame into a list of rows for processing
books = data.values.tolist()

# Loop through each book record
for book in books:
    # Split the authors column into individual authors
    authors_array = book[3].split("; ")

    for author in authors_array:
        # Split each author into "Lastname" and "Name" parts
        author_array = author.split(", ")

        # Check if the author_array has both "Lastname" and "Name"
        if len(author_array) < 2:
            print(f"Skipping invalid author format: '{author}'")
            continue  # Skip this author and move to the next one

        # Generate the slugified URL for the author
        url_raw = f"{author_array[0]}-{author_array[1]}"  # Combine Lastname and Name
        url = slugify(url_raw)  # Use the slugify library to make it URL-safe

        # Define the output file name
        file_name = f'../../../_authors/{url}.md'

        # Write the author details to the .md file
        title = str(author)  # Use the full author name for the title
        with open(file_name, 'w', encoding="utf-8") as f:
            f.write(f'---\ntitle: {title}\n---')  # Write the YAML front matter
            f.close()  # Close the file explicitly

        # Log the saved file
        print(f'{file_name} saved')
