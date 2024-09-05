from .utils import TestSample

class Protocol:
    def __init__(self, population_size: int, prevalence: float):
        self.n = population_size
        self.p = prevalence
    
    def isolate_positives(self, sample: TestSample) -> set:
        # Implement your strategy here.
        # 
        # 
        # Your goal is to return the indices of the positive samples
        # while minimizing the number of calls to sample.query
        #
        # Not correctly identifying the set of positive samples results in disqualification!
        #
        # The input will be a TestSample object, which allows you to query
        # a subset of 0 ... n-1
        #
        # sample.query([1, 3, 4]) will return True if any of 1, 3, or 4 are positive
        # return {i for i in range(self.n) if sample.query(set([i]))}

        if sample.query(set)(range(self.n)):
            # true
            return sample.query(set)(range(0, self.n /2))
            return sample.query(set)(range(self.n / 2 , self.n))
            
        else 
            # false
            return {}

       