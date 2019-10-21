def main(lists):
    lists.sort()
    for index, val in enumerate(lists):
        if(val == 0):
            lists.remove(lists[index])
            lists.append(val)
            
    return lists
    
if __name__ == "__main__":
    print(main([0,2, 0,12,0, 0,4]))
