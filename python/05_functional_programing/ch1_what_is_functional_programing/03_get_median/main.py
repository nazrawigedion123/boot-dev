def get_median_font_size(font_sizes: list[int]) -> int | None:
    font_sizes=sorted(font_sizes)
    print(f"sorted font_sizes: {font_sizes}")
    if len(font_sizes)==0:
        return

    i :int = int(len(font_sizes)/2)
    if len(font_sizes)%2==0:
        return font_sizes[i-1]
    return font_sizes[i]

