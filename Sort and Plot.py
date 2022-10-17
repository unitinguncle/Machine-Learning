"""Problem 02 - Sort and Plot
Write a function called sort_and_plot(x) that sort the input sequence x and display the sorted sequence in both ascending and descending order using matplotlib.pyplot. This visualization shows you the result of sorting.

Do not create tick marks for x-axis.
Include legends for points displayed. """

from typing import List
import matplotlib.pyplot as plt


def sort_and_plot(x: List[int]) -> None:
    # Write Code Here
    plt.tick_params(bottom = False)
    plt.bar(np.arange(len(x)) - 0.2,sorted(x),0.4, color= 'Red', label='Ascending', alpha=1)
    plt.bar(np.arange(len(x)) + 0.2,sorted(x,reverse = True),0.4, color= 'Blue', label='Descending', alpha=1)
    plt.xlabel('Place')
    plt.ylabel('Number')
    plt.legend()
    
    plt.show()
    plt.close()


    return None
