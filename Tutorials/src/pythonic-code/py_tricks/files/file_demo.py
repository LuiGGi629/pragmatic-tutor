# with open('test.txt', 'r') as f:
#     size_to_read = 10
#
#     f_contents = f.read(size_to_read)
#     print(f_contents, end='')
#
#     f.seek(0)
#
#     f_contents = f.read(size_to_read)
#     print(f_contents)

    # while len(f_contents) > 0:
    #     print(f_contents, end='*')
    #     f_contents = f.read(size_to_read)

# with open('test.txt', 'r') as rf:
#     with open('test-copy.txt', 'w') as wf:
#         for line in rf:
#             wf.write(line)
# with open('fill_line_plot.png', 'rb') as rf:
#     with open('fill_line_plot_copy.png', 'wb') as wf:
#         for line in rf:
#             wf.write(line)

# https://docs.python.org/3/library/functions.html#open

with open('fill_line_plot.png', 'rb') as rf:
    with open('fill_line_plot_copy.png', 'wb') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)

        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)
