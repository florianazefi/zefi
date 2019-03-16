import unittest

class Test(unittest.TestCase):

    def test_oversampling_kfold(self):

        from sklearn.datasets import make_classification
        from zefi.tools import OversampledStratifiedKFold
        import numpy as np

        X, y = make_classification(weights=[0.9, 0.1])

        kfold = OversampledStratifiedKFold(n_splits = 3)

        for train_index, test_index in kfold.split(X, y):

            n_0 = len(np.where(y[train_index]==0)[0])
            n_1 = len(np.where(y[train_index]==1)[0])

            self.assertEqual(n_0, n_1)


if __name__ == "__main__":

    unittest.main(verbosity=2)
