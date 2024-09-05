from .utils import TestSample

class Protocol:
    def __init__(self, population_size: int, prevalence: float):
        self.n = population_size
        self.p = prevalence
    
    def isolate_positives(self, sample: TestSample) -> set:
        def binary_search(pool):
            if len(pool) == 1:
                return set(pool) if sample.query(pool) else set()
            else:
                mid = len(pool) // 2
                left, right = pool[:mid], pool[mid:]

                positives = set()

                if sample.query(left):
                    positives = positives.union(binary_search(left))

                if sample.query(right):
                    positives = positives.union(binary_search(right))

                return positives

        full_pool = list(range(self.n))
        return binary_search(full_pool)