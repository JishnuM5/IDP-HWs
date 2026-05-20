"""
Jishnu Mehta
Intermediate Data Programming

Description:
    This program runs the search engine, taking user input
"""
from search_engine import SearchEngine


def main():
    '''
    This is the main method that runs the search engine in the command line
    '''
    directory = input("Please enter the name of a directory: ")
    print("Building Search Engine...")
    engine = SearchEngine(directory)
    query = input("Please enter a search term or query (press Enter to quit): ")
    # Loop that runs until user quits
    while query != "":
        result_list = engine.search(query)
        print(f"Displaying results for '{query}': ")
        if (len(result_list) == 0):
            print("No results :(")
        else:
            for i in range(len(result_list)):
                print(f"{i+1}. {result_list[i]}")
        query = input("Please enter a search term or query (press Enter to quit): ")
    print("Thank you for searching. \n")


if __name__ == '__main__':
    main()