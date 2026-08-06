def format_line(line: str) -> str:
    res=line.strip()
    res= res.upper()
    res=res.replace('.', '')
    return f"{res}..."

