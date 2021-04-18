from datasets import load_data
from deduplipy.active_learning import ActiveStringMatchLearner
from deduplipy.string_matcher import StringMatcher
from deduplipy.blocking import Blocking
from deduplipy.clustering import hierarchical_clustering
from deduplipy.deduplicator import Deduplicator

if __name__ == "__main__":
    df_train = load_data(kind='childcare', return_pairs=False)

    myDedupliPy = Deduplicator('name_address', 999, cache_tables=True)

    myDedupliPy.fit(df_train)
    res = myDedupliPy.predict(df_train)
    res.to_csv('res.csv')
    print(res)