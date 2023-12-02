max_chapters= -1
book_max=""
with open("books_and_chapters.txt") as books_file:
    for line in books_file:
        parts=line.split(":")
        book=parts[0]
        chapters=int(parts[1])
        scripture=parts[2].strip()
        print(f"Scripture: {scripture}, Book: {book}, Chapters: {chapters}")
        if chapters > max_chapters:
            max_chapters=chapters
            book_max=book
print(f"The book with the most chapters is: {book_max}")
print(f"It has {max_chapters} chapters.")    