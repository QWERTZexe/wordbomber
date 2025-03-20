#    Wordbomber
#    Copyright (C) 2025  QWERTZ_EXE
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

import requests
import random

def get_word_list(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text.splitlines()
    else:
        print("Failed to fetch word list. Using a small default list.")
        return ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]

def find_matching_words(letters, word_list):
    matching = [word for word in word_list if letters in word]
    return sorted(matching, key=len) 

def wordbomb_helper():
    """Main function to play the word game."""

    urls = [
        "https://raw.githubusercontent.com/first20hours/google-10000-english/refs/heads/master/google-10000-english-usa.txt",
        "https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt",
        "https://gist.githubusercontent.com/h3xx/1976236/raw/bbabb412261386673eff521dddbe1dc815373b1d/wiki-100k.txt"
    ]

    print("Available word lists:")
    for i, url in enumerate(urls):
        print(f"{i+1}. {url}")

    while True:
        try:
            choice = input("Choose a word list (1-{} or 'q' to quit): ".format(len(urls)))
            if choice.lower() == 'q':
                return  # Exit the function
            choice_index = int(choice) - 1
            if 0 <= choice_index < len(urls):
                selected_url = urls[choice_index]
                break  # Exit the loop if a valid choice is made
            else:
                print("Invalid choice. Please enter a number between 1 and {}.".format(len(urls)))
        except ValueError:
            print("Invalid input. Please enter a number or 'q'.")

    print("Fetching word list...")
    word_list = get_word_list(selected_url)

    if not word_list:
        print("No words loaded.  Exiting.")
        return

    print(f"Loaded {len(word_list)} words.")

    while True:
        print("\n")
        letters = input("Enter 3 letters (or 'q' to quit): ").lower()
        if letters == 'q':
            break

        matching_words = find_matching_words(letters, word_list)

        if matching_words:
            print(f"Found {len(matching_words)} matching words.")
            print(f"Random matching word: {random.choice(matching_words)}")
            print(f"Random #2 match word: {random.choice(matching_words)}")
            print(f"Shortest matching word: {matching_words[0]}")

            show_more = input("Show all matching words? (y/n): ").lower()
            if show_more == 'y':
                for word in matching_words:
                    print(word)
        else:
            print("No matching words found.")

if __name__ == "__main__":
    wordbomb_helper()
