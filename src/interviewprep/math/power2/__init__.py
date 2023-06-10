from typing import Union


def is_power_of_2(n: Union[int, float]) -> bool:
    """Checks if the input number is a power of `2`

    Args:
        n (Union[int, float]): Input number

    Returns:
        bool: `True` if power of two, otherwise `False`.
    """
    if type(n) is int:
        return n & (n - 1) == 0
    else:
        return False


def next_power_of_2_left(n: int) -> int:
    """Returns the smallest integer power of `2`, greater than or equal to
    the input number. If the input is not an integer, it's fractional component
    is stripped off and only the integer component is considered as input.
    Examples:
        1->2, 2->2,3->4,4->4,5->8,6->8,7->8,8->8
        0->1,-1->1,-2->1,-3->1


    Args:
        n (int): Input number

    Returns:
        int: Smallest power of 2, greater than or equal to the input `n`.
    """
    n = int(n)
    if n < 1:
        return 1
    m = n - 1
    ctr = 0
    while n > 2**ctr:
        m |= m >> ctr
        ctr += 1
    m += 1
    return m


def next_power_of_2_right(n: int) -> int:
    """Returns the smallest integer power of `2`, strictly greater than the
    input number. If the input is not an integer, it's fractional component
    is stripped off and only the integer component is considered as input.
    Examples:
        1->2, 2->4,3->4,4->8,5->8,6->8,7->8,8->16
        0->1,-1->1,-2->1,-3->1


    Args:
        n (int): Input number

    Returns:
        int: Smallest power of 2, strictly greater than the input `n`.
    """
    n = int(n)
    if n < 1:
        return 1
    n += 1
    m = n-1
    ctr = 0
    while n > 2**ctr:
        m |= m >> ctr
        ctr += 1
    m += 1
    return m

next_power_of_2 = next_power_of_2_right

__all__ = [is_power_of_2, next_power_of_2, next_power_of_2_left, next_power_of_2_right]