class SimilarityEvaluator(object):
    def compute_similarity(self, output, batch_output):
        """
        an output with higher frequency in the batch needs to be given a lower score

        :param output: output data point who's length is being scored
        :param batch_output: the batch of data points to score against
        :return:
        """
        raise NotImplementedError


class LengthModerator(object):
    def score_length(self, output, batch_output):
        """
        score for output increases as it grows closer to the batch average

        :param output: output data point who's length is being scored
        :param batch_output: the batch of data points to score against
        :return:
        """
        raise NotImplementedError


class LossHelper(object):

    def variance(self, output, batch_output):
        pass

    def length(self, output, batch_output):
        pass
