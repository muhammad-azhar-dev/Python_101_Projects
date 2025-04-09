from zipfile import ZipFile

def meta_info(names):
    with ZipFile(names) as zf:
        print(len(zf.infolist()))
        for info in zf.infolist():
            print('file_name:',info.filename)
            
            if info.create_system == 0:
                system = "Windows"
            elif info.create_system == 3:
                system = "Unix"
            else:
                system = "UNKNOWN"

            print("System:", system)
            print(" zip version:", info.create_version)
            print("compressed:", info.compress_size, "bytes")
            print("uncompressed:", info.file_size, "bytes")

            print()

if __name__ == "__main__":
    meta_info("testing.zip")