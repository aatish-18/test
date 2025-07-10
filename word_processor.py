
class WordVectorizer :
    def __init__(self):
        self.vocab =[]
        self.token_dict = {}

    def vocab_builder(self , file_path) :
        with open(file= file_path) as file :
            for lines in file.readlines() :
                words = lines.strip()
                self.vocab.append(words)
                print("done")

    def printer(self):
        print(self.vocab)



first = WordVectorizer()
first.vocab_builder("shakespeare.txt")
first.printer()


        