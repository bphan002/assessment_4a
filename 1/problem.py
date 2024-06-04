class Solution:
    def minCost(self, costs):
        #length of costs is the number of houses to paint
        num_houses = len(costs)
        memo = {}
        #each subarray represents the cost to use each color
        #red blue green
        # the following subarray cannot use the same index as the previous
        # we want to minimize the cost
        #there will be 3 branches 
        def _dfs(curr_house, prev_color,curr_color):
           #when we reach the last house we know we are done
           #base case
             # if it hits the the end of the length
                if curr_house == num_houses:
                     return 0 
                if prev_color == curr_color:
                     return float('inf')
                if (curr_house, prev_color) in memo:
                     return memo[(curr_house,prev_color, curr_color)]

            #iterate through all of the colors
                # curr_red_cost = costs[curr_house][0] if prev_color != 0 else float('inf')
                # curr_blue_cost = costs[curr_house][1] if prev_color != 1 else float('inf')
                # curr_green_cost = costs[curr_house][2] if prev_color != 2 else float('inf')
                # print('curr_house', curr_house)
                # print('curr red', curr_red_cost)
                # print('curr blue', curr_blue_cost)
                # print('curr green', curr_green_cost)
                # curr_min = min(curr_red_cost, curr_blue_cost, curr_green_cost)
                # mapping = {
                #      curr_red_cost:0, # maps to red
                #      curr_blue_cost:1, #maps to blue
                #      curr_green_cost:2 # maps to green
                #      }
                # curr_min_color = mapping[curr_min] 
                # print('curr_min_color', curr_min_color)
                # print('curr_min_color', curr_min_color)

                red = _dfs(curr_house + 1, curr_color,0) 
                blue = _dfs(curr_house + 1, curr_color,1) 
                green = _dfs(curr_house + 1, curr_color,2)
                memo[(curr_house,prev_color, curr_color)] = costs[curr_house][curr_color] + min(red, blue, green)
                return memo[(curr_house,prev_color, curr_color)]
        results = float('inf')
        
        for i in range(len(costs[0])):
             min_cost = _dfs(0,-1,i)
             results = min(results, min_cost)     
        # print('memo', memo)
        # print('results', results)
        return results
         

