def markdown_to_blocks(markdown):
    split_markdown_blocks = markdown.split("\n\n")
    stripped_markdown_blocks = []
    for block in split_markdown_blocks:
        stripped_markdown_blocks.append(block.strip())
    while "" in stripped_markdown_blocks:
        stripped_markdown_blocks.remove("")
    return stripped_markdown_blocks
