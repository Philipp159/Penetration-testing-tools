import os

path = "./test_folder"
keywords = ["password", "secret", "token"]

for root, dirs, files in os.walk(path):
    for file in files:
        full_path = os.path.join(root, file)
        try:
            with open(full_path, "r", errors="ignore") as f:
                content = f.read()
                for word in keywords:
                    if word in content:
                        print(f"[FOUND] {word} in {full_path}")
        except:
            pass
