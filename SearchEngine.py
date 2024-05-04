def read_documents(doc_file):
    """
    It opens the document file
    Reads it
    Divide and format content into a dictionary
    document number as key and content as value
    """
    doc_content = {}
    current_content = []
    with open(doc_file, 'r') as file:
        content_number = 0
        for line in file:
            if line.strip() == "<NEW DOCUMENT>":
                doc_content[content_number] = ' '.join(current_content)
                current_content = []
                content_number += 1
            else:
                current_content.append(line.strip())
        doc_content[content_number] = ' '.join(current_content)
    return doc_content


def create_index(doc_content):
    """
    Creates index in a dictionary
    words as keys and document numbers as values.
    """
    index = {}
    for doc_num, content in doc_content.items():
        words = content.lower().split()
        for word in words:
            if word not in index:
                index[word] = {doc_num}
            else:
                index[word].add(doc_num)
    return index


def search_words(index, search_word):
    """
    Searches the user input from the dictionary
    returns the document the user input is in
    """
    search_word = search_word.lower().split()
    relevant_content = None
    for word in search_word:
        if word in index:
            if relevant_content is None:
                relevant_content = index[word]
            else:
                relevant_content = relevant_content.intersection(index[word])
        else:
            return set()
    return relevant_content


def main():
    """
    Main function
    runs the program
    """
    doc_file = "ap_docs.txt"
    doc_paragraph = read_documents(doc_file)
    index = create_index(doc_paragraph)

    while True:
        print("\nWhat would you like to do?")
        menu_items = ["Search for documents", "Read Document", "Quit Program"]
        for i, option in enumerate(menu_items, start=1):
            print(f"{i}. {option}")

        user_input = input("Enter your option: ")

        if user_input.isdigit():
            user_option = int(user_input)
            if 1 <= user_option <= 3:
                if user_option == 1:
                    search_input = input("Enter search words separated by space: ")
                    relevant_content = search_words(index, search_input)
                    if relevant_content:
                        print("Relevant documents found:", relevant_content)
                    else:
                        print("No relevant documents found for the given search words.")

                elif user_option == 2:
                    try:
                        doc_num = int(input("Enter document number: "))
                        if doc_num not in doc_paragraph:
                            print("Invalid document number.")
                        else:
                            print(f"Document #{doc_num}: {doc_paragraph[doc_num]}")
                    except ValueError:
                        print("Invalid input. Please enter a valid document number.")

                elif user_option == 3:
                    print("Closing program...")
                    break
            else:
                print("Please enter a number between 1 and 3!")
        else:
            print("Please enter a valid number! (1-3): ")


if __name__ == "__main__":
    main()
