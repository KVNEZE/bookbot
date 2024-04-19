def main():
  def count_words(words):
    return len(words.split())
  
  def sort_on(dict):
    return dict["value"]
  
  def count_letters(words):
    dict = {}
    dict_list = []
    letters = list(words.lower())

    for letter in letters:
      if letter.isalpha():
        entry = dict.get(letter)

        if entry == None:
          dict[letter] = 1
        else:
          dict[letter] += 1

    for key, value in dict.items():
      dict_list.append({ "key": key, "value": value })
    
    dict_list.sort(reverse=True, key=sort_on)

    return dict_list

  BOOK_PATH = "./books/frankenstein.txt"

  with open(BOOK_PATH) as f:
    file_contents = f.read()
    # number_of_words = count_words(file_contents)
    number_of_letters = count_letters(file_contents)

    print(f"-- Begin report of {BOOK_PATH} ---")

    for item in number_of_letters:
      print(f"The {item["key"]} character was found {item["value"]} times")

    print ("--- End report ---")
  
main()