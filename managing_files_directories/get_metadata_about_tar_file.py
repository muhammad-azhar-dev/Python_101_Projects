import tarfile

def meta_info(names):
    with tarfile.open(names, "r") as tar:
        print(tar.getnames())

if __name__ == "__main__":
    meta_info("folder.tar")