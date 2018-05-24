def answer_one():
    return df[df['Gold'] == df['Gold'].max()].index[0]

answer_one()