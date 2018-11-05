"""Sample module"""
import logging


def sample_func(say=True):
    """Sample func"""
    logging.debug("Enter sample_func()")
    if say:
        print "::: Sample func"
    return True


if __name__ == "__main__":
    sample_func()
