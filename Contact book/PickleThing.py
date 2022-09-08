import pickle


def pickling(contacts):
    with open('ContactBase.txt', 'wb') as CB:
        pickle.dump(contacts, CB)


def unpikling():
    with open('ContactBase.txt', 'rb') as CB:
        load_file = pickle.load(CB)
        return load_file


change_file = {}
change_file = unpikling()
