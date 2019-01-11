dict_ = {i+1: height[i] for i in range(len(height))}
        for i, v in dict_.items():
            for j, v_ in {j: v_ for (j, v_) in dict_.items() if v_ >= v}.items():
                area = v * abs(j - i)
                max_area = max(area, max_area)
        return max_area
        