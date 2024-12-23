def countSides(area):
    corner_canditades = set()

    for r, c in area:
        for corner_r, corner_c in [(r - 0.5, c - 0.5), (r - 0.5, c + 0.5), (r + 0.5, c - 0.5), (r + 0.5, c + 0.5)]:
            corner_canditades.add((corner_r, corner_c))

    corners = 0
    for corner_r, corner_c in corner_canditades:
        config = [(sr, sc) in area for sr, sc in [
            (corner_r - 0.5, corner_c - 0.5), 
            (corner_r - 0.5, corner_c + 0.5), 
            (corner_r + 0.5, corner_c - 0.5), 
            (corner_r + 0.5, corner_c + 0.5)
        ]]
        num = sum(config)
        
        if num == 1:
            corners += 1
        elif num == 2:
            if config == [True, False, True, False] or config == [False, True, False, True]:
                corners += 2
        elif num == 3:
            corners += 1

    return corners