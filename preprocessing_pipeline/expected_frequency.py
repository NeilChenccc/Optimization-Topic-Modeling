
class ExpF:
    def __init__(self, total_documents=0, freq=None):
        self.total_documents = total_documents
        if freq is not None:
            self.freq = freq

    def clean_obsexp(self, D, alpha, r, total_documents=None, freq=None):
        if total_documents is not None:
            self.total_documents = total_documents
        if freq is not None:
            self.freq = freq
        pipe = r.pipeline()
        clean_dataset = []
        for d in D:
            clean_document = []
            for term in d:
                key = 'term:{}:exp'.format(term)
                pipe.hgetall(key)
            freq_dicts = pipe.execute()
            for i in range(0, len(freq_dicts)):
                freq_dict = freq_dicts[i]
                term = d[i]
                exp_f = 0
                if 'exp_f' in freq_dict:
                    exp_f = float(freq_dict['exp_f'])
                if self.freq[term][2] / self.total_documents > alpha * exp_f:
                    clean_document.append(term)
            if len(clean_document) > 0:
                clean_dataset.append(clean_document)
        return clean_dataset

    def __str__(self):
        return 'ExpF'