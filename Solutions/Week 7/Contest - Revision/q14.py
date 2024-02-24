def mergeFiles(file1: str, file2: str, output_file: str) -> None:
    with open(file1, "r") as f1, open(file2, "r") as f2, open(
        output_file, "w"
    ) as out_f:
        for line in f1:
            out_f.write(line)

        # Add a separator between contents of file1 and file2
        out_f.write("\n\n")

        for line in f2:
            out_f.write(line)


file1 = "file1.txt"
file2 = "file2.txt"
output_file = "merged_file.txt"
mergeFiles(file1, file2, output_file)
