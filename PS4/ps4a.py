# Problem Set 4A
# Name: llewellyndm
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    if len(sequence) == 1:
        return [sequence]
    else:
        previous_perms = get_permutations(sequence[1:]) #recursive step
        first_letter = sequence[0]
        permutations = []
        for perm in previous_perms:
            #for each character in that permutation
            for i in range(len(perm)):
                # make a new permutation of sequence by inserting the first
                # letter of sequence before that character
                new_perm = list(perm)
                new_perm.insert(i, first_letter)
                new_perm_joined = ''.join(new_perm)
                # ensure permutation is not a duplicate
                if new_perm_joined not in permutations:
                    permutations.append(new_perm_joined)
            # make an extra permutation by placing the first letter at the end
            # of the permutation
            extra_perm = list(perm)
            extra_perm.append(first_letter)
            extra_perm_joined = ''.join(extra_perm)
            if extra_perm_joined not in permutations:
                permutations.append(extra_perm_joined)
        return permutations

if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    pass #delete this line and replace with your code here

