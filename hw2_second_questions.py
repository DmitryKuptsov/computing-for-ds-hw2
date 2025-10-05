def has_experience_as(cvs, job_title):
    users = []
    for cv in cvs:
        if job_title in cv['jobs']:
            users.append(cv['user'])
    return users


def job_counts(cvs):
    dict_job_counts = {}
    for cv in cvs:
        for job in cv['jobs']:
            if dict_job_counts.get(job) is None:
                dict_job_counts[job] = 0
            dict_job_counts[job] += 1
    return dict_job_counts


def most_popular_job(cvs):
    dict_job_counts = job_counts(cvs)
    max_cnt = 0
    for job, cnt in dict_job_counts.items():
        if cnt > max_cnt:
            max_cnt = cnt
            max_job = job
    return (max_job, max_cnt)
