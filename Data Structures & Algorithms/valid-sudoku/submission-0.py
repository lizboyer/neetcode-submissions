class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        x_ctr = 0
        y_ctr = 0
        col_array_dict = [{},{},{},{},{},{},{},{},{}]
        box_array_dict = [[{},{},{}],[{},{},{}],[{},{},{}]]
        for x in board: # iterate through rows
            x_ctr = x_ctr + 1
            row_dict = {}
            for y in x: # iterate through each item in row
                y_ctr = (y_ctr + 1) % 9
                print("x,y counter:",x_ctr, y_ctr)
                if (y != "."): print("x,y:",int(x_ctr)//3,int(y_ctr)//3)
                if (y != "."): print(box_array_dict[int(y_ctr-1)//3][int(x_ctr-1)//3])
                if (y != ".") and (row_dict.get(y)): return False # if the number has repeated in the row
                if (y != ".") and (col_array_dict[y_ctr].get(y)): return False # if the number has repeated in the col
                if (y != ".") and (box_array_dict[int(y_ctr-1)//3][int(x_ctr-1)//3].get(y)): return False # if the number has repeated in the col
                row_dict[y] = 1
                col_array_dict[y_ctr][y] = 1
                box_array_dict[int(y_ctr-1)//3][int(x_ctr-1)//3][y] = 1
        print(box_array_dict)
        return True