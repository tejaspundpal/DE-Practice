import logging
import os

def setup_logger(filename):
    # Avoid circular import by not naming this file 'logging.py'
    if os.path.basename(__file__) == 'logging.py':
        print("Warning: Rename this file to avoid conflict with Python's logging module.")
    # Create file if it doesn't exist
    if not os.path.exists(filename):
        with open(filename, 'w') as f:
            pass
    logger = logging.getLogger('PracticeLogger')
    logger.setLevel(logging.DEBUG)
    # Remove existing handlers to avoid duplicate logs
    if logger.hasHandlers():
        logger.handlers.clear()
    file_handler = logging.FileHandler(filename, mode='a')
    console_handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    return logger

def main():
    log_filename = 'app.log'  # You can change this filename as needed
    logger = setup_logger(log_filename)
    logger.info('Logging setup complete.')

    # Lambda function practice
    add = lambda x, y: x + y
    result = add(5, 3)
    logger.info(f'Lambda add(5, 3) = {result}')

    # List practice
    my_list = [1, 2, 3, 4, 5]
    logger.debug(f'Original list: {my_list}')
    list_squared = list(map(lambda x: x**2, my_list))
    logger.info(f'Squared list: {list_squared}')

    # Set practice
    my_set = set([1, 2, 2, 3, 4])
    logger.debug(f'Original set: {my_set}')
    my_set.add(5)
    logger.info(f'Set after adding 5: {my_set}')

    # Tuple practice
    my_tuple = (10, 20, 30)
    logger.debug(f'Tuple: {my_tuple}')
    tuple_sum = sum(my_tuple)
    logger.info(f'Sum of tuple: {tuple_sum}')

    # Dictionary practice
    my_dict = {'a': 1, 'b': 2, 'c': 3}
    logger.debug(f'Original dictionary: {my_dict}')
    my_dict['d'] = 4
    logger.info(f'Dictionary after adding d: {my_dict}')

    # Logging error example
    try:
        val = my_list[10]
    except IndexError as e:
        logger.error(f'IndexError: {e}')

if __name__ == "__main__":
    main()
