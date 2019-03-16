from sklearn.model_selection import StratifiedKFold

class OversampledStratifiedKFold:
    def __init__(self, n_splits=3):
        self.n_splits = n_splits

    def split(self, X, y, groups=None):

        for train_index, test_index in StratifiedKFold(n_splits=self.n_splits).split(X,y):
            nix = np.where(y[train_index]==0)[0]
            pix = np.where(y[train_index]==1)[0]
            pixu = np.random.choice(pix, size=nix.shape[0], replace=True)
            ix = np.append(nix, pixu)
            train_index_oversampled = rx[ix]
            yield train_index_oversampled, test_index

    def get_n_splits(self, X, y, groups=None):
        return self.n_splits
