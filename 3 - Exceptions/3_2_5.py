def read_file(file_name):
    try:
        print("__CONTENT_START__")
        with open(file_name) as f:
            print(f.read())
    except:
        print("__NO_SUCH_FILE__")
    finally:
        print("__CONTENT_END__")


read_file("test.txt")
