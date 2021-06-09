def conjunct(first_list, second_list):
    return any(map(lambda first: first in second_list, first_list))

def disjunct(first_list, second_list):
    return not any(map(lambda first: first in second_list, first_list))

def conjunct_attr(value, in_list):
    return any(map(lambda item: item in value, in_list))

def not_in(value, block_list):
    return value not in block_list

def in_attr(value, in_list, attribute):
    return any(map(lambda element: element[attribute] == value, in_list))

def package_divide(package, manager, package_managers):
    prioritized_managers = list(filter(lambda package_manager: package_manager in package, package_managers))
    if not prioritized_managers:
        return False
    return prioritized_managers[0] == manager

class TestModule(object):
    def tests(self):
        return {'conjunct': conjunct, 'disjunct': disjunct, 'conjunct_attr': conjunct_attr, 'not_in': not_in, 'in_attr': in_attr, 'package_divide': package_divide}
