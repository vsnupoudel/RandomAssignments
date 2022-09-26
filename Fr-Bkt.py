class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        def start_from(start, maxs):
            total_picked = 0
            typelist = []
            flip_start = start
            while start < len_fruits:    
                fr = fruits[start]
                if  fr not in typelist:
                    typelist.append( fr )
                    if len(typelist)==2:
                        flip_start = start
                    if len(typelist)>2:
                        break 
                total_picked += 1
                start +=1
                
            if total_picked>maxs:
                maxs = total_picked
            return flip_start, maxs
 

        flip_start = 0; maxs = 0
        len_fruits = len(fruits)
        while True:
            last_flip = flip_start
            flip_start, maxs = start_from(flip_start, maxs)
            if flip_start == last_flip:
                break
            
        return maxs
    
 # Hashmap
def totalFruit( tree):
    count, i = {}, 0
    for j, v in enumerate(tree):
        count[v] = count.get(v, 0) + 1
        if len(count) > 2:
            count[tree[i]] -= 1
            if count[tree[i]] == 0: del count[tree[i]]
            i += 1
    return j - i + 1
                
                
        
