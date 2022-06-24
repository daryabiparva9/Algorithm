# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    '''
    This function takes capacity of knapsack, 
    the weights and values of item that could potentially be put in the knapsack
    and returns the maximum value that can be put in knapsack.
    
    The items can be put in franctions 
    '''
    
    #initializing the final value of knapsack to zero
    
    final_value = 0.
    if capacity == 0:
        return 0
    
    #we make a list of tuples, where each tuple is of the form:
    #((weight, value), value_divided_by_weight)
    #The list is sorted descending in value_divided_by_weight
    
    w_v = tuple(zip(weights, values))
    value_per_weight = [i[1]/i[0] for i in w_v]
    w_v_u = tuple(zip(w_v, value_per_weight))
    sorted_v = sorted(w_v_u, reverse=True, key=lambda i: i[1])
    
    #adding the whole item if capacity >= weight of the item
    #otherwise, adding the fraction that could fit in the knapsack 
    for item in sorted_v:
        weight, value = item[0]
        if capacity >= weight:
            final_value += value
            capacity -= weight
        else:
            final_value += capacity * value / weight
            capacity = 0
            
        if capacity <= 0:
            break
    

    return final_value





if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
#trying to change this file
#checking git