def oxford_comma(items):
    if len(items) == 0:
        return ""
    elif len(items) == 1:
        return items[0]
    elif len(items) == 2:
        return f"{items[0]} and {items[1]}"
    else:
        # Oxford comma: insert comma before the final item
        last_item = items.pop()
        item_str = ", ".join(items)
        return f"{item_str}, and {last_item}"
