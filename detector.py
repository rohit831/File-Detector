import cchardet as chardet

def get_encoding(src_path):
    with open(src_path, "rb") as f:
        msg = f.read()
        result = chardet.detect(msg)
        return result['encoding']


# if __name__ == "__main__":
#     print(get_encoding("/media/rohit/New Volume/Learning/mailids"))
