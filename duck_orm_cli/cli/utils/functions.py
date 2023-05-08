import logging


def load_path(dir_migration):
    from importlib.machinery import SourceFileLoader

    return SourceFileLoader("module.name", dir_migration).load_module()


def log_info(msg):
    print(msg)
    logging.info(msg)


def log_error(msg):
    print(msg)
    logging.error(msg)
