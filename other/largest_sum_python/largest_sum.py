#!/usr/bin/python
import logging

logging.basicConfig(level=logging.DEBUG, format='%(message)s')


def largest(sequence):
    """
    This is based on Bentley's Programming Pearls chapter 8.  My
    modification: if the sequence is all negatives then max is the
    largest element
    """
    logging.debug('Sequence: {}'.format(sequence))
    max_so_far = max_up_to_here = 0
    largest_element = sequence[0]
    all_negatives = True

    for element in sequence:
        max_up_to_here = max(max_up_to_here + element, 0)
        max_so_far = max(max_so_far, max_up_to_here)
        largest_element = max(largest_element, element)
        if element >= 0:
            all_negatives = False

        logging.debug('  element:         {}'.format(element))
        logging.debug('  max_up_to_here:  {}'.format(max_up_to_here))
        logging.debug('  max_so_far:      {}'.format(max_so_far))
        # logging.debug('  largest_element: {}'.format(largest_element))
        # logging.debug('  all_negatives:   {}'.format(all_negatives))
        logging.debug('')

    if all_negatives:
        return largest_element
    return max_so_far
