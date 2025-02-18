

# CMPS 2200 Assignment 1

**Name:** Dylan Mondrus


In this assignment, you will learn more about asymptotic notation, parallelism, functional languages, and algorithmic cost models. As in the recitation, some of your answer will go here and some will go in `main.py`. You are welcome to edit this `assignment-01.md` file directly, or print and fill in by hand. If you do the latter, please scan to a file `assignment-01.pdf` and push to your github repository. 
  
  

1. (2 pts ea) **Asymptotic notation** (12 pts)

  - 1a. Is $2^{n+1} \in O(2^n)$? Why or why not? 
.  Yes because we can find a constant c=2 such that big O is satisfied. 

.  
.  
.  
. 
  - 1b. Is $2^{2^n} \in O(2^n)$? Why or why not?     
.  No because 2^2^n grows much faster than 2^n. There is no constant c that can make 
  - C * 2^n catch up to 2^2^n.
.  
.  
.  
.  
  - 1c. Is $n^{1.01} \in O(\mathrm{log}^2 n)$?    
.  
.  No because polynomial functions always grow faster than polylogarithmic,
so big O is not satisfied. 
.  
.  

  - 1d. Is $n^{1.01} \in \Omega(\mathrm{log}^2 n)$?  
.  Yes because n^1.01 grows at least as fast as log^2 n, so omega is satisfied.
.  
.  
.  
  - 1e. Is $\sqrt{n} \in O((\mathrm{log} n)^3)$?  
.  No because polynomial grows faster than polylogarithm, so big O is not satisfied. 
.  
.  
.  
  - 1f. Is $\sqrt{n} \in \Omega((\mathrm{log} n)^3)$?  
.  Yes because polynomial grows faster than polylogarithm, so omega is satisfied. 


2. **SPARC to Python** (12 pts)

Consider the following SPARC code of the Fibonacci sequence, which is the series of numbers where each number is the sum of the two preceding numbers. For example, 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610 ... 
$$
\begin{array}{l}
\mathit{foo}~x =   \\
~~~~\texttt{if}{}~~x \le 1~~\texttt{then}{}\\
~~~~~~~~x\\   
~~~~\texttt{else}\\
~~~~~~~~\texttt{let}{}~~(ra, rb) = (\mathit{foo}~(x-1))~~,~~(\mathit{foo}~(x-2))~~\texttt{in}{}\\  
~~~~~~~~~~~~ra + rb\\  
~~~~~~~~\texttt{end}{}.\\
\end{array}
$$ 

  - 2a. (6 pts) Translate this to Python code -- fill in the `def foo` method in `main.py`  

  - 2b. (6 pts) What does this function do, in your own words?  

.  This function recursively implements the fibonacci sequence in reverse. First, it sets up a
base case that ends the loop if x is equal to 1 or 0. If x is not 0 or 1, it calculates
the previous(or next) value in the sequence by adding the last 2 values together,
and returning that back in until it reaches 1 or 0. 
.  
.  
.  
.  
.  
.  
.  
  

3. **Parallelism and recursion** (26 pts)

Consider the following function:  

```python
def longest_run(myarray, key)
   """
    Input:
      `myarray`: a list of ints
      `key`: an int
    Return:
      the longest continuous sequence of `key` in `myarray`
   """
```
E.g., `longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3`  
 
  - 3a. (7 pts) First, implement an iterative, sequential version of `longest_run` in `main.py`.  

  - 3b. (4 pts) What is the Work and Span of this implementation?  

.  The work is O(n) because the function has to traverse the list 
n times for n elements in the list. 
The span is O(n) because the function is not parallelized because none of the 
loops or checks in the function rely on each other, so the span is the same as the work.
.  
.  
.  
.  
.  
.  
.  
.  


  - 3c. (7 pts) Next, implement a `longest_run_recursive`, a recursive, divide and conquer implementation. This is analogous to our implementation of `sum_list_recursive`. To do so, you will need to think about how to combine partial solutions from each recursive call. Make use of the provided class `Result`.   

  - 3d. (4 pts) What is the Work and Span of this sequential algorithm?  
.  
.  The work is W(n) = 2W(n/2) + O(1) because of each recursive call for the two
halves of the list, and the merge step operation is O(1). 
.  
The span is S(n) = S(n/2) + O(1) because the function is parallelized 
so the two recursive calls can be made at the same time(in parallel), so only
one S(n/2) is needed. But the merge operation is still needed so the 
O(1) is added at the end. 
.  
.  
.  
.  
.  
.  
.  
.  


  - 3e. (4 pts) Assume that we parallelize in a similar way we did with `sum_list_recursive`. That is, each recursive call spawns a new thread. What is the Work and Span of this algorithm?  

.  The work is W(n) = O(n) for a = 2, b = 2, f(n) = O(1).
The span is S(n) = O(log n) for a = 1, b = 2, f(n) = O(1).
.  
.  
.  
.  
.  
.  

