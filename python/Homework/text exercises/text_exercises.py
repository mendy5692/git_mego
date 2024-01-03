def text_status():

    # read the file with the path thet you got from the user
    with open(input("Enter a path of a text file: ")) as text_read:
        text = text_read.read()
        text_read = text.lower()

    # chang the all bad characters to an amity string
    bad_characters = ["\n","?", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "=", "+", "/", ",", ".", "<", ">", "'", "~", "`", ":", ";", "[", "]", "{", "}", "|"]
    for i in bad_characters:
        if i == "\n":
            text_read = text_read.replace(i, " ")
        else:
            text_read = text_read.replace(i,"")

    # num of words
    num_of_words = len(text_read.split(" "))

    # list_and_sum_of_repeted_words
    repeted_sum_words = 0
    repeted_list_words = {}
    for i in text_read.split(" "):
            if i not in repeted_list_words.keys():
                times = text_read.count(i)
                if times != 1:
                    repeted_list_words[i] = times
                    repeted_sum_words += times / times

    #num of uniq words
    num_of_uniq_words = int(num_of_words - repeted_sum_words)

    # print num of words
    print(f"\nNumber of words: {num_of_words}")

    # print num of uniq words
    print(f"Number of unique words: {num_of_uniq_words}\n")

    # print the repeted words in their num of repetion
    for i in repeted_list_words:
        print(f"the word \"{i}\" is appears \"{repeted_list_words[i]}\" times.")

text_status()